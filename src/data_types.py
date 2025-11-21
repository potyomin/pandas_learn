import pandas as pd


###
#   ГЛАВА 3. ТИПЫ ДАННЫХ В PANDAS
###

s = pd.Series([1,2,3])
# Вывод информации о Series, где будет видно, какой тип данных у этого столбца
print(s.info(), '\n')

d = [{'name': 'pen', 'price': 3.9, 'count': 8},
     {'name': 'book', 'price': 4.5, 'count': 11}]

df = pd.DataFrame(d)

# Вывод информации о DataFrame, где мы увидим три разных типа данных
print(df.info(), '\n')

###
#   3.1 ТИПЫ ДАННЫХ
###

# Использование метода dtypes, метод предназначен для вывода типов данных
print(s.dtypes, '\n')
print(df.dtypes, '\n')

###
#   3.2 ИНСТРУМЕНТЫ ДЛЯ РАБОТЫ С ТИПАМИ
###

###
#   3.2.1 astype()
###

# изменение типа данных при помощи astype()
s = s.astype('float64')
print(s.dtype, '\n')

df['count'] = df['count'].astype('int32')
print(df.dtypes, '\n')
# возврат к исходному типу данных
df = df.astype({'count': 'int64'})
print(df.dtypes, '\n')

