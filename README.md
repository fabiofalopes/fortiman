# FortiMan

## Estrutura do Repositório

O projeto está organizado nas seguintes pastas principais:

-   `docs/`: Contém documentação oficial e notas de release para produtos Fortinet. É um recurso valioso para consulta técnica.
-   `scripts/`: Scripts Python para automatizar tarefas de análise e visualização. Cada subpasta contém um `README.md` específico com instruções de uso.
    -   `log_analysis/`: Ferramentas para análise de logs.
    -   `network_visualization/`: Scripts para extrair, processar e visualizar a topologia de rede a partir de um FortiGate.
-   `reports/`: Relatórios de análise, guias de configuração e outros artefactos gerados pelos scripts ou por análises manuais.
-   `prompts/`: Coleção de prompts e planos usados para desenvolvimento e automação com IA.

## Como Começar

### 1. Configuração do Ambiente Virtual

Recomenda-se o uso de um ambiente virtual (`venv`) para gerir as dependências do projeto de forma isolada. Este projeto foi desenvolvido e testado com Python 3.11.

```bash
# Crie o ambiente virtual na raiz do projeto
python3.11 -m venv venv

# Ative o ambiente virtual
# No macOS/Linux:
source venv/bin/activate
# No Windows:
# venv\\Scripts\\activate
```

### 2. Utilização dos Scripts

Com o ambiente virtual ativo, navegue até à pasta do script que pretende utilizar e siga as instruções no `README.md` correspondente para instalar as suas dependências e executá-lo.

Por exemplo, para os scripts de visualização de rede:
```bash
cd scripts/network_visualization
pip install -r requirements.txt
```

## Contribuições

Contribuições são bem-vindas. Se tiver um novo script, documentação relevante ou uma melhoria, sinta-se à vontade para abrir uma *Pull Request*. 