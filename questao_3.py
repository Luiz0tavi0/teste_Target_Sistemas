# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem
# que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE: a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; b) Podem existir dias sem
# faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json
import os
from collections import deque

KEY_VALUE = 'valor'
KEY_NAME = 'dia'


def get_result_for_generator(gen):
    value = None
    for v_gen in gen:
        value = v_gen
    return value


class Problem3Resolution:
    def __init__(self, path_file: str):
        self.__filepath = path_file
        self.__file_size = os.path.getsize(self.__filepath)

    def __get_rows(self):
        with open(self.__filepath, 'r', encoding='utf-8') as f:
            for row in self.__get_chunk(f):
                yield json.loads(row)

    def __get_chunk(self, f):
        chunk = ''
        while f.tell() != self.__file_size:
            letter = f.read(1)
            if letter != '{':
                continue
            chunk += letter
            while f.tell() != self.__filepath:
                letter = f.read(1)
                chunk += letter
                if letter == '}':
                    yield chunk
                    chunk = ''
                    break

    def __low_high_billing(self) -> tuple:
        """Returns a tuple containing the lowest and highest billing value"""
        gen_data = self.__get_rows()
        min_value = max_value = 0.0

        try:
            while True:
                data = next(gen_data)
                value_by_day = data[KEY_VALUE]
                min_value = min(min_value, value_by_day)
                max_value = max(max_value, value_by_day)
                yield min_value, max_value
        except StopIteration:
            pass

    def __media(self):
        """Return tuple with median and sum"""
        count = s = 0
        gen_data = self.__get_rows()
        try:
            while True:
                data = next(gen_data)
                value_by_day = data[KEY_VALUE]
                if not value_by_day:
                    continue
                count += 1
                s += value_by_day
                yield s / count
        except StopIteration:
            pass

    def __days_with_higher_than_average(self):
        month_media = get_result_for_generator(self.__media())
        count_days = 0
        try:
            gen_data = self.__get_rows()
            while True:
                data = next(gen_data)
                value_by_day = data[KEY_VALUE]
                if value_by_day < month_media: continue
                count_days += 1
                yield count_days
        except StopIteration:
            pass

    def __call__(self, *args, **kwargs):
        lowest, higher = get_result_for_generator(self.__low_high_billing())
        days_billing_greater = get_result_for_generator(self.__days_with_higher_than_average())
        print(
            f"O menor valor de faturamento ocorrido no mês: {lowest}\n"
            f"O maior valor de faturamento ocorrido no mês: {higher}\n"
            f"Número de dias no mês em que o valor de faturamento diário foi superior"
            f" à média mensal: {days_billing_greater}"
        )

if __name__ == '__main__':
    filepath = 'dados.json'
    solver = Problem3Resolution(filepath)
    solver()
