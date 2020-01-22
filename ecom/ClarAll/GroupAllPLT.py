import pandas as pd
import numpy as np
import sqlite3


def groupAllPLT(month):
	conn = sqlite3.connect('db/dhl.db')

	# expect FOC CASH account and select non-doc
	sql = "SELECT awb_no,orig_fclty,shacct_no,billing_acct_no,eShipperCompany,esiteid,eclientApp,cSales_cd,cleaned_product_code,PLT FROM ecom_base_" + month + " \
           WHERE shacct_no NOT LIKE 'F%' AND shacct_no NOT LIKE '';"
	df = pd.read_sql(sql, conn)
	data = df.loc[(df['cleaned_product_code'].isin(['3', '4', '8', 'E', 'F', 'H', 'J', 'M', 'P', 'Q', 'V', 'Y']))]

	# selsct MyDHL API \XMLPI  waybill and select ESHIP waybill
	data1 = data.loc[data['eclientApp'].isin(['MyDHL API', 'XMLPI'])]
	data2 = data.loc[data['esiteid'] == 'PEK0000009055SPS']

	# append the result
	xmlAndPltResult = data1.append(data2)

	# filter the dataframe by prepay account and import account
	preAccResult = xmlAndPltResult.loc[xmlAndPltResult['shacct_no'].str.startswith('60')]
	impAccResult = xmlAndPltResult.loc[
		(xmlAndPltResult['shacct_no'].str.startswith('95')) | (xmlAndPltResult['shacct_no'].str.startswith('96'))]
	# replace value:PEK0000009055SPS to DDHLCNESHIPC
	preAccResult['esiteid'] = preAccResult['esiteid'].replace('PEK0000009055SPS', 'DDHLCNESHIPC')

	# sort_index = sort the rows by indexs
	# sort_values = sort the rows by values
	# rename = rename the index name
	# reset_index reset the index to 0,1,2,3... True: drop the old index, False keep the old index on
	# in groupby(), 'shacct_no','esiteid' are indices, agg() args is values like 'awb_no'
	# map() change the int to str
	# the column has returned the str, and we must use sum() method
	preAccAll = preAccResult.groupby(['shacct_no', 'esiteid', 'PLT']).agg(
		{'awb_no': np.size, 'billing_acct_no': lambda x: x.map(str).str.startswith('60').sum()})
	print(preAccAll, type(preAccAll))

	bb = preAccResult.groupby(['shacct_no', 'billing_acct_no']).agg(
		{'esiteid': 'first', 'PLT': 'first',
		 'awb_no': np.size})
	print(bb, type(bb))

	impAcc = impAccResult.groupby(['shacct_no', 'orig_fclty', 'esiteid', 'eclientApp', 'PLT']).count()
	# print(impAcc)

	# to repeat all label used the to_csv method
	# xmlAndPlt.to_csv('report/ESHIP and XMLPI PLT Report ' + month + '.csv', header=True)
	preAccAll.to_csv('report/Pre PLT Report ' + month + 'test1.csv', header=True)
	bb.to_csv('report/Pre PLT Report ' + month + 'test2.csv', header=True)
	# impAcc.to_csv('report/IMP PLT Report ' + month + '.csv', header=True)
