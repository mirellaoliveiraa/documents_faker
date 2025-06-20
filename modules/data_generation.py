from faker import Faker
import random

faker = Faker("pt_BR")

def gerar_dados_pessoais():
    nome = faker.name()
    cpf = faker.cpf()
    endereco = faker.address().replace("\n", ", ")
    crm = f"{random.randint(10000, 99999)}/{random.choice(['SP', 'RJ', 'MG', 'BA'])}"
    return nome, cpf, endereco, crm
