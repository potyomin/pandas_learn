import pandas as pd         # импорт библиотеки pandas
import numpy as np          # импорт библиотеки numpy

# Создание объекта Series
s = pd.Series([10,20,30,40,50], index=['a','b','c','d','e'])
print(s['a'], '\n')
print(s, '\n')

# Доступ к Series с использованием меток
print(s.loc['a'], '\n')
print(s.loc[['a', 'b', 'e']], '\n')
print(s.loc['a':'c'], '\n')
print(s.loc[:'c'], '\n')        # аналог предыдущего
# Везде используется .loc, но все будет работать и без него
# так мы более явно указываем, что работаем по меткам, а не по позиции

# Использование lambda-функции
print(s.loc[lambda x: x >= 30], '\n')

# Использование логического выражения
print(s.loc[s > 30], '\n')

# Создание объекта DataFrame
d = {'price': [1,2,3,],
    'count': [10,20,30],
    'percent': [24,51,71]}
df = pd.DataFrame(d, index=['a','b','c'])
print(df, '\n')

# Доступ к DataFrame с использованием меток
print(df.loc[:, 'count'], '\n')
print(df.loc[:, ['count', 'price']], '\n')
print(df.loc['a':'b', :], '\n')
# Также рекомендуется везде использовать .loc,
# но при этом не забывать указывать ":" для использования всех строк

# Доступ к DF с использованием callback - функции
print(df.loc[lambda x: x['count'] > 15], '\n')
print(df.loc[df['count'] > 15], '\n')           # Записи эквивалентны

# Доступ с использованием логического выражения
print(df.loc[df['price'] >= 2], '\n')
