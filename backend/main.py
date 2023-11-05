import asyncio
from prisma import Prisma

async def main():
    db = Prisma()
    await db.connect()


    # Exemplos para o modelo "Paciente"
    await db.paciente.create(
        {
            "nome": "João da Silva",
            "endereco": "Rua A, 123",
            "sexo": "Masculino",
        }
    )

    await db.paciente.create(
        {
            "nome": "Maria Oliveira",
            "endereco": "Avenida B, 456",
            "sexo": "Feminino",
        }
    )

    await db.paciente.create(
        {
            "nome": "José Santos",
            "endereco": "Rua C, 789",
            "sexo": "Masculino",
        }
    )

    # Exemplos para o modelo "UnidadeDeSaude"
    await db.unidadedesaude.create(
        {
            "nome": "Hospital Municipal",
            "endereco": "Avenida X, 123",
        }
    )

    await db.unidadedesaude.create(
        {
            "nome": "Clínica de Saúde ABC",
            "endereco": "Rua Y, 456",
        }
    )

    await db.unidadedesaude.create(
        {
            "nome": "Centro de Atendimento Médico",
            "endereco": "Praça Z, 789",
        }
    )

    # Exemplos para o modelo "ProdutoMedico"
    await db.produtomedico.create(
        {
            "nome": "Aspirina",
            "descricao": "Analgésico comum",
            "estoque_atual": 500,
        }
    )

    await db.produtomedico.create(
        {
            "nome": "Seringa",
            "descricao": "Descartável, 10ml",
            "estoque_atual": 1000,
        }
    )

    await db.produtomedico.create(
        {
            "nome": "Luvas de Látex",
            "descricao": "Tamanho M",
            "estoque_atual": 2000,
        }
    )

    # Exemplos para o modelo "Veiculo"
    await db.veiculo.create(
        {
            "tipo": "Ambulância",
            "capacidade": 4,
        }
    )

    await db.veiculo.create(
        {
            "tipo": "Van Médica",
            "capacidade": 6,
        }
    )

    await db.veiculo.create(
        {
            "tipo": "Carro de Apoio",
            "capacidade": 5,
        }
    )

    # Exemplos para o modelo "TransporteDePaciente"
    await db.transportedepaciente.create(
        {
            "pacienteId": 1,
            "unidadeId": 1,
            "data_hora_transporte": "2023-11-04T10:00:00Z",
            "veiculoId": 1,
        }
    )

    await db.transportedepaciente.create(
        {
            "pacienteId": 2,
            "unidadeId": 1,
            "data_hora_transporte": "2023-11-04T11:30:00Z",
            "veiculoId": 2,
        }
    )

    await db.transportedepaciente.create(
        {
            "pacienteId": 3,
            "unidadeId": 2,
            "data_hora_transporte": "2023-11-04T13:45:00Z",
            "veiculoId": 3,
        }
    )

    # Exemplos para o modelo "EntregaDeProdutoMedico"
    await db.entregadeprodutomedico.create(
        {
            "produtoId": 1,
            "unidadeId": 1,
            "data_hora_entrega": "2023-11-04T11:00:00Z",
            "quantidade_entregue": 50,
        }
    )

    await db.entregadeprodutomedico.create(
        {
            "produtoId": 2,
            "unidadeId": 2,
            "data_hora_entrega": "2023-11-04T14:15:00Z",
            "quantidade_entregue": 20,
        }
    )

    await db.entregadeprodutomedico.create(
        {
            "produtoId": 3,
            "unidadeId": 1,
            "data_hora_entrega": "2023-11-04T16:30:00Z",
            "quantidade_entregue": 100,
        }
    )

    # Exemplos para o modelo "RotaDeTransporte"
    await db.rotadetransporte.create(
        {
            "descricao_rota": "Rota 1",
            "pontos_coleta_entrega": "Ponto A -> Ponto B -> Ponto C",
            "otimizacao_rota": "Otimização da Rota 1",
        }
    )

    await db.rotadetransporte.create(
        {
            "descricao_rota": "Rota 2",
            "pontos_coleta_entrega": "Ponto D -> Ponto E -> Ponto F",
            "otimizacao_rota": "Otimização da Rota 2",
        }
    )

    await db.rotadetransporte.create(
        {
            "descricao_rota": "Rota 3",
            "pontos_coleta_entrega": "Ponto G -> Ponto H -> Ponto I",
            "otimizacao_rota": "Otimização da Rota 3",
        }
    )
    
    await db.disconnect()


if __name__ == '__main__':
    asyncio.run(main())