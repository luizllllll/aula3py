# Recebe dois valores e usa 2 casas decimais como padrão.
def media(a, b, casas=2):
    m = (a + b) / 2  # Calcula a média dos dois valores.
    return round(m, casas)  # Devolve a média arredondada.


print(media(8, 6))  # Usa o padrão de 2 casas: 7.0
print(media(8, 5, 1))  # Define 1 casa decimal: 6.5