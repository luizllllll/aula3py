def criar(nome, ativo=True):
    if ativo:
        s = "Disponivel"

    else:
        s = "Esgotado"
    return nome + "-" + s

print(criar("Caneta", False))