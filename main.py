from ecom.ClarAll.GroupAllPLT import *
from ecom.ClarAll.CalrAll import *
from ecom.MakeExcel.writeExcel import *
from ecom.DbControl.InsertShippment import *
from ecom.ClarAll.ClarAndWrite import *

month = '201912'

# 0....导入数据
# insertShipment("201912")

# 1....计算所有路区、销售百分比并写入到表ecom_plt_monthly
calrAndWrite(month)

# 2....计算60,95/96账号PLT使用情况并分别写出文件
#groupAllPLT(month)
