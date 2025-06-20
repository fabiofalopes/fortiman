import asyncio
import pandas as pd
from playwright.async_api import async_playwright, TimeoutError, Page
from datetime import datetime
import re
import os
from dotenv import load_dotenv

# --- Carregar variáveis de ambiente ---
# Crie um ficheiro chamado '.env' na mesma diretoria deste script
# e adicione as seguintes linhas (substituindo com os seus dados):
# FORTIGATE_URL="https://seu_endereco_fortigate"
# USERNAME="seu_utilizador"
# PASSWORD="sua_password"
load_dotenv()

# --- Configuração ---
FORTIGATE_URL = os.getenv("FORTIGATE_URL")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
AUTH_FILE = "auth_state.json"

# --- Nova Configuração de Filtro ---
# Deixe em branco ("") para não aplicar nenhum filtro.
FILTER_COLUMN_NAME = "Native VLAN"  # O nome exato da coluna como aparece na UI
FILTER_VALUE = "_sw"                # O valor a ser procurado

# --- Exemplos de outros filtros (descomente para usar) ---
# FILTER_COLUMN_NAME = "Description"
# FILTER_VALUE = "TRUNK"

# --- Seletores (Baseado no PLAN_UI_Scraping.md) ---
USER_SELECTOR = "#username"
PASS_SELECTOR = "#secretkey"
LOGIN_BUTTON_SELECTOR = "#login_button"
PORTS_PAGE_NAV_TEXT = "FortiSwitch Ports"
TABLE_CONTAINER_SELECTOR = "div.mutable-table-container"
NATIVE_VLAN_FILTER_ICON_SELECTOR = 'div[data-column-id="vlan"] button.column-settings'
FILTER_INPUT_SELECTOR = 'input[placeholder="value1, value2, etc."]'
FILTER_APPLY_BUTTON_SELECTOR = 'div.footer > button.primary'
SCROLL_CONTAINER_SELECTOR = 'div.table-container'
SECTION_ROW_SELECTOR = 'div.row.section'
DATA_ROW_SELECTOR = 'div.row.selectable'

async def login_and_navigate(page: Page):
    """Executa o processo completo de login e navegação para a página de portas."""
    print("--- A iniciar processo de login completo ---")
    print(f"A navegar para: {FORTIGATE_URL}")
    await page.goto(FORTIGATE_URL, timeout=60000)

    print(f"A preencher o campo de utilizador com o seletor: '{USER_SELECTOR}'")
    await page.fill(USER_SELECTOR, USERNAME)
    
    print(f"A preencher o campo da password com o seletor: '{PASS_SELECTOR}'")
    await page.fill(PASS_SELECTOR, PASSWORD)
    
    print(f"A clicar no botão de login com o seletor: '{LOGIN_BUTTON_SELECTOR}'")
    await page.click(LOGIN_BUTTON_SELECTOR)

    print(f"Login efetuado. A aguardar pelo link de navegação com o texto: '{PORTS_PAGE_NAV_TEXT}'")
    nav_link = page.get_by_text(PORTS_PAGE_NAV_TEXT, exact=True)
    await nav_link.wait_for(state="visible", timeout=30000)
    
    print("Link de navegação encontrado. A clicar para ir para a página de portas.")
    await nav_link.click()
    print("--- Login e navegação concluídos ---")

async def get_visible_columns(page: Page) -> dict:
    """
    Lê os cabeçalhos da tabela que estão visíveis e retorna um dicionário
    mapeando o 'data-column-id' para o nome de exibição da coluna.
    """
    print("--- A ler os cabeçalhos das colunas visíveis ---")
    header_cells_selector = 'div.fixed-header-container div.header-cell'
    
    try:
        await page.wait_for_selector(header_cells_selector, state="visible", timeout=10000)
        header_cells = page.locator(header_cells_selector)
        count = await header_cells.count()
        
        visible_columns = {}
        for i in range(count):
            cell = header_cells.nth(i)
            column_id = await cell.get_attribute("data-column-id")
            label_element = cell.locator("span.header-cell-label")
            
            if column_id and await label_element.count() > 0:
                column_name = await label_element.inner_text()
                visible_columns[column_id] = column_name.strip()
                
        print(f"Detetadas {len(visible_columns)} colunas visíveis.")
        return visible_columns

    except Exception as e:
        print(f"ERRO ao ler os cabeçalhos das colunas: {e}")
        return {}

