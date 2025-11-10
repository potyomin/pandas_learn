from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT / 'data'
FILE_TITANIC = DATA_DIR / 'Titanic.csv'


url_titanic = "https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv"


HEAD_ROWS = 10
