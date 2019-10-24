import sqlite3
import pandas as pd

# pandas 读取数据库文件。
conn = sqlite3.connect('../db/dhl.db')
sql = "SELECT awb_no,orig_fclty,shacct_no,esiteid,eclientApp,cSales_cd,cleaned_product_code,PLT FROM ecom_base_201909"
# 返回DataFrame对象
df = pd.read_sql(sql, conn)

# All Awb
all = df.count()
plt = df.loc[df['PLT'] == 'Y'].count()
all_plt = plt / all
all_plt.to_csv("hello.csv")
# print(plt)
conn.close()

# df.to_excel("/Users/apple/Documents/dhl_ecom_data/test.xlsx", sheet_name='hello')
# df.to_csv("hello.csv")
# print(df.columns)