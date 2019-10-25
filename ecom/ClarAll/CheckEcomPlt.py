import pandas as pd
import sqlite3

conn = sqlite3.connect('C:\\Users\\admin\\Desktop\\dhl_ecom_plt\\db\\dhl.db')
df = pd.read_sql("select * from ecom_plt_monthly", conn)
print(df)