async def set_all_columns_visible(page: Page):
    """
    Abre o menu de contexto da tabela, seleciona todas as colunas
    que não estão visíveis e aplica as alterações.
    """
    print("--- A iniciar processo para tornar todas as colunas visíveis ---")

    # Selector corrigido com base na análise do full.html
    header_selector = 'div.fixed-header-container div.header-cell[data-column-id="port-name"]'
    menu_selector = "div.pop-up-menu-tooltip"
    menu_items_selector = f'{menu_selector} div.auto-overflow .menu-item button'
    apply_button_selector = f'{menu_selector} .footer button.primary'

    try:
        await page.wait_for_selector(header_selector, state="visible", timeout=20000)
        print(f"A clicar com o botão direito no cabeçalho: '{header_selector}'")
        await page.click(header_selector, button="right")

        print(f"A aguardar pelo menu de seleção de colunas: '{menu_selector}'")
        await page.wait_for_selector(menu_selector, state="visible", timeout=10000)
        print("Menu de seleção de colunas encontrado.")

        menu_items = page.locator(menu_items_selector)
        items_count = await menu_items.count()
        print(f"Encontrados {items_count} itens de coluna no menu.")
        
        clicked_something = False
        for i in range(items_count):
            item = menu_items.nth(i)
            icon = item.locator("f-icon")
            icon_class = await icon.get_attribute("class")
            
            # Clica se não tiver a marca de 'aplicado'
            if "fa-apply" not in (icon_class or ""):
                column_name = await item.locator("span").inner_text()
                print(f"A selecionar a coluna '{column_name}'...")
                await item.click()
                clicked_something = True
                await page.wait_for_timeout(250) # pequena pausa para estabilidade

        if clicked_something:
            print("A clicar no botão 'Apply' para confirmar as novas colunas.")
            apply_button = page.locator(apply_button_selector)
            if await apply_button.is_enabled():
                await apply_button.click()
                print("A aguardar que o menu se feche após aplicar...")
                await page.wait_for_selector(menu_selector, state="hidden", timeout=15000)
            else:
                print("Botão 'Apply' não estava ativo. A fechar o menu.")
                await page.keyboard.press("Escape")
        else:
            print("Nenhuma coluna nova para selecionar. Todas já estão visíveis.")
            await page.keyboard.press("Escape")
        
        # Aguarda que a tabela recarregue após as alterações
        loading_selector = f"{TABLE_CONTAINER_SELECTOR} .fa-loading"
        print("A aguardar que a tabela recarregue com as novas colunas...")
        try:
            await page.wait_for_selector(loading_selector, state='visible', timeout=2000)
            await page.wait_for_selector(loading_selector, state='hidden', timeout=30000)
            print("Indicador de carregamento concluído.")
        except TimeoutError:
            print("Nenhum indicador de carregamento detetado, a continuar.")
        
        print("--- Visibilidade das colunas configurada ---")

    except Exception as e:
        print(f"ERRO ao configurar visibilidade das colunas: {e}")
        print("A continuar o script com as colunas atuais...")

