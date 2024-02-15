def extrair_simples(string_entrada):
    partes = string_entrada.split()
    nome = partes[0]
    numero = partes[1]
    return nome, numero

def extrair_complicado(string_entrada):
    partes = string_entrada.split()

    if partes[2].isdigit():
        numero = partes[2]
        nome = ' '.join(partes[:-1])
    else:
        numero = ' '.join(partes[3:])
        nome = ' '.join(partes[:3])

    return nome, numero

caso_simples = [
    "Miritiba 339",
    "Babaçu 500",
    "Cambuí 804B"
]

for endereco in caso_simples:
    nome, numero = extrair_simples(endereco)
    print(f"{endereco} -> {nome}, {numero}")

casos_complicados = [
    "Rio Branco 23",
    "Quirino dos Santos 23 b"
]

for endereco in casos_complicados:
    nome, numero = extrair_complicado(endereco)
    print(f"{endereco} -> {nome}, {numero}")
