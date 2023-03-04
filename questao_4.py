# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve
# dentro do valor total mensal da distribuidora.
import re
import sys

monthly_billing_by_state = {
    'SP': 'R$67.836,43',
    'RJ': 'R$36.678,66',
    'MG': 'R$29.229,88',
    'ES': 'R$27.165,48',
    'Outros': 'R$19.849,53'
}


def parse_money_value(value: str):
    value_without_currency_symbols = re.search(r"\d+.*", value).group()
    return float(value_without_currency_symbols.replace('.', '').replace(',', '.'))


def sum_all(billings: dict):
    return sum(parse_money_value(value) for value in billings.values())


def percentage_representation_for_state(uf: str):
    value_by_state = parse_money_value(monthly_billing_by_state.get(uf, monthly_billing_by_state['Outros']))
    return 100*(value_by_state/sum_all(monthly_billing_by_state))


if __name__ == '__main__':
    # Run example
    # python.exe.\questao_4.py SP
    state = sys.argv[1]

    print(f'UF: {state}\nRepresentação: {percentage_representation_for_state(state):.2f}%')