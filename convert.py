import pandas as pd
import sqlite3 as sq

conn = sq.connect('measurements.db')
c = conn.cursor()
df = pd.read_sql('SELECT * from measurements', conn)
df.to_parquet('measurements.parquet')

conn = sq.connect('sample.db')
c = conn.cursor()
df = pd.read_sql('SELECT * from measurements', conn)
df.to_parquet('sample.parquet')
