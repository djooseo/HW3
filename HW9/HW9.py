"""
1. Створіть файл lib.py, помістіть в нього допоміжні функції вашої програми "Касир".
   Імпортуйте їх для основної функції в основний файл. Запустіть "Касир" з основного файлу.
2. Помістіть в lib.py декоратор для вимірювання часу.
   Імпортуйте декоратор в основний файл, задекоруйте основну функцію "Касир".
"""

import lib


@lib.decorator_time
def final_res():
    prompt = 'Вкажіть ваш вік: '
    res = lib.age_input(prompt)
    lib.cashier_in_cinema(res)


final_res()