# FortiMan: Ferramenta de Análise de Portas FortiSwitch

Este projeto fornece um pipeline completo para extrair, processar e analisar dados da tabela "FortiSwitch Ports" a partir da interface web de um FortiGate. O processo está dividido em duas fases principais:

1.  **Extração**: Um script de scraping (`fortiswitch_ports_scraper.py`) acede ao FortiGate, extrai todos os dados das portas e guarda-os num ficheiro CSV.
2.  **Processamento**: Um segundo script (`process_switch_data.py`) pega nesse ficheiro CSV e transforma-o num relatório Excel (`.xlsx`), agrupando as portas por switch para facilitar a análise.

## Funcionalidades Principais

### Script de Extração (`fortiswitch_ports_scraper.py`)

- **Automação Completa:** Faz o login, navega até à página correta, e extrai os dados sem qualquer intervenção manual.
- **Visibilidade Automática de Colunas:** Deteta e ativa programaticamente todas as colunas da tabela que estejam desativadas por defeito na UI.
- **Extração Robusta:** Lida com o scroll virtual, percorrendo toda a tabela para garantir que nenhuma linha de dados é perdida.
- **Saída Estruturada:** Guarda os dados extraídos num ficheiro CSV dentro da pasta `outputs/`, com um timestamp para fácil identificação.

### Script de Processamento (`process_switch_data.py`)

- **Organização por Switch**: Lê o ficheiro CSV e cria um relatório em Excel.
- **Estrutura de Mini-Tabelas**: No ficheiro Excel, cada switch tem a sua própria tabela, facilitando a visualização.
- **Priorização de Switches Core**: As tabelas de switches que contêm "core" no nome são apresentadas no topo do relatório.
- **Nomenclatura Clara**: O ficheiro final é guardado como `outputs/processed_<nome_do_ficheiro_original>.xlsx`.

## Como Usar

### 1. Pré-requisitos

- Python 3.8+
- Acesso a um FortiGate com um utilizador que tenha permissões para ver a página "FortiSwitch Ports".

### 2. Instalação

Clone o repositório e instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

O Playwright também necessita de instalar os browsers que utiliza. Execute o seguinte comando para os instalar:

```bash
playwright install
```

### 3. Configuração de Credenciais

Crie um ficheiro chamado `.env` na raiz do projeto. Este ficheiro **não deve ser partilhado** ou enviado para repositórios de código (já está incluído no `.gitignore`). Adicione as suas credenciais e o URL do FortiGate a este ficheiro:

```dotenv
# .env
FORTIGATE_URL="https://192.168.1.99"
USERNAME="seu_utilizador"
PASSWORD="sua_password_super_secreta"
```

### 4. Execução do Pipeline

O processo é executado em dois passos:

**Passo 1: Extrair os dados do FortiGate**

Execute o script de scraping. Ele irá gerar um ficheiro CSV na pasta `outputs/`.

```bash
python fortiswitch_ports_scraper.py
```

**Passo 2: Processar o ficheiro CSV**

Execute o script de processamento, passando o caminho do ficheiro CSV gerado no passo anterior como argumento.

```bash
# Substitua 'caminho/para/o/seu/ficheiro.csv' pelo nome do ficheiro real
python process_switch_data.py outputs/fortiswitch_ports_2025-06-20_21-56-38.csv
```

Após a execução, encontrará o relatório final em formato Excel (`.xlsx`) na pasta `outputs/`, pronto para análise. 