import pandas as pd
import numpy as np
import sqlite3


def groupAllPLT(month):
    conn = sqlite3.connect('db/dhl.db')

    # expect FOC CASH account and select non-doc
    sql = "SELECT awb_no,orig_fclty,shacct_no,billing_acct_no,eShipperCompany,esiteid,eclientApp,cSales_cd,cleaned_product_code,PLT FROM shipment_" + month + " \
           WHERE shacct_no NOT LIKE 'F%' AND shacct_no NOT LIKE '';"

    df = pd.read_sql(sql, conn)
    data = df.loc[(df.cleaned_product_code.isin(['3', '4', '8', 'E', 'F', 'H', 'J', 'M', 'P', 'Q', 'V', 'Y']))]
    # select MyDHL API \ XMLPI  waybill and select ESHIP waybill
    data1 = data.loc[data.eclientApp.isin(['MyDHL API', 'XMLPI'])]
    data2 = data.loc[data.esiteid == 'PEK0000009055SPS']

    # append the result
    xmlAndPltResult = data1.append(data2)
    # replace value:PEK0000009055SPS to DDHLCNESHIPC
    xmlAndPlt = xmlAndPltResult.copy()
    xmlAndPlt.loc[xmlAndPlt.esiteid == 'PEK0000009055SPS', 'esiteid'] = 'DDHLCNESHIPC'
    xmlAndPlt['shacct_no'] = xmlAndPlt['shacct_no'].str[:8]
    # filter the dataframe by prepay account and import account
    preAccResult = xmlAndPlt.loc[xmlAndPltResult.shacct_no.str.startswith('60')]
    impAccResult = xmlAndPlt.loc[
        (xmlAndPlt.shacct_no.str.startswith('95')) | (xmlAndPltResult.shacct_no.str.startswith('96'))]

    preAccAll = preAccResult.groupby(['shacct_no']).agg(
        {'shacct_no': 'first',
         'esiteid': 'first',
         'PLT': 'first',
         'awb_no': np.size,
         'billing_acct_no': lambda x: x.map(str).str.startswith('60').sum()})
    preAccAll.rename(columns={'shacct_no': '发件人账号', 'esiteid': 'ESITEID', 'PLT': '是否为PLT', 'awb_no': '总发件量',
                              'billing_acct_no': '付款账号件量'}, inplace=True)
    preAccAll = preAccAll.reset_index(drop=True)

    impAccAll = impAccResult.groupby(['shacct_no']).agg(
        {'shacct_no': 'first',
         'orig_fclty': 'first',
         'esiteid': 'first',
         'PLT': 'first',
         'awb_no': np.size})
    impAccAll.rename(columns={'shacct_no': '发件人账号', 'orig_fclty': 'SVC', 'esiteid':
        'ESITEID', 'PLT': '是否为PLT', 'awb_no': '总发件量'}, inplace=True)
    impAccAll = impAccAll.reset_index(drop=True)

    fileName = 'ecom/Report/plt Report ' + month + '.xlsx'
    writer = pd.ExcelWriter(fileName)

    # to repeat all label used the to_csv method
    preAccAll.to_excel(writer, 'PRE', header=True, index=None, encoding='utf_8')
    impAccAll.to_excel(writer, 'IMP', header=True, index=None, encoding='utf_8')

    # must be save, the data needs fresh by writer
    writer.save()
