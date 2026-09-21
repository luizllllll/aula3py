# DESAFIO 1 — Conversor de temperatura.
def celsius_para_fahrenheit(c):
    """Converte Celsius para Fahrenheit."""
    return c * 9 / 5 + 32

# DESAFIO 2 — Validador de senha.
def validar_senha(senha):
    """Verifica se a senha tem pelo menos 8 caracteres."""
    return len(senha) >= 8  # Retorna True ou False.

# DESAFIO 3 — Caixa com vários preços.
def caixa(*precos):
    """Retorna o total, o maior preço e a média."""
    if not precos:
        return 0, None, 0  # Trata a chamada sem preços.

    total = sum(precos)          # Soma todos os preços.
    mais_caro = max(precos)      # Encontra o maior preço.
    media = total / len(precos)  # Divide pela quantidade.

    return total, mais_caro, media