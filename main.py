from ecom.ClarAll.GroupAllPLT import *
from ecom.ClarAll.CalrAll import *
from ecom.MakeExcel.writeExcel import *
from ecom.DbControl.InsertShippment import *

# 0....导入数据
# insertShipment("201912")

# 1....计算所有路区、销售百分比并写入到表ecom_plt_monthly
calrAll("201912")

# 2....写入到文件ecom_report
# writeExcel("201912")

# 3....计算60,95/96账号PLT使用情况并分别写出文件
# groupAllPLT('201912')
