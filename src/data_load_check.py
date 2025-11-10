# Импорт библиотеки pandas
import numpy as np
import pandas as pd
# Импорт переменных из файла src/config.py
from src.config import FILE_TITANIC, HEAD_ROWS, url_titanic


df = pd.read_csv(url_titanic)               # чтение csv-файла
# df = pd.read_excel("file.xlsx")           # чтение excel-файла
# df = pd.read_parquet("file.parquet")      # чтение parquet-файла

NA = ["", "NA", "N/A", "-", "null"]         # список возможных пустых значений в файле

df1 = pd.read_csv(                          # чтение файла с полезными параметрами
    url_titanic,                            # имя/путь файла
    sep=",",                                # разделитель "," также можно ";"
    encoding="utf-8",                       # кодировка
    na_values=NA,                           # распознавание пропусков
    dtype={"PassengerId": "int64"},         # фиксация типов
    dayfirst=True                           # проверка дат на формат ДД/ММ/ГГГГ
)

print(f"Количество строк:", df.shape[0])                # вывод количества строк
print(f"Количество столбцов:", df.shape[1])             # вывод количества столбцов
print(f"Количество строк и столбцов:", df.shape,"\n")   # вывод количества строк и столбцов

print(df.head(HEAD_ROWS), "\n")         # вывод заданного количества первых строк файла в консоль
print(df.head(5), "\n")                 # вывод 5 первых строк файла в консоль
print(df.tail(HEAD_ROWS), "\n")         # вывод заданного количества последних строк файла в консоль
print(df.tail(5), "\n")                 # вывод 5 последних строк файла в консоль
print(df.sample(5), "\n")               # вывод 5 случайных строк файла

print(df.info(), "\n")                  # вывод информации: типы, пропуски, размер файла

print(df.describe(), "\n")                      # вывод базовой статистики по колонкам: min, max, mean, std, count и др
print(df.describe(include="object"), "\n")      # вывод базовой статистики по колонкам типа object, вывод кол-ва уникальных значений и др

print(df.nunique(), "\n")               # количество уникальных значений в каждом столбце

print(df.notna(),"\n")                  # вывод таблицы true/false которая показывает где есть ненулевые значения
print(df.isnull(),"\n")                 # аналог предыдущего метода, но наоборот, показывает true/false

print(df.notna().sum(), "\n")           # вывод количества ненулевых элементов по каждому столбцу
print(df.isnull().sum(), "\n")          # вывод количества нулевых элементов по каждому столбцу

