from ecom.Models.Shippment import Shippment
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import pandas as pd

conn = create_engine('sqlite:////Users/apple/Documents/dhl_ecom_plt/db/dhl.db?check_same_thread=False', echo=True)

# 建立会话
# Session = sessionmaker(bind=conn）
# session = Session()

data = pd.read_csv('../../test/test.txt', sep='|', dtype=str)
data.to_sql('ecom_test', con=conn, if_exists='append', index=False)
print(conn)
