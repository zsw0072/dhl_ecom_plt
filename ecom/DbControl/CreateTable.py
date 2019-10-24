import sqlite3

file = open("/Users/apple/Documents/dhl_ecom_plt/db/create_table_ecom_base.sql", "r")
contents = file.read()
print(contents)

conn = sqlite3.connect("/Users/apple/Documents/dhl_ecom_plt/db/dhl.db")
#c = conn.cursor()
#c.execute()
