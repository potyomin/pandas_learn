import pandas as pd         # импорт библиотеки pandas
import numpy as np          # импорт библиотеки numpy

# Создание Series на основе списка
s1 = pd.Series([1,2,3,4,5])
print(s1, '\n')

# Создание Series на основе списка с индексами
s2 = pd.Series([1,2,3,4,5], ['a','b','c','d','e'])
print(s2, '\n')
print(pd.Series(['a','b','c','d','e']),'\n')

# Создание ndarray массива
ndarr = np.array([1,2,3,4,5])
print(type(ndarr))
print(ndarr, '\n')

# Создание Series на основе ndarray
s3 = pd.Series(ndarr, ['a','b','c','d','e'])
print(s3, '\n')

# Создание Series на основе словаря dict
d = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
s4 = pd.Series(d)
print(s4, '\n')

# Создание Series на основе константы const
a = 5
s5 = pd.Series(a, ['a','b','c','d','e'])
print(s5, '\n')

# Работа с элементами Series
s6 = pd.Series([1,2,3,4,5],['a','b','c','d','e'])
print(s6[2], '\n')
print(s6['d'], '\n')
print(s6[:2], '\n')
print(s6[s6 <= 3], '\n')

s7 = pd.Series([10,20,30,40,50],['a','b','c','d','e'])
print(s6 + s7, '\n')
print(s6 * 3, '\n')
