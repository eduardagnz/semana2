# semana2
Atividade ponderada M6 - semana 2

## Passos Seguidos:
1. Com a criação de um RDS e um repositório, foi necessário instalar o prisma e conectar ao diretório
![Alt text](../semana2/imagens/image-2.png)
![Alt text](../semana2/imagens/image.png)

2. Fazer a incerção de dados do arquivo 'main.py' para o banco de dados
![Alt text](../semana2/imagens/image-1.png)


3. Para verificar se estava funcionando, utilizei o 'Workbench' e com o sucesso da conexão, fiz uma query de teste para confirmação.
![Alt text](../semana2/imagens/imagea.png)

4. Com a conexão funcionando, fiz a query como pedido na atividade ponderada, com o resultado a seguir:
![Alt text](../semana2/imagens/image-3.png)

## Modelo Lógico:
Entendendo a complexidade e a inter-relação entre o transporte de pacientes e a logística de produtos médicos, vou propor um esboço do modelo lógico do banco de dados que aborde os principais aspectos do sistema proposto.

**Modelo Lógico:**

![Alt text](../semana2/imagens/modelo.png)

1. **Relacionamentos:**
    - Um paciente pode estar associado a diversos registros médicos, tratamentos, consultas, etc.
    - As Unidades de Saúde estão relacionadas aos pacientes que são atendidos por elas.
    - Os Veículos Médicos estão associados às rotas, agendamentos de transporte de pacientes e entregas de suprimentos.
    - Os Produtos Médicos estão vinculados aos fornecedores, unidades de saúde (estoque) e às entregas.

2. **Relacionamentos Específicos para Otimização:**
    - Relacionamento entre rotas de transporte de pacientes e a otimização das mesmas.
    - Relacionamento entre as entregas de produtos médicos e a otimização das rotas para garantir a eficiência da logística.

3. **Atributos e Campos:**
    - Os atributos para cada entidade devem ser identificados de acordo com as necessidades específicas de rastreamento e gerenciamento. Por exemplo, para pacientes, isso pode incluir informações pessoais, histórico médico, informações de seguros, etc. Para produtos médicos, pode incluir detalhes de estoque, data de validade, lote, etc.