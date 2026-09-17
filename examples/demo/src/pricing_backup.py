"""Regra fictícia de desconto, com valores inteiros em centavos."""


def total_com_desconto(subtotal_centavos):
    if subtotal_centavos >= 10000:
        return subtotal_centavos - subtotal_centavos * 10 // 100
    return subtotal_centavos
