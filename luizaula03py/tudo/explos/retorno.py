def rel(titulo, *itens, fmt="txt", **extras):
    print(titulo, fmt)
    print(itens)
    print(extras)

rel("vendas", "jan", "fev", fmt="pdf", autor="Ana")