###
#   3.2.2 ФУНКЦИИ ПОДГОТОВКИ ДАННЫХ
###

import pandas as pd
from src.config import FILE_DATA, ENCODINGS

# Читаем датафрейм
df = pd.read_csv(FILE_DATA, sep=';', encoding=ENCODINGS[2])

print(df, '\n')
print(df.dtypes, '\n')

# Задание функций для смены типов
temper_convertor = lambda x: x.replace('°C', '').strip()
pressure_convertor = lambda x: x.replace('Па', '').strip()
prec_convertor = lambda x: True if x == 'Да' else False

# Использование функций
df['Температура'] = df['Температура'].apply(temper_convertor).astype('float64')
df['Давление'] = df['Давление'].apply(pressure_convertor).astype('int64')
df['Осадки'] = df['Осадки'].apply(prec_convertor)

print(df.dtypes, '\n')
