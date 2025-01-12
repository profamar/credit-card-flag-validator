def get_credit_card_flag(card_number):
    """
    Retorna a bandeira do cartão de crédito com base no número do cartão.

    Args:
        card_number (str): Número do cartão de crédito.

    Returns:
        str: Bandeira do cartão de crédito.
    """
    card_number = str(card_number)
    
    # Prefixos das bandeiras
    prefixes = {
        "Visa": ["4"],
        "MasterCard": [str(i) for i in range(51, 56)],
        "American Express": ["34", "37"],
        "Discover": ["6011"] + [str(i) for i in range(622126, 622926)] + [str(i) for i in range(644, 650)] + ["65"],
        "JCB": [str(i) for i in range(3528, 3590)]
    }
    
    for flag, prefix_list in prefixes.items():
        for prefix in prefix_list:
            if card_number.startswith(prefix):
                return flag
    
    return "Bandeira desconhecida"

# Exemplo de uso
if __name__ == "__main__":
    print(get_credit_card_flag("4111111111111111"))  # Visa
    print(get_credit_card_flag("5105105105105100"))  # MasterCard
    print(get_credit_card_flag("371449635398431"))   # American Express
    print(get_credit_card_flag("6011111111111117"))  # Discover
    print(get_credit_card_flag("3530111333300000"))  # JCB
