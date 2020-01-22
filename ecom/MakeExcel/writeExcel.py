import xlwt
import sqlite3

list = ['All PLT', '2019', '60', '96', '2019(除领添)', '60(除领添)', '96(除领添)', 'OPS', 'GZW', 'GZH', 'GZP', 'GZE',
        'GZS', 'FON', 'FOS', 'ZHQ', 'NNG', 'ZHA', 'HKE', '郭靖', '于慧显', '黄懿徽', '林煜', '谢琳', '郭光澈', '方耀祺（代）',
        '陈欣', '黎凯伦','GZA', 'GZB', 'GZC', 'GZG+GDA', 'GZD', 'GZF', 'GWC', 'GWE', 'GWF',
        'GWG', 'GWH', 'GEB', 'GEC', 'GED', 'GEE', 'GEF', 'GPO', 'GPB', 'GPC', 'GPD', 'GPE', 'GHB', 'GHC', 'GHD', 'GHE',
        'FNE', 'FNF', 'FNH', 'FNK', 'ZQC', 'NNB', 'FSA', 'FSB', 'FSC', 'FSD', 'HAC', 'ZHC', 'GEO', 'GEN+GWN', 'GWO',
        'GWQ', 'GZV+GWS', 'GZY', 'FNM', 'FSY+FNN', 'FSV', 'GPU', 'GHP', 'GHO+GPR', 'GHT+GPV+F12+FNP+NNK+ZQF+HAI+ZHL',
        'GWT+GZU+GET']


def writeExcel(month):
    conn = sqlite3.connect('db/dhl.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ecom_plt_monthly where e_month =" + month)

    # 创建 workbook 对象
    workbook = xlwt.Workbook()

    # 制定单元格格式是 '0.00%',红色,加粗
    style = xlwt.XFStyle()
    font1 = xlwt.Font()
    font1.colour_index = 8
    font1.bold = True
    style.font = font1
    style.num_format_str = '0.00%'

    # 建立Sheet
    sheet = workbook.add_sheet('PLT')

    row = sheet.row(0)
    row.write(0, "All PLT")
    row.write(1, month + "占比")
    for res in cursor:
        for x in range(1, len(res)):
            row = sheet.row(x)
            row.write(0, list[x])
            row.write(1, res[x], style)

    workbook.save("report/ecom_plt_" + month + ".xls")
