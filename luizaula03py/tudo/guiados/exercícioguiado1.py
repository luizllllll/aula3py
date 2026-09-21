# Recebe um nome e devolve uma saudação.
def saudar(nome):
    return "Ola, " + nome + "!"  # Junta os textos com o nome.


print(saudar("Ana"))  # Mostra: Ola, Ana!

msg = saudar("Edilson")  # Guarda a saudação na variável msg.
print(msg.upper())  # Mostra em maiúsculas: OLA, EDILSON!