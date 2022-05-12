# engru.py

import json

import sys
import random
import keyboard


def rus():
    print('Переводим с английского на русский: \n')


def eng():
    print('Переводим с русского на английский: \n')


yes = ['yes', 'y', 'да', 'д']
no = ['no', 'n', 'нет', 'н']

if __name__ == '__main__':
    x = input('Перевести слово с английского (д/н)?: ')
    print('Ваш выбор: ', x)
    if x in yes:
        rus()
    elif x in no:
        eng()
    else:
        print('Некорректный ввод...')
