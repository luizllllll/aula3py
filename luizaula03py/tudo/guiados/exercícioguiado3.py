# Recebe vários preços e um desconto opcional.
def total(*precos, desc=0):
    s = sum(precos)  # Soma os preços.
    return s * (1 - desc / 100)  # Retorna o total com desconto.


print(total(10, 25.5, 7))  # Sem desconto: 42.5
print(total(10, 25.5, 7, desc=10))  # Com 10% de desconto: 38.25