async def apply_filter(page: Page, column_name_to_filter: str, filter_value: str):
    """
    Aplica um filtro a uma coluna específica da tabela de forma dinâmica.
    """
    print(f"--- A aplicar filtro na coluna '{column_name_to_filter}' com o valor '{filter_value}' ---")

    # Primeiro, obtemos o mapeamento de colunas ID -> Nome
    visible_columns = await get_visible_columns(page)
    if not visible_columns:
        print("ERRO: Não foi possível obter as colunas visíveis para aplicar o filtro.")
        return

    # Invertemos o dicionário para encontrar o ID a partir do nome
    columns_by_name = {name: col_id for col_id, name in visible_columns.items()}
    target_column_id = columns_by_name.get(column_name_to_filter)

    if not target_column_id:
        print(f"ERRO: A coluna '{column_name_to_filter}' não foi encontrada. O filtro não será aplicado.")
        print(f"Colunas disponíveis: {list(columns_by_name.keys())}")
        return

    try:
        # Construímos o seletor do ícone de filtro dinamicamente
        filter_icon_selector = f'div.header-cell[data-column-id="{target_column_id}"] button.column-settings'
        
        print(f"A clicar no ícone de filtro com o seletor: {filter_icon_selector}")
        await page.click(filter_icon_selector)

        # O resto do fluxo de filtro é genérico e reutilizável
        print(f"A aguardar pelo campo de input do filtro: '{FILTER_INPUT_SELECTOR}'")
        await page.wait_for_selector(FILTER_INPUT_SELECTOR, state="visible", timeout=10000)
        
        print(f"A preencher o filtro com o valor: '{filter_value}'")
        await page.fill(FILTER_INPUT_SELECTOR, filter_value)
        
        print(f"A clicar no botão 'Apply' do filtro: '{FILTER_APPLY_BUTTON_SELECTOR}'")
        await page.click(FILTER_APPLY_BUTTON_SELECTOR)

        print("A aguardar que o painel de filtro se feche...")
        await page.wait_for_selector(FILTER_INPUT_SELECTOR, state="hidden", timeout=15000)
        
        loading_selector = f"{TABLE_CONTAINER_SELECTOR} .fa-loading"
        print(f"A aguardar que o indicador de carregamento ('{loading_selector}') desapareça...")
        try:
            await page.wait_for_selector(loading_selector, state='visible', timeout=5000)
            await page.wait_for_selector(loading_selector, state='hidden', timeout=30000)
        except TimeoutError:
            print("Indicador de carregamento não apareceu (ou foi rápido demais).")
        
        print("--- Filtro aplicado com sucesso ---")

    except Exception as e:
        print(f"ERRO inesperado ao aplicar o filtro: {e}")

async def extract_data_with_virtual_scroll(page: Page, columns_to_extract: dict) -> pd.DataFrame:
    """
    Localiza a tabela, faz scroll programaticamente para carregar todos os dados 
    devido ao "virtual scrolling", e extrai a informação de forma estruturada.
    """
    print("--- A iniciar extração de dados com gestão de scroll virtual ---")
    
    try:
        scroll_container = page.locator(SCROLL_CONTAINER_SELECTOR)
        await scroll_container.wait_for(state="visible", timeout=15000)
        print(f"Contentor de scroll encontrado: '{SCROLL_CONTAINER_SELECTOR}'")
    except TimeoutError:
        print(f"ERRO: Não foi possível encontrar o contentor da tabela com o seletor '{SCROLL_CONTAINER_SELECTOR}'.")
        return pd.DataFrame()

    all_rows_data = []
    processed_row_ids = set()
    last_seen_switch = "N/A"
    
    # Usa as colunas detetadas dinamicamente
    column_headers = list(columns_to_extract.values())
    column_headers.insert(0, "Switch Name") # Adicionar a nossa coluna personalizada

    last_scroll_top = -1
    while True:
        # Encontra todas as "linhas" visíveis (tanto secções como linhas de dados)
        visible_rows = page.locator(f"{SECTION_ROW_SELECTOR}, {DATA_ROW_SELECTOR}")
        
        for i in range(await visible_rows.count()):
            row = visible_rows.nth(i)
            
            # Verifica se é uma linha de secção (cabeçalho do switch)
            is_section = "section" in (await row.get_attribute("class") or "")
            if is_section:
                section_id = await row.get_attribute("section-id")
                if section_id:
                    last_seen_switch = section_id.strip()
                continue # Pula para a próxima linha visível

            # Se chegámos aqui, é uma linha de dados
            row_id = await row.get_attribute("row-id")
            if not row_id or row_id in processed_row_ids:
                continue # Ignora se não tiver ID ou se já foi processada

            processed_row_ids.add(row_id)
            
            # Extrai todas as células desta linha
            row_data = {"Switch Name": last_seen_switch}
            cells = row.locator("div.row-cell")
            
            for j in range(await cells.count()):
                cell = cells.nth(j)
                column_id = await cell.get_attribute("column-id")
                
                if column_id in columns_to_extract:
                    column_name = columns_to_extract[column_id]
                    
                    # Lógica de extração robusta para lidar com múltiplos formatos de célula.
                    formatted_content = cell.locator("span.select-formatted-content").first
                    standard_content = cell.locator("div.standard-value-content").first
                    cell_content = cell.locator("div.row-cell-content").first
                    
                    cell_text = ""
                    if await formatted_content.count() > 0:
                        # Prioridade para conteúdo formatado (ex: Port com ícone)
                        cell_text = await formatted_content.inner_text()
                    elif await standard_content.count() > 0:
                        # Caso geral para a maioria dos campos
                        cell_text = await standard_content.inner_text()
                    elif await cell_content.count() > 0:
                        # Fallback para conteúdo direto na célula (ex: Bytes)
                        cell_text = await cell_content.inner_text()

                    row_data[column_name] = cell_text.strip().replace('\n', ' ') # Limpa e remove quebras de linha
            
            all_rows_data.append(row_data)

        print(f"Encontradas {len(all_rows_data)} linhas de dados até agora. A tentar fazer scroll...")
        
        # Lógica de scroll: Executa JS para fazer scroll dentro do contentor
        current_scroll_top = await scroll_container.evaluate('el => el.scrollTop')
        await scroll_container.evaluate('el => { el.scrollTop += el.clientHeight; }')
        
        # Espera um pouco para o conteúdo novo carregar
        await page.wait_for_timeout(1000) 
        
        new_scroll_top = await scroll_container.evaluate('el => el.scrollTop')

        # Condição de paragem: se o scroll não se moveu, chegámos ao fim.
        if new_scroll_top == current_scroll_top:
            print("Scroll chegou ao fim. Extração de dados concluída.")
            break
            
    if not all_rows_data:
        print("⚠️ Não foram encontrados dados para guardar (após o processo de scroll).")
        return pd.DataFrame()

    # Cria o DataFrame com as colunas na ordem definida
    df = pd.DataFrame(all_rows_data, columns=column_headers)
    return df

