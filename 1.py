import pandas as pd
import numpy as np
import csv
from random import randint

MIN_NAME_LENGTH = 30
MAX_BOOK_PRICE = 200
quantity = 20

book_records = pd.read_csv('itmo_study/laba1/1.csv', sep=';', index_col='ID')
print(f'{book_records.shape[0]} - количество записей\n')


books_long_names = book_records.query(f'Название.str.len() > {MIN_NAME_LENGTH}')  
print(f'{books_long_names} - количество записей с длиной более 30\n')


book_records_1 = book_records[book_records['Цена поступления'] < MAX_BOOK_PRICE]
input_author = input('Введите автора: ')
notes = []
position = 0
for author in book_records_1['Автор']:
    if author == input_author:
        notes.append(position)
    position += 1
print(f'{book_records_1.iloc[notes].to_string(index = False)} - поиск книги по автору\n')


random_indxs = [randint(0, book_records.shape[0]) for _ in range(quantity)]
file = open('itmo_study/laba1/answer.txt', 'w')
for index in random_indxs:
    book = book_records.iloc[index]
    autor = book['Автор']
    name = book['Название']
    date = book['Дата поступления']
    link = f'{autor}, {name} - {date}\n'
    file.write(link)
file.close()