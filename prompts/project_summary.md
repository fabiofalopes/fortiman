# Resumo do Projeto: Extração de Dados da UI FortiGate

Este documento serve como um registo cronológico do processo de desenvolvimento e depuração para criar um script de web scraping para a interface da FortiGate. O objetivo era extrair os dados da tabela "FortiSwitch Ports".

## Fase 1: Análise Inicial e Recolha de Informação

- **Objetivo:** Identificar os seletores CSS necessários para a automação.
- **Ferramentas:** `PLAN_UI_Scraping.md` como guia, Ferramentas de Programador do Chrome.
- **Descobertas:**
    - Seletores de login foram facilmente identificados: `#username`, `#secretkey`, `#login_button`.
    - A navegação para a página correta foi resolvida procurando pelo texto "FortiSwitch Ports".
    - A análise do HTML da tabela (guardado em `table_structure.html`) revelou uma estrutura moderna e complexa, baseada em `divs` em vez de uma `<table>` tradicional. Isto indicou que a extração não seria trivial.

## Fase 2: Desenvolvimento do Script Inicial

- **Ações:**
    - Criado `requirements.txt` com `playwright` e `pandas`.
    - Desenvolvido um script inicial, capaz de fazer login, navegar e aplicar um filtro.
    - Implementadas melhorias de segurança e robustez:
        - Uso da biblioteca `python-dotenv` para gerir credenciais num ficheiro `.env`.
        - Criação de um ficheiro `.gitignore` para proteger dados sensíveis.
        - Adição de logging e blocos `try-except` para capturar erros e guardar screenshots.

## Fase 3: Depuração do Problema "0 Resultados"

- **Problema:** O script executava todos os passos com sucesso (login, navegação, filtro), mas consistentemente reportava "0 linhas de dados encontradas".
- **Investigação e Soluções Tentadas:**
    1.  **Gestão de Sessão:** Implementado um sistema para guardar e reutilizar o estado de autenticação (`auth_state.json`) para evitar logins repetidos e possíveis problemas de sessão. **Isto funcionou**, mas não resolveu a extração de dados.
    2.  **Race Condition:** Suspeitámos que o script tentava ler os dados antes de a UI os renderizar após o filtro. Foram adicionadas esperas explícitas para o desaparecimento de indicadores de carregamento. O problema persistiu.
    3.  **Virtual Scrolling:** Ao executar em modo não-headless (`headless=False`), observámos que os dados **apareciam no ecrã**, mas o script não os capturava. A hipótese tornou-se "Virtual Scrolling", onde a UI só renderiza as linhas visíveis no ecrã. Implementámos uma lógica de "scroll e scrape" para percorrer a tabela programaticamente. **Ainda assim, o problema persistiu.**

## Fase 4: A Descoberta Crucial - Visibilidade das Colunas

- **Ponto de Viragem:** Através do modo de depuração interativo (`page.pause()`), o utilizador fez a descoberta fundamental. O problema não era apenas o scroll vertical, mas a visibilidade das colunas em si.
- **As Duas Causas Raiz:**
    1.  **Colunas Desativadas por Defeito:** A configuração padrão da UI da FortiGate não exibe todas as colunas disponíveis (ex: "Description"). Se uma coluna não está ativa na UI, ela **não existe no HTML da página**, tornando impossível a sua extração.
    2.  **Colunas Fora do Viewport (Scroll Horizontal):** Mesmo que uma coluna esteja ativada, se a janela do browser não for suficientemente larga, a UI pode não renderizar as colunas mais à direita para otimizar o desempenho. O nosso scroll vertical não resolvia este "scroll horizontal".

## Fase 5: A Solução Híbrida e o Sucesso

- **A Estratégia Vencedora:** Combinar a intervenção manual do utilizador com uma automação mais inteligente.
    1.  **Pausa Estratégica:** O script é pausado (`page.pause()`) após o login e a navegação.
    2.  **Intervenção Manual (Utilizador):** Durante a pausa, o utilizador:
        - Clica com o botão direito no cabeçalho da tabela para **ativar todas as colunas desejadas**.
        - Faz **"zoom out"** no browser (ex: para 80%). Isto força a UI a renderizar todas as colunas ativadas numa única vista, resolvendo o problema do scroll horizontal.
    3.  **Continuação da Automação (Script):** Após o utilizador retomar o script:
        - A lógica de **scroll vertical** percorre todas as linhas da tabela.
        - A extração funciona porque agora **todas as células e colunas desejadas estão presentes no DOM e são visíveis** para o Playwright.

- **Resultado:** Esta abordagem híbrida resultou na extração bem-sucedida de todas as 115 linhas de dados, incluindo as colunas que antes vinham vazias (`Negotiated Speed`, `Description`), como se pode ver no ficheiro `fortiswitch_ports_2025-06-20_19-52-09.csv`.

## Estado Atual e Próximos Passos (Consolidação)

- **Situação:** Temos um processo funcional, mas que depende de passos manuais e código de depuração.
- **Objetivo Final:** Refinar o script para ser uma ferramenta robusta e limpa.
- **Automatizar o Zoom:** O script deve aplicar o "zoom out" programaticamente após a pausa.
- **Leitura Dinâmica de Cabeçalhos:** O script deve deixar de usar uma lista de colunas pré-definida. Em vez disso, deve ler os cabeçalhos que estão visíveis na tabela *após* a configuração manual do utilizador e usar essa lista para construir o CSV. Isto torna o script flexível e adaptável a qualquer configuração de colunas.
- **Organização:** Criar um diretório `output/` para os resultados.
- **Limpeza:** Remover todos os ficheiros de depuração e artefactos do projeto.

## Fase 6: A Descoberta Final e a Automação Completa

