import pandas as pd
import numpy as np
import sqlite3


def createPivotTable(month):
    conn = sqlite3.connect('../../db/dhl.db')

    # expect FOC CASH account and select non-doc
    sql = "SELECT awb_no,orig_fclty,shacct_no,eShipperCompany,esiteid,eclientApp,cleaned_product_code,PLT FROM ecom_base_" + month + " \
           WHERE shacct_no NOT LIKE 'F%' AND shacct_no NOT LIKE 'C%' AND shacct_no NOT LIKE '';"
    df = pd.read_sql(sql, conn)
    data = df.loc[(df['cleaned_product_code'].isin(['3', '4', '8', 'E', 'F', 'H', 'J', 'M', 'P', 'Q', 'V', 'Y']))]

    # selsct MyDHL API \XMLPI  waybill and select ESHIP waybill
    data1 = data.loc[data['eclientApp'].isin(['MyDHL API', 'XMLPI', 'eCom WayForward'])]
    data2 = data.loc[data['esiteid'] == 'PEK0000009055SPS']

    # append the result
    xmlAndPltResult = data1.append(data2)
    preAccResult = xmlAndPltResult.loc[xmlAndPltResult['shacct_no'].str.startswith('60')]
    impAccResult = xmlAndPltResult.loc[(xmlAndPltResult['shacct_no'].str.startswith('95')) | (xmlAndPltResult['shacct_no'].str.startswith('96'))]

    # create pivot table by shacct_no, svc, company, eclientapp, PLT
    xmlAndPlt_table = pd.pivot_table(xmlAndPltResult, index=['shacct_no', 'orig_fclty', 'esiteid', 'eclientApp', 'PLT'],
                           values=['awb_no'],
                           aggfunc=[np.count_nonzero])
    print(xmlAndPlt_table)

    preAcc_table = pd.pivot_table(preAccResult, index=['shacct_no', 'orig_fclty', 'esiteid', 'eclientApp', 'PLT'],
                           values=['awb_no'],
                           aggfunc=[np.count_nonzero])
    print(preAcc_table)


    impAcc_table = pd.pivot_table(impAccResult, index=['shacct_no', 'orig_fclty', 'esiteid', 'eclientApp', 'PLT'],
                           values=['awb_no'],
                           aggfunc=[np.count_nonzero])
    print(impAcc_table)

    # print(table)
    # to repeat all label used the to_csv method
    xmlAndPlt_table.to_csv('../report/ESHIP and XMLPI PLT Report '+month+'.csv')
    preAcc_table.to_csv('../report/Pre PLT Report '+month+'.csv')
    impAcc_table.to_csv('../report/IMP PLT Report '+month+'.csv')



createPivotTable('201909')
