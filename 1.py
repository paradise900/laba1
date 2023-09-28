import pandas as pd
import numpy as np
import csv


df = pd.read_csv('itmo_study/laba1/1.csv', sep=';', index_col='ID')
print(df.shape[0], ' - количество записей')
print()

ans = 0
for x in df['Название']:
    if len(x) > 30:
        ans += 1
        
print(ans, '- количество записей с длиной более 30')
print()

df_1 = df[df['Цена поступления'] < 200]
author = input('Введите автора: ')
a = []
i = 0
for x in df_1['Автор']:
    if x == author:
        a.append(i)
    i += 1
print(df_1.iloc[a].to_string(index = False), '- поиск книги по автору')
print()

from random import randint


ind = [randint(0, df.shape[0]) for _ in range(20)]
f = open('itmo_study/laba1/answer.txt', 'w')
for i in ind:
    s = ''
    s += str(df.iloc[i]['Автор']) + ', '
    s += df.iloc[i]['Название'] + ' - '
    s += df.iloc[i]['Дата поступления']
    s += '\n'
    f.write(s)
f.close()