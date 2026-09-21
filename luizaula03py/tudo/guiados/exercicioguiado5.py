# Importa as funçoes criandos na calculadora.py
from calculadora import somar, multiplicar

def orc(qtd, preco, frete=0):              
    """Total do pedido."""         # Define a funçao que calcula o valor total de um pedido
    s = multiplicar(qtd, preco)
    return somar(s, frete)
print(orc(3, 49.9, 15)) # 164.7