import pandas as pd

###
#   2.7 ИСПОЛЬЗОВАНИЕ isin ПРИ РАБОТЕ С ДАННЫМИ PANDAS
###

# S

s = pd.Series([10,20,30,40,50,10,10], ['a', 'b', 'c', 'd', 'e', 'f', 'g'])

# метод isin возвращает все значения в формате bool
print(s.isin([10,20]), '\n')

df = pd.DataFrame({'price': [1,2,3,5,6],
                   'count': [10,20,30,40,50],
                   'percent': [24,51,71,25,42]})

print(df.isin([1,3,25,30,10]), '\n')
