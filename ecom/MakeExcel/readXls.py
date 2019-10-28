import xlrd

workbook = xlrd.open_workbook("C:\\Users\\admin\\Desktop\\dhl_ecom_plt\\plt_report\\ecom_plt.xls")
sheet = workbook.sheet_by_name("PLT")

cols = sheet.ncols
for col in range(cols):
	print(sheet.col_values(col))
