# Define uma função que recebe uma nota e, opcionalmente, uma lista.
# Se nenhuma lista for informada, boletim recebe None.
def reg(nota, boletim=None):
    """Não altera a lista original."""

    # Verifica se nenhuma lista foi passada para a função.
    if boletim is None:
        boletim = []  # lista vazia
    novo = boletim[:]
    novo.append(nota)
    return novo

notas = [7]
# Passa 9 como nota e a lista notas como boletim.
print(reg(9, notas))
print(notas)