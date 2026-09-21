# Importa as funções do módulo calculadora.
from calculadora import somar, subtrair, multiplicar, dividir

# Chama as funções e mostra os resultados.
print("Soma:", somar(10, 5))                # 15
print("Subtração:", subtrair(10, 5))        # 5
print("Multiplicação:", multiplicar(10, 5)) # 50
print("Divisão:", dividir(10, 5))           # 2.0

# Testa a divisão por zero sem interromper o programa.
resultado = dividir(10, 0)

if resultado is None:
    print("Não é possível dividir por zero.")
else:
    print("Divisão:", resultado)