# 5) Escreva um programa que inverta os caracteres de um string.
import sys


def reverse_string(text: str) -> str:
    last_position = len(text)
    reversed_text = ''
    while last_position:
        last_position -= 1
        reversed_text += text[last_position]

    return reversed_text


if __name__ == '__main__':
    # Run examples
    #  python.exe .\questao_5.py "Adias a data da saída"
    #  python.exe .\questao_5.py "A miss é péssima"
    #  python.exe .\questao_5.py "Acuda cadela da Leda caduca"
    #  python.exe .\questao_5.py "Anotaram a data da maratona"
    text = sys.argv[1]
    print(reverse_string(text))
