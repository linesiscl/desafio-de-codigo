def extrair_simples(string_entrada):
    partes = string_entrada.split()
    nome = partes[0]
    numero = partes[1]
    return nome, numero

caso_simples = [
    "Miritiba 339",
    "Babaçu 500",
    "Cambuí 804B"
]

for endereco in caso_simples:
    nome, numero = extrair_simples(endereco)
    print(f"{endereco} -> {nome}, {numero}")

