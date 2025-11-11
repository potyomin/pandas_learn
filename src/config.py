from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT / 'data'
FILE_TITANIC = DATA_DIR / 'Titanic.csv'


url_titanic = "https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv"

# список с кодировками
ENCODINGS = [
    # универсальные
    "utf-8", "utf-8-sig",
    # кириллица / Windows-рус
    "cp1251", "koi8-r", "koi8-u", "iso-8859-5", "mac_cyrillic", "cp866",
    # запад/центр Европа
    "cp1252", "latin-1", "iso-8859-15", "cp1250", "iso-8859-2",
    "cp1253", "iso-8859-7", "cp1254", "iso-8859-9", "cp1257", "cp1258",
    # Азия
    "gb18030", "gbk", "big5", "shift_jis", "euc_jp", "iso2022_jp",
    "cp949", "euc_kr", "cp874", "tis-620",
    # реже встречается
    "utf-16", "utf-16-le", "utf-16-be",
    "utf-32", "utf-32-le", "utf-32-be",
    "cp437", "cp850", "mac_roman",
]

# список возможных пустых значений в файле
NA_VALUES = [
    "", " ",             # пусто и пробел
    "NA", "na", "N/A", "n/a",
    "-", "—",            # тире (обычно «нет данных»)
    "None", "none",
    "NULL", "null",
    "NaN", "nan", "<NA>",
]

# переменная для количества выводимых строк
HEAD_ROWS = 10
