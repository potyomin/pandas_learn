import pandas as pd         # импорт библиотеки pandas
import numpy as np          # импорт библиотеки numpy

# Создание DataFrame из Series
d = {
    'price':pd.Series(data=[1, 2, 3], index=['v1', 'v2', 'v3']),
    'count':pd.Series([10, 12, 7], ['v1', 'v2', 'v3'])
}
df1 = pd.DataFrame(d)
print(df1, '\n')

# Вывод отдельного столбца из DataFrame
print(df1['price'], '\n')
print(df1['count'], '\n')

# Вывод индексов и названий столбцов
print(df1.index, '\n')
print(df1.columns, '\n')

# Создание DataFrame из ndarray
d2 = {
    'price':np.array([1, 2, 3]),
    'count': np.array([10, 12, 7])
}
df2 = pd.DataFrame(d2, index=['v1', 'v2', 'v3'])
print(df2, '\n')

# Вывод индексов и названий столбцов
print(df2.index, '\n')
print(df2.columns, '\n')

# Создание DataFrame из списка словарей
d3 = [
    {'price': 3, 'count': 8},
    {'price': 4, 'count': 11}
]
df3= pd.DataFrame(d3)
print(df3, '\n')

# Вывод сводной информации
print(df3.info(), '\n')

# Создание DataFrame из двумерного массива
nda1 = np.array([[1, 2, 3],
                 [10, 20, 30]])
df4 = pd.DataFrame(nda1)
print(df4, '\n')

# Создание df для работы с элементами
d5 = {
    'price': np.array([1, 2, 3]),
    'count': np.array([10, 20, 30])
}
df5 = pd.DataFrame(d5, index=['a', 'b', 'c'])
print(df5, '\n')
print(df5['count'],'\n')
print(df5.loc['a'],'\n')
print(df5.iloc[1],'\n')
print(df5[0:2],'\n')
print(df5[df5['count'] >= 20],'\n')
