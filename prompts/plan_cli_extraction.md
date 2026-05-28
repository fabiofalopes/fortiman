# Plano de Extração de Dados via CLI

Este documento descreve o plano de investigação para determinar a viabilidade da extração de informações da FortiGate através da sua Command-Line Interface (CLI).

**Objetivo:** Descobrir se os mesmos dados disponíveis na UI (especificamente, a lista de portas de switch com os seus status, velocidade, VLANs, etc.) podem ser obtidos através de comandos na CLI e qual o formato desses dados.

**Pressupostos:**
*   Existe acesso SSH à FortiGate.
*   As credenciais de utilizador têm permissões de leitura (`read-only`) ou equivalentes para os comandos necessários. Não executaremos quaisquer comandos de configuração (`config`).

---

### Fase 1: Investigação e Exploração da CLI

**Objetivo:** Tentar executar comandos na CLI para encontrar a informação desejada.

**Ferramenta:** Um cliente SSH (como o Terminal do macOS/Linux ou PuTTY no Windows).

**Passos de Investigação a Tentar:**

1.  **Conectar via SSH:**
    ```bash
    ssh <seu_utilizador>@<ip_da_fortigate>
    ```

2.  **Verificar Comandos de Switch:**
    Uma vez dentro da CLI da FortiGate, o sistema de comandos é hierárquico. O foco é encontrar os comandos relacionados com o `switch-controller`.

    *   Comece por explorar os comandos disponíveis. O `?` ou a tecla `Tab` são geralmente úteis para autocompletar e listar opções.

    *   **Comandos Sugeridos para Experimentar:**
        ```
        # Entrar no contexto de configuração dos switches geridos
        config switch-controller managed-switch
        
        # Listar os switches geridos
        show 
        
        # Sair do contexto de configuração
        end
        ```

        ```
        # Usar comandos de diagnóstico (geralmente seguros e não alteram a configuração)
        # Estes comandos devem ser executados a partir do prompt principal (root) da CLI, não dentro de um contexto de configuração (e.g., (managed-switch) $)
        
        # Listar o estado das portas de um switch específico (substitua <FGT_serial> pelo S/N do switch)
        diagnose switch-controller get-conn-status
        
        # Outro comando de diagnóstico que pode mostrar informação detalhada das portas
        diagnose switch-controller dump port-stats <switch-id>
        
        # Listar as VLANs
        diagnose switch-controller list-vlans <switch-id>
        ```
        
    *   **Comandos `get`:**
        Os comandos `get` são para visualização e são seguros.
        ```
        get switch-controller managed-switch
        ```

3.  **Analisar o Output:**
    *   Para cada comando que executar, observe o formato da saída. É texto simples? Está estruturado em tabelas? É semelhante a JSON?
    *   A informação que procura (Nome da Porta, Estado, Velocidade de Negociação, Native VLAN) está presente?
    *   Copie e cole exemplos do output dos comandos mais promissores para este documento.

    **Nota:** A execução de comandos e a extração de dados podem ser desafiadoras quando a CLI é acedida via UI, devido à dificuldade em copiar o output de forma programática ou consistente. Para uma extração mais eficaz, o acesso direto via SSH é preferível.

---

### Fase 2: Avaliação de Viabilidade

**Objetivo:** Com base nos resultados da Fase 1, decidir se a extração via CLI é uma abordagem viável.

**Questões a Responder:**

1.  **A informação necessária está disponível?** Conseguimos obter todos os campos que temos na UI?
2.  **O output é consistente e "parseable"?** É suficientemente estruturado para que um script o consiga ler de forma fiável?
3.  **As permissões são suficientes?** A sua conta de utilizador consegue executar os comandos de `diagnose` e `get` necessários?

---

### Fase 3: Desenvolvimento do Script (Se Viável)

Se a abordagem CLI for promissora, podemos desenvolver um script Python usando bibliotecas como `netmiko` ou `paramiko`, que são especializadas em conectar-se a dispositivos de rede via SSH e executar comandos.

**Apenas avançaremos para esta fase se a Fase 2 concluir que a abordagem é viável e vantajosa em relação ao web scraping.** 