# Импорт библиотеки pandas
import pandas as pd
# Импорт переменных из файла src/config.py
from src.config import FILE_TITANIC, HEAD_ROWS, url_titanic, NA_VALUES

df = pd.read_csv(                          # чтение файла с полезными параметрами
    url_titanic,                            # имя/путь файла | можно использовать локальный файл FILE_TITANIC
    sep=",",                                # разделитель "," также можно ";"
    encoding="utf-8",                       # кодировка | можно использовать ENCODINGS[0]
    na_values=NA_VALUES,                           # распознавание пропусков
    dtype={"PassengerId": "int64"},         # фиксация типов
    dayfirst=True                           # проверка дат на формат ДД/ММ/ГГГГ
)

# приведение столбца Age к числовому типу, все что не числа приводится к NA (параметр coerce)
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")
# то же самое, но некорректные данные будут игнорироваться (ignore)
#df["Age"] = pd.to_numeric(df["Age"], errors="ignore")
# то же самое, но при некорректных данных будет падать с ошибкой (raise)
#df["Age"] = pd.to_numeric(df["Age"], errors="raise")
print(df.head(HEAD_ROWS).to_string())

