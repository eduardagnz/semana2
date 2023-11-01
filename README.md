# semana2
Atividade ponderada M6 - semana 2

## Modelo Lógico:
Entendendo a complexidade e a inter-relação entre o transporte de pacientes e a logística de produtos médicos, vou propor um esboço do modelo lógico do banco de dados que aborde os principais aspectos do sistema proposto.

**Modelo Lógico:**

1. **Entidades Principais:**
    a. **Paciente:** Representa informações detalhadas sobre os pacientes, incluindo dados pessoais, informações médicas, histórico de tratamento, etc.
    
    b. **Fornecedores de Produtos Médicos:** Inclui informações sobre os fornecedores de suprimentos médicos, detalhes de contato, catálogos de produtos, etc.
    
    c. **Unidades de Saúde:** Representa hospitais, clínicas e centros de atendimento médico. Inclui detalhes sobre localização, especialidades médicas, capacidade de atendimento, etc.

    d. **Veículos Médicos:** Detalhes sobre a frota de veículos utilizados para o transporte de pacientes e entrega de suprimentos médicos.

    e. **Produtos Médicos:** Informações detalhadas sobre os produtos médicos, incluindo estoque, validade, descrição, etc.

2. **Relacionamentos:**
    - Um paciente pode estar associado a diversos registros médicos, tratamentos, consultas, etc.
    - As Unidades de Saúde estão relacionadas aos pacientes que são atendidos por elas.
    - Os Veículos Médicos estão associados às rotas, agendamentos de transporte de pacientes e entregas de suprimentos.
    - Os Produtos Médicos estão vinculados aos fornecedores, unidades de saúde (estoque) e às entregas.

3. **Relacionamentos Específicos para Otimização:**
    - Relacionamento entre rotas de transporte de pacientes e a otimização das mesmas.
    - Relacionamento entre as entregas de produtos médicos e a otimização das rotas para garantir a eficiência da logística.

4. **Atributos e Campos:**
    - Os atributos para cada entidade devem ser identificados de acordo com as necessidades específicas de rastreamento e gerenciamento. Por exemplo, para pacientes, isso pode incluir informações pessoais, histórico médico, informações de seguros, etc. Para produtos médicos, pode incluir detalhes de estoque, data de validade, lote, etc.



![Alt text](../semana2/imagens/image.png)