async def capture_table_html(page: Page):
    """
    Função de diagnóstico para fazer scroll na tabela e capturar o seu HTML final.
    """
    print("A iniciar a captura de diagnóstico do HTML da tabela...")

    rows_selector = f'{TABLE_CONTAINER_SELECTOR} >> .row'
    
    # Faz scroll até ao fim para garantir que todos os elementos são carregados
    while True:
        rows = page.locator(rows_selector)
        count = await rows.count()
        if count == 0:
            print("Nenhuma linha encontrada para iniciar o scroll.")
            break
            
        last_row = rows.nth(count - 1)
        last_row_html = await last_row.inner_html()
        
        await last_row.scroll_into_view_if_needed()
        await page.wait_for_timeout(1000)
        
        # Verifica se a última linha mudou. Se não, chegámos ao fim.
        new_last_row_html = await page.locator(rows_selector).nth(count - 1).inner_html()
        if last_row_html == new_last_row_html:
            print("Scroll chegou ao fim. A tabela está totalmente carregada.")
            break
            
    # Extrai o HTML completo do contentor da tabela
    table_container = page.locator(TABLE_CONTAINER_SELECTOR)
    if await table_container.count() > 0:
        table_html = await table_container.inner_html()
        filename = "debug_table_snapshot.html"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(table_html)
        print(f"✅ Snapshot do HTML da tabela guardado com sucesso no ficheiro '{filename}'")
    else:
        print("⚠️ Não foi possível encontrar o contentor da tabela para extrair o HTML.")

