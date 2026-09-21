def real(titulo, *itens,
         fmt= "txt", **extras):
    print(titulo, fmt)
    print(itens)     #tupla
    print(extras)    #dicionario

real("vendas", "jan", "fev",
     fmt= "pdf", autor="Ana")