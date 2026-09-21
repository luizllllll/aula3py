def add(lista, item):
    lista.append(item)     #altera ojeto

compras = ["arroz"]
add(compras, "ovos")
add(compras , "feijao")
print(compras)             #['arroz', 'feijao']

#copia defensiva: proteje o riginal
compras[1] = "cafe"
print(compras)