async def main():
    """
    Função principal que executa o processo de web scraping.
    """
    if not all([FORTIGATE_URL, USERNAME, PASSWORD]):
        print("ERRO: Uma ou mais variáveis de ambiente (FORTIGATE_URL, USERNAME, PASSWORD) não estão definidas.")
        print("Por favor, crie um ficheiro .env e defina-as conforme as instruções no topo do scraper.py")
        return

    print("--- Início do Script de Scraping da FortiGate ---")
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=["--ignore-certificate-errors"])
        context = None
        page = None
        
        try:
            if os.path.exists(AUTH_FILE):
                print(f"Ficheiro de autenticação '{AUTH_FILE}' encontrado. A tentar reutilizar sessão.")
                context = await browser.new_context(storage_state=AUTH_FILE, ignore_https_errors=True)
                page = await context.new_page()
                
                ports_url = f"{FORTIGATE_URL}/ng/switchctrl/ports"
                print(f"A navegar diretamente para a página de portas para validar a sessão: {ports_url}")
                await page.goto(ports_url, timeout=60000, wait_until="domcontentloaded")
                
                try:
                    await page.wait_for_selector(USER_SELECTOR, state="visible", timeout=5000)
                    print("Sessão inválida ou expirada. A efetuar novo login.")
                    await context.close()
                    
                    context = await browser.new_context(ignore_https_errors=True)
                    page = await context.new_page()
                    await login_and_navigate(page)
                    await context.storage_state(path=AUTH_FILE)
                    print(f"Nova sessão de autenticação guardada em '{AUTH_FILE}'.")
                except TimeoutError:
                    print("Sessão reutilizada com sucesso.")
            else:
                print(f"Nenhum ficheiro de autenticação encontrado. A efetuar login completo.")
                context = await browser.new_context(ignore_https_errors=True)
                page = await context.new_page()
                await login_and_navigate(page)
                await context.storage_state(path=AUTH_FILE)
                print(f"Sessão de autenticação guardada em '{AUTH_FILE}'.")
            
            # --- FLUXO AUTOMATIZADO COMPLETO ---
            
            # 1. Tornar todas as colunas visíveis
            await set_all_columns_visible(page)
            
            # 2. Aplicar zoom 
            print("A aplicar zoom de 22% na página.")
            await page.evaluate("document.body.style.zoom = 0.22")
            
            # 3. Fazer refresh à página para consolidar as alterações
            print("A fazer refresh da página para consolidar as alterações.")
            await page.reload(wait_until="domcontentloaded")
            
            # 4. Reaplicar o zoom após o refresh
            print("A reaplicar o zoom de 22% após o refresh.")
            await page.evaluate("document.body.style.zoom = 0.22")
            await page.wait_for_timeout(1000) # Pausa para renderização
            
            # 5. Detetar as colunas visíveis dinamicamente
            columns_to_extract = await get_visible_columns(page)
            if not columns_to_extract:
                print("ERRO CRÍTICO: Não foi possível detetar as colunas da tabela. A abortar.")
                return
            
            # 6. Aplicar Filtro (se configurado)
            if FILTER_COLUMN_NAME and FILTER_VALUE:
                await apply_filter(page, FILTER_COLUMN_NAME, FILTER_VALUE)
            else:
                print("Nenhum filtro configurado, a extrair todos os dados da tabela.")
            
            # 7. Extrair os Dados
            print("\n▶️ A iniciar a extração de dados...")
            df = await extract_data_with_virtual_scroll(page, columns_to_extract)
            
            # 8. Guardar os Dados
            if not df.empty:
                output_dir = "outputs"
                os.makedirs(output_dir, exist_ok=True)
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                filename = os.path.join(output_dir, f"fortiswitch_ports_{timestamp}.csv")
                df.to_csv(filename, index=False, encoding='utf-8-sig')
                print(f"✅ Sucesso! Encontradas {len(df)} linhas de dados.")
                print(f"Dados guardados com sucesso no ficheiro: '{filename}'")
            else:
                print("Script concluído, mas não foram extraídos dados.")

        except TimeoutError as e:
            print(f"\nERRO: O tempo de espera por um elemento expirou. {e}")
            print("Isto pode acontecer se a página demorar muito a carregar ou se um seletor estiver incorreto.")
            if 'page' in locals() and page and not page.is_closed():
                filename = f"error_screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                await page.screenshot(path=filename)
                print(f"Foi guardado um screenshot do erro em: '{filename}'")
        except Exception as e:
            print(f"\nERRO INESPERADO: {e}")
            if 'page' in locals() and page and not page.is_closed():
                filename = f"error_screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                await page.screenshot(path=filename)
                print(f"Foi guardado um screenshot do erro em: '{filename}'")
        finally:
            if 'browser' in locals() and browser:
                await browser.close()
                print("\nBrowser fechado.")
            print("--- Fim do Script ---")

if __name__ == "__main__":
    asyncio.run(main()) 