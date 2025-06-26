# Análise de Upgrade de Firmware: Core Switches FortiSwitch 1048E

**Data:** 21 de Junho de 2025
**Autor:** [O seu nome]
**Status:** Proposta para Análise

---

## 1. Resumo Executivo

Este documento analisa a viabilidade e os riscos de um upgrade de firmware para os dois switches core da infraestrutura, `DC-L_CORE-FIB01` e `DC-L_CORE-FIB02` (modelo `FortiSwitch 1048E`). A análise foi solicitada após instabilidade recorrente na rede, incluindo quebras de serviço, e a sugestão de avaliar um upgrade para a versão `7.6.0`.

A investigação, baseada nas release notes oficiais da Fortinet e em discussões da comunidade, resultou na seguinte conclusão:

**Recomendação Principal: NÃO fazer upgrade para a versão 7.6.x.** A versão `7.6.0` (e até a mais recente `7.6.2`) mantém um bug crítico (`940248`) que afeta especificamente o modelo `1048E`, causando a geração de pacotes duplicados e instabilidade.

**Ação Recomendada:**
1.  **Upgrade para FortiSwitchOS `7.4.7`:** Esta é a versão mais madura da linha `7.4.x`. Ela corrige bugs conhecidos de **alto consumo de CPU e de memória** que muito provavelmente estão a causar a instabilidade atual.
2.  **Implementar Workaround para o Bug `940248`:** Após o upgrade para `7.4.7`, aplicar uma alteração de configuração para mitigar o bug dos pacotes duplicados, desativando o "network device detection" nos switches.
3.  **Harden FortiLink:** Aplicar a configuração de `static-isl` para aumentar a estabilidade das ligações entre os switches.

Esta abordagem mitiga os problemas mais prováveis (CPU/memória) de forma segura, permanecendo numa linha de firmware estável e contornando o bug persistente do modelo `1048E`.

---

## 2. Contexto e Problemas Atuais

- **Equipamento:** 2x FortiSwitch 1048E (`DC-L_CORE-FIB01` e `DC-L_CORE-FIB02`)
- **Firmware Atual:** `FS1E48-v7.4.4-build0861`
- **Gestão:** FortiGate 1101E com FortiOS `7.4.5`
- **Sintomas Reportados:**
    - Breves mas recorrentes quebras de serviço na rede.
    - Relatos vagos de picos de CPU e/ou memória nos switches core.
    - Comportamento semelhante ao descrito na análise de logs anterior (`LOG_ANALYSIS_README.md`), como port flapping e instabilidade geral.

A nossa versão atual (`7.4.4`) está suscetível a vários bugs críticos que correspondem exatamente aos sintomas observados.

---

## 3. Análise dos Caminhos de Upgrade

### Caminho A: Manter a Versão Atual (`7.4.4`) - NÃO RECOMENDADO

- **Riscos:**
    - **Bug `955550`:** Comportamento inesperado que leva o **CPU a processar o tráfego que deveria ser tratado pelo NPU (hardware)**. Causa provável dos picos de CPU e perda de performance.
    - **Bug `1138333` (corrigido em 7.4.7):** Uso ineficiente de memória pelo daemon de configuração do FortiLink. Causa provável dos picos de memória.
    - **Bug `940248`:** Geração de pacotes duplicados no modelo `1048E`.
- **Conclusão:** Permanecer na versão atual mantém a infraestrutura exposta a bugs conhecidos e graves que são a causa mais provável da instabilidade da rede.

### Caminho B: Upgrade para a Versão Sugerida (`7.6.0`) - NÃO RECOMENDADO

- **Riscos:**
    - **Bug `940248` Persistente:** A análise das release notes da versão `7.6.0` e até da `7.6.2` confirma que o bug que causa **pacotes duplicados no modelo 1048E AINDA é um "Known Issue"**. Fazer o upgrade não resolve este problema fundamental.
    - **Risco de Nova Branch:** Versões `x.x.0` são as primeiras de uma nova linha de features, historicamente mais propensas a instabilidade e a bugs inesperados. Para switches core, a estabilidade é mais importante que novas funcionalidades.
    - **Bugs Adicionais:** A versão `7.6.0` introduz outros "known issues" relacionados com port flapping (`961142`).
- **Conclusão:** Este caminho é de alto risco. Não resolve um problema crítico específico do nosso hardware e introduz o risco de uma branch de firmware imatura.

### Caminho C: Upgrade para a Versão Madura (`7.4.7`) - RECOMENDADO

Esta é a abordagem mais segura e profissional. Foca-se em estabilidade em vez de novas features.

- **Benefícios:**
    - **Correção de Bug de CPU (`1077496`):** As release notes da linha `7.4.7` confirmam a resolução de um problema de **alto consumo de CPU** nos daemons do FortiLink.
    - **Correção de Bug de Memória (`1138333`):** As mesmas release notes confirmam a resolução de um problema de **eficiência de memória** no FortiLink.
    - **Maturidade:** `7.4.7` é uma versão "madura", focada em corrigir bugs da linha `7.4.x` em vez de adicionar novas funcionalidades de risco.

- **Riscos Residuais (e como mitigá-los):**
    - O bug `940248` (pacotes duplicados no `1048E`) ainda existe.
    - **Mitigação:** A descrição do bug indica que ele é despoletado quando o "network device detection" e o "routing offload" estão ativos. Podemos desativar o "network device detection" para contornar o problema, uma vez que a sua função não é crítica para a operação do core.
      ```cli
      # Comando a ser executado nos switches após o upgrade
      config switch network-monitor settings
          set network-monitor-mode disable
      end
      ```

---

## 4. Plano de Ação Proposto

1.  **Planeamento:** Agendar uma janela de manutenção para o upgrade dos dois switches core (`DC-L_CORE-FIB01` e `DC-L_CORE-FIB02`).
2.  **Upgrade:** Fazer o upgrade do firmware dos switches para a versão **`FortiSwitchOS 7.4.7`**. O FortiGate já está numa versão compatível (`7.4.5`).
3.  **Aplicar Workaround:** Imediatamente após o upgrade e a estabilização dos switches, aplicar o workaround para o bug `940248`, desativando o `network-monitor-mode`.
4.  **Harden FortiLink (Opcional, mas recomendado):** Aumentar a resiliência das ligações entre os switches para prevenir "ISL timing-out" e flapping, ativando o `static-isl`.
    ```cli
    # Comando a ser executado nos FortiSwitches nos troncos ISL
    config switch trunk
        edit <nome-do-trunk-isl>
            set static-isl enable
        next
    end
    ```
5.  **Monitorização:** Monitorizar ativamente o consumo de CPU, memória e a estabilidade geral da rede após a intervenção.

Esta abordagem resolve os problemas mais críticos de performance (CPU e memória) com base em correções documentadas pela Fortinet, enquanto se navega à volta do único bug persistente para o qual existe um workaround claro. É a estratégia que oferece o maior ganho de estabilidade com o menor risco associado. 