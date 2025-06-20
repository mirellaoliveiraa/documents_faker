import random

def substituir_palavras(texto):
    substituicoes = {
        "paciente": ["indivíduo", "cliente", "assistido"],
        "compareceu": ["esteve presente", "veio", "apresentou-se"],
        "médico": ["doutor", "profissional de saúde", "especialista"],
        "documento": ["arquivo", "ficha", "registro"],
    }
    for palavra, sinonimos in substituicoes.items():
        if palavra in texto:
            texto = texto.replace(palavra, random.choice(sinonimos))
    return texto

def inserir_erros(texto):
    texto_modificado = ""
    for c in texto:
        texto_modificado += c
        if random.random() < 0.01:
            texto_modificado += random.choice(["", " ", ".", ","])
    return texto_modificado
