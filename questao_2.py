# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores
# anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde,
# informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número
# informado pertence ou não a sequência.

import sys

def fibo():
    """Gerador de números Fibonacci"""
    previous = 0
    later = 1
    while True:
        yield previous
        previous, later = (previous + later), previous


def in_sequence(n: int):
    """Verifica se o número procurado n está contido na sequência de Fibonacci"""
    gen_fibo = fibo()
    fb_number = 0
    while fb_number <= n:
        fb_number = next(gen_fibo)
        if fb_number == n:
            return True
    return False


if __name__ == '__main__':
    # Execute a linha no console
    # python.exe .\questao_2.py 1134903170
    n = int(sys.argv[1])

    print(f'O número {n}{" " if in_sequence(n) else " não "}faz parte da sequência de fibonacci.')

