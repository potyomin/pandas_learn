import pandas as pd
import numpy as np


###
#   2.6 ИНДЕКСАЦИЯ С ИСПОЛЬЗОВАНИЕМ ЛОГИЧЕСКИХ ВЫРАЖЕНИЙ
###

# S

s = pd.Series([10,20,30,40,50,10,10], ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# Используем везде подобие WHERE в SQL
# Выводим значения больше 30
print(s[s>30], '\n')
print(s[s==10], '\n')
print(s[(s>10)&(s<=40)], '\n')

# DF

d = {'price': [1,2,3,5,6],
     'count': [10,20,30,40,50],
     'percent': [24,51,71,25,42],
     'cat': ['A', 'B', 'A', 'A', 'C']
}
df = pd.DataFrame(d)
print(df, '\n')
print(df[df['price']>3], '\n')  # Выводим все строки, учитывая условие по определенному столбцу
print(df[df['cat']=='A'], '\n')
print(df['cat'].map(lambda x: x == 'A'), '\n')
# Доступно использование функций map lambda filter и др
fn = df['cat'].map(lambda x: x == 'A')
print(df[fn], '\n')
