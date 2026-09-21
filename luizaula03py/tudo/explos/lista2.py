#copia defensiva antes de alterar
def total(carrinho):
    itens = carrinho[:]
    itens.append("brinde")
    return itens

original = ["arroz", "batata", "feijao", "Sal"]
novo = total(original)
print(original)         #lista original = ['arroz', 'batata', 'feijao', 'sal']
print(novo)             #mostrando na tela ['arroz', 'brinde']. motivo --> itens.append("brinde")