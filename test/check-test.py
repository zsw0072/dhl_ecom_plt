import sqlite3

conn = sqlite3.connect("C:\\Users\\admin\\Desktop\\dhl_ecom_plt\\db\\dhl.db")
all_awb_result = conn.execute("SELECT COUNT(*) FROM ecom_base_201909").fetchone()[0]
plt_awb_result = conn.execute("SELECT COUNT(*) FROM ecom_base_201909 WHERE PLT = 'Y'").fetchone()[0]
plt_awb_total = plt_awb_result / all_awb_result
print("--------------------------")
print(all_awb_result)
print(plt_awb_result)
print("PLT占比::", plt_awb_total)
