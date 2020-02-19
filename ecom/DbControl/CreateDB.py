from sqlalchemy import create_engine
from ecom.Models.Shippment import Shippment

# echo=True----echo默认为False，表示不打印执行的SQL语句等较详细的执行信息，改为Ture表示让其打印。
conn = create_engine('sqlite:////Users/apple/Documents/dhl_ecom_plt/db/dhl.db?check_same_thread=False', echo=True)

# 查看映射对应的表
Shippment.__tablename__
# 创建数据表
Shippment.metadata.create_all(conn)