- **Problema Persistente:** Embora a abordagem híbrida funcionasse, a tentativa de automatizar a ativação das colunas falhava consistentemente. O script não conseguia encontrar o seletor do cabeçalho da tabela para clicar com o botão direito, mesmo após várias tentativas com seletores mais robustos.

- **Ponto de Viragem Analítico:** A decisão foi tomada para analisar o DOM completo da página. O HTML da página inteira foi guardado no ficheiro `full.html`. A análise deste ficheiro massivo revelou a estrutura que estava a escapar às ferramentas de inspeção do browser em tempo real. O seletor correto para o cabeçalho não era `div.table-header-container`, mas sim `div.fixed-header-container`.

- **A Solução Definitiva:**
    1.  **Reimplementação da Lógica:** Foi criada a função `set_all_columns_visible` no script, desta vez usando o seletor `div.fixed-header-container div.header-cell[data-column-id="port-name"]` que foi validado contra o `full.html`.
    2.  **Fluxo Totalmente Autónomo:** A lógica do script foi reordenada para seguir um processo infalível:
        *   Fazer login e navegar para a página correta.
        *   Chamar a função `set_all_columns_visible` para detetar e ativar programaticamente todas as colunas desativadas.
        *   Aplicar um zoom de 22% para garantir que todas as colunas ativadas são renderizadas no DOM.
        *   Fazer um `refresh` à página para consolidar as alterações de visibilidade e zoom.
        *   Aplicar o filtro desejado na tabela.
        *   Percorrer a tabela com a lógica de scroll virtual para extrair os dados.

- **Resultado Final:** O processo resultou num script (`fortiswitch_ports_scraper.py`) 100% automatizado, robusto e que não depende de estados de sessão pré-configurados ou de qualquer intervenção manual. Consegue consistentemente extrair a totalidade dos dados.

## Fase 7: Refinamento Final e Extração Universal de Células

- **O Último Detalhe:** Após alcançar a automação completa, foi notado que, embora todas as colunas fossem lidas, algumas (como "Port") apareciam vazias no CSV final.
- **Análise Final:** Uma nova inspeção do `full.html` revelou que a formatação do conteúdo dentro das células da tabela não era uniforme.
    - Algumas células usavam a classe `div.standard-value-content`.
    - A coluna "Port" usava `span.select-formatted-content` para incluir ícones de estado.
    - Outras células tinham o texto diretamente dentro de `div.row-cell-content`.
- **Solução de Extração Robusta:** A lógica de extração de dados na função `extract_data_with_virtual_scroll` foi substituída por um mecanismo de "fallback" inteligente:
    1.  O script tenta primeiro extrair texto do seletor mais específico (`span.select-formatted-content`).
    2.  Se falhar, tenta o seletor padrão (`div.standard-value-content`).
    3.  Como último recurso, lê o conteúdo da célula principal (`div.row-cell-content`).
- **Resultado Definitivo:** Esta alteração final resultou num script que não só automatiza a visibilidade e leitura das colunas, mas também extrai de forma fiável o conteúdo de *cada* célula, independentemente da sua formatação interna.

## Fase 8: Generalização do Mecanismo de Filtro

- **A Última Fronteira da Flexibilidade:** O script era robusto, mas o filtro ainda estava "hardcoded" (fixo no código) para a coluna "Native VLAN".
- **Objetivo:** Permitir que o utilizador final pudesse filtrar qualquer coluna por qualquer valor, sem ter de alterar a lógica do script.
- **Solução Dinâmica:**
    1.  **Variáveis de Configuração:** Foram criadas duas variáveis no topo do ficheiro, `FILTER_COLUMN_NAME` e `FILTER_VALUE`, para permitir uma configuração fácil.
    2.  **Função de Filtro Genérica:** Foi desenvolvida uma nova função, `apply_filter`, que:
        *   Recebe o nome da coluna e o valor de filtro desejados.
        *   Utiliza a função `get_visible_columns` para obter o mapeamento dinâmico de nomes de colunas para os seus IDs internos (ex: "Native VLAN" -> "vlan").
        *   Constrói o seletor para o ícone de filtro da coluna-alvo de forma programática.
        *   Executa o processo de clicar, preencher o valor e aplicar o filtro.
    3.  **Integração Limpa:** O bloco de código de filtro fixo na função `main` foi substituído por uma simples chamada à nova função `apply_filter`, que é ativada apenas se as variáveis de configuração estiverem preenchidas.

## Fase 9: Limpeza e Organização Final do Projeto

- **Objetivo:** Finalizar o projeto, garantindo que a estrutura de ficheiros está limpa e o código é auto-explicativo.
- **Ações Realizadas:**
    1.  **Centralização dos Resultados:** O script foi modificado para guardar todos os ficheiros CSV gerados no diretório `outputs/`, criando-o automaticamente se não existir.
    2.  **Eliminação de Código Obsoleto:** O ficheiro `scraper.py` original, que já não era utilizado, foi eliminado.
    3.  **Renomeação do Script Principal:** O script `scraper-auto.py` foi renomeado para `fortiswitch_ports_scraper.py`, um nome mais descritivo e alinhado com as boas práticas.

## Conclusão Final

O projeto demonstrou com sucesso a capacidade de generalizar uma solução para um problema de web scraping complexo. Partindo da análise de um ficheiro HTML "insano e huge" (`full.html`), foi possível extrair a informação estrutural necessária para criar um processo automatizado e fiável, superando os desafios de UIs dinâmicas e complexas. O resultado é um script universal para esta tarefa, que se adapta autonomamente à estrutura da página, ao seu conteúdo e permite uma filtragem de dados totalmente flexível e configurável pelo utilizador.

