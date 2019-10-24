import sqlite3
import pandas as pd

# pandas load data from sqlites3。
conn = sqlite3.connect('../db/dhl.db')
sql = "SELECT awb_no,orig_fclty,shacct_no,esiteid,eclientApp,cSales_cd,cleaned_product_code,PLT FROM ecom_base_201909"

# return DataFrame object
df = pd.read_sql(sql, conn)

# convert str to int, the method only allow all num str.
# df['awb_no'].astype("int")

# show data types
print(df.dtypes)

# show the DataFrame column
print(df.columns)

# non_doc = All Awb expect Doc
non_doc = df.loc[(df['cleaned_product_code'].isin(['3', '4', '8', 'E', 'F', 'H', 'J', 'M', 'P', 'Q', 'V', 'Y']))]

# All PLT percentage
all_plt_awb = non_doc.loc[non_doc['PLT'] == 'Y'].count().tolist()[0]
plt = all_plt_awb / non_doc.count().tolist()[0]
# print(all_awb)
# print(all_plt_awb)
print("All PLT: ", plt)

# Pre acc percentage / DataFrame.str() -> convert it to string, and you can use string methods
pre_awb = non_doc.loc[non_doc['shacct_no'].str.startswith('60')]
pre_plt_awb = non_doc.loc[(non_doc['shacct_no'].str.startswith('60')) & (non_doc['PLT'] == 'Y')].count().tolist()[0]
pre_plt = pre_plt_awb / pre_awb.count().tolist()[0]
# print(pre_awb)
# print(pre_plt_awb)
print("Pre Acc PLT: ", pre_plt)

# Pre acc percentage / DataFrame.str() -> convert it to string, and you can use string methods
imp_awb = non_doc.loc[(non_doc['shacct_no'].str.startswith('95'))|(non_doc['shacct_no'].str.startswith('96'))]
imp_plt_awb = imp_awb[imp_awb['PLT'] == 'Y'].count().tolist()[0]
imp_plt = imp_plt_awb / imp_awb.count().tolist()[0]
# print(imp_awb.count().tolist()[0])
# print(imp_plt_awb)
print("Pre Acc PLT: ", imp_plt)

conn.close()

# df.to_excel("/Users/apple/Documents/dhl_ecom_data/test.xlsx", sheet_name='hello')
# df.to_csv("hello.csv")


# non_doc = df.loc[(df['cleaned_product_code'] == '3') | (df['cleaned_product_code'] == ) |
#                        (df['cleaned_product_code'] == '8') | (df['cleaned_product_code'] == 'E') |
#                        (df['cleaned_product_code'] == 'F') | (df['cleaned_product_code'] == 'H') |
#                        (df['cleaned_product_code'] == 'J') | (df['cleaned_product_code'] == 'M') |
#                        (df['cleaned_product_code'] == 'P') | (df['cleaned_product_code'] == 'Q') |
#                        (df['cleaned_product_code'] == 'V') | (df['cleaned_product_code'] == 'Y')]
