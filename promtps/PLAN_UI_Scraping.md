# Plano de Extração de Dados via UI (Web Scraping)

Este documento detalha o plano para extrair dados da interface web da FortiGate, que evoluiu de um processo manual para um script totalmente automatizado.

---

### Fase 1: Investigação e Automação (Concluído)

**Objetivo:** Desenvolver um script Python (`scraper-auto.py`) capaz de extrair de forma autónoma e robusta os dados da tabela "FortiSwitch Ports".

**Desafios e Soluções Implementadas:**

1.  **Login e Gestão de Sessão:**
    *   O script utiliza credenciais de um ficheiro `.env` para segurança.
    *   Guarda e reutiliza o estado da sessão (`auth_state.json`) para acelerar execuções futuras e aumentar a estabilidade.

2.  **Visibilidade das Colunas:**
    *   **Problema:** A UI da FortiGate não renderiza colunas que não estão visíveis no ecrã (seja por estarem desativadas ou por scroll horizontal).
    *   **Solução:** O script agora automatiza este processo:
        *   Clica com o botão direito do rato no cabeçalho da tabela para abrir o menu de seleção de colunas.
        *   Analisa o menu e clica em todas as colunas que ainda não estão selecionadas.
        *   Aplica as alterações para garantir que *todas* as colunas estão presentes no DOM para extração.

3.  **Scroll Horizontal e Zoom:**
    *   **Problema:** Mesmo com as colunas ativas, a largura do browser podia fazer com que não fossem renderizadas.
    *   **Solução:** O script aplica programaticamente um "zoom out" (para 22%) na página. Isto força a UI a renderizar todas as colunas ativas numa única vista, eliminando a necessidade de scroll horizontal.

4.  **Scroll Vertical e Dados Dinâmicos:**
    *   **Problema:** A tabela utiliza "virtual scrolling", carregando apenas as linhas visíveis.
    *   **Solução:** O script localiza o contentor da tabela e faz scroll programaticamente até ao fim, garantindo que todas as linhas de dados são carregadas e extraídas.

### Fase 2: Execução do Script (`scraper-auto.py`)

**Como Funciona:**

1.  **Configuração:** As credenciais e o URL devem estar no ficheiro `.env`.
2.  **Execução:** O script é executado com `python scraper-auto.py`.
3.  **Processo Autónomo:**
    *   Faz login (ou reutiliza uma sessão).
    *   Navega para a página "FortiSwitch Ports".
    *   Ativa todas as colunas disponíveis no menu de contexto.
    *   Deteta dinamicamente os nomes e IDs de todas as colunas visíveis.
    *   Aplica zoom e faz refresh à página para renderizar tudo.
    *   Aplica o filtro para `_sw` na VLAN nativa.
    *   Percorre a tabela completa com scroll vertical.
    *   Extrai os dados de cada célula usando uma lógica de extração robusta que se adapta a diferentes formatos de conteúdo.
4.  **Resultado:** Um ficheiro CSV com um timestamp (ex: `fortiswitch_ports_YYYY-MM-DD_HH-MM-SS.csv`) é gerado no diretório, contendo a tabela completa e todas as colunas disponíveis. 