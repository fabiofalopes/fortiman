# Análise e Visualização de Portas FortiSwitch

Este conjunto de scripts extrai, processa e visualiza dados de portas de FortiSwitch a partir da interface web de um FortiGate.

## Pipeline de Execução

### 1. Instalar Dependências
```bash
# Navegue para a pasta dos scripts
cd scripts/network_visualization

# Instale os pacotes necessários
pip install -r requirements.txt
playwright install
```

### 2. Configurar Credenciais
Crie um ficheiro `.env` na raiz do projeto (`fortiman/.env`):
```dotenv
FORTIGATE_URL="https://192.168.1.99"
USERNAME="your_username"
PASSWORD="your_password"
```

### 3. Executar os Scripts em Ordem

```bash
# Passo 1: Extrair dados do FortiGate
python fortiswitch_ports_scraper.py

# Passo 2: Processar o ficheiro CSV (substitua pelo nome do seu ficheiro)
python process_switch_data.py ../../outputs/fortiswitch_ports_2025-01-20_15-30-45.csv

# Passo 3: Gerar a visualização da topologia (opcional)
python visualize_network.py ../../outputs/fortiswitch_ports_2025-01-20_15-30-45
```

### 4. Ficheiros Gerados

Após a execução, encontrará os seguintes ficheiros numa pasta dentro de `outputs/`:

```
outputs/fortiswitch_ports_YYYY-MM-DD_HH-MM-SS/
├── processed_fortiswitch_ports_...xlsx    # Relatório Excel
├── links_for_vis_fortiswitch_ports_...csv # Dados de ligações de rede
├── nodes_for_vis_fortiswitch_ports_...csv # Dados de nós de rede
├── network_topology_fortiswitch_ports_...png # Diagrama de rede (PNG)
├── network_topology_fortiswitch_ports_...svg # Diagrama de rede (SVG)
└── network_topology_fortiswitch_ports_...mmd # Código fonte do diagrama (Mermaid)
```

## Descrição dos Scripts

### `fortiswitch_ports_scraper.py`
- Faz login automático no FortiGate.
- Navega para a página FortiSwitch Ports.
- Extrai todos os dados da tabela, lidando com *virtual scrolling*.
- Guarda os dados num ficheiro CSV com timestamp na pasta `outputs`.

### `process_switch_data.py`
- Lê o CSV gerado e cria um relatório Excel.
- Agrupa as portas por switch e prioriza os *core switches*.
- Gera ficheiros auxiliares (nós e ligações) para a visualização.

### `visualize_network.py`
- Cria diagramas visuais da topologia de rede.
- Filtra para mostrar apenas switches de *core* e distribuição.
- Gera múltiplos formatos (PNG, SVG, Mermaid).

## Nota de Segurança

O ficheiro `.env` contém credenciais sensíveis e nunca deve ser partilhado ou versionado. Ele já se encontra no `.gitignore`. 