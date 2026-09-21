# DESAFIO 5 — Importa o módulo com as três funções.
import desafio1

# DESAFIO 4 — Ficha do aluno.
def ficha_aluno(**dados):
    """Mostra uma informação do aluno por linha."""
    for campo, valor in dados.items():
        print(f"{campo}: {valor}")

# DESAFIO 6 — Lista segura.
def adicionar_item(lista, item):
    """Adiciona um item sem alterar a lista original."""
    nova_lista = lista.copy()  # Copia a lista recebida.
    nova_lista.append(item)    # Adiciona o item à cópia.
    return nova_lista


print("DESAFIO 1 — Temperatura")
print("Fahrenheit:", desafio1.celsius_para_fahrenheit(25))

print("\nDESAFIO 2 — Senha")
print("Senha curta:", desafio1.validar_senha("abc"))
print("Senha válida:", desafio1.validar_senha("abcd1234"))

print("\nDESAFIO 3 — Caixa")
# Cada variável recebe um dos três valores retornados.
total, mais_caro, media = desafio1.caixa(10, 20, 30)

print("Total:", total)
print("Mais caro:", mais_caro)
print("Média:", media)

print("\nDESAFIO 4 — Ficha do aluno")
ficha_aluno(nome="Ana", idade=20, curso="Computação")

print("\nDESAFIO 6 — Lista segura")
materiais = ["caderno", "caneta"]
nova_lista = adicionar_item(materiais, "livro")

print("Original:", materiais)
print("Nova:", nova_lista)