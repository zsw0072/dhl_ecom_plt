import xlrd
import sqlite3

workbook = xlrd.open_workbook("../orgin/CAO_201909ecom_base.xlsx")
sheet = workbook.sheet_by_name("Sheet1")
conn = sqlite3.connect("../../db/dhl.db")
c = conn.cursor()
nrows = sheet.nrows
for curr_row in range(nrows):
    sd_dtm = sheet.row_values(curr_row)[0];awb_no = sheet.row_values(curr_row)[1];orig_ctry = sheet.row_values(curr_row)[2]
    orig_stn = sheet.row_values(curr_row)[3];orig_fclty = sheet.row_values(curr_row)[4];cleaned_orig_city_name = sheet.row_values(curr_row)[5]
    sd_route_id = sheet.row_values(curr_row)[6];dest_ctry = sheet.row_values(curr_row)[7];cleaned_del_zip = sheet.row_values(curr_row)[8]
    cleaned_dest_city_name = sheet.row_values(curr_row)[9];shacct_no = sheet.row_values(curr_row)[10];billing_acct_no = sheet.row_values(curr_row)[11]
    ship_ref = sheet.row_values(curr_row)[12];piece_no = sheet.row_values(curr_row)[13];eShipperCompany = sheet.row_values(curr_row)[14]
    eShipperContact = sheet.row_values(curr_row)[15];eShipperAddress1 = sheet.row_values(curr_row)[16];eShipperAddress2 = sheet.row_values(curr_row)[17];
    eShipperAddress3 = sheet.row_values(curr_row)[18];eShipperZip = sheet.row_values(curr_row)[19];eshipperCity = sheet.row_values(curr_row)[20];
    eShipperState = sheet.row_values(curr_row)[21];eshipperPhone = sheet.row_values(curr_row)[22];eshipperFax = sheet.row_values(curr_row)[23]
    esignName = sheet.row_values(curr_row)[24];esiteid = sheet.row_values(curr_row)[25];eclientVer = sheet.row_values(curr_row)[26];eclientApp = sheet.row_values(curr_row)[27]
    cSales_cd = sheet.row_values(curr_row)[28];csegment = sheet.row_values(curr_row)[20];csale_route = sheet.row_values(curr_row)[30];copen_date = sheet.row_values(curr_row)[31]
    cname = sheet.row_values(curr_row)[32];cstation = sheet.row_values(curr_row)[33];msales_name = sheet.row_values(curr_row)[34]
    mAcctatt = sheet.row_values(curr_row)[35];mchannel = sheet.row_values(curr_row)[36];marea = sheet.row_values(curr_row)[37];mcluster = sheet.row_values(curr_row)[38]
    mroute_name = sheet.row_values(curr_row)[39];mghost = sheet.row_values(curr_row)[40];meCOM = sheet.row_values(curr_row)[41];mopms = sheet.row_values(curr_row)[42]
    cntOfErr = sheet.row_values(curr_row)[43];errMemo = sheet.row_values(curr_row)[44];message_create_dtm_ecom = sheet.row_values(curr_row)[45]
    Montime = sheet.row_values(curr_row)[46];exemptEFR = sheet.row_values(curr_row)[47];cleaned_product_code = sheet.row_values(curr_row)[48];
    billing_acct_no_ctry = sheet.row_values(curr_row)[49];ezsite_authorizing = sheet.row_values(curr_row)[50];extra_charge = sheet.row_values(curr_row)[51];PLT = sheet.row_values(curr_row)[52];
    EshipMI = sheet.row_values(curr_row)[53];plt_account = sheet.row_values(curr_row)[54];
    c.execute("INSERT INTO ecom_base_201909 VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, \
              ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
              (sd_dtm,awb_no,orig_ctry,orig_stn,orig_fclty,cleaned_orig_city_name,sd_route_id,dest_ctry,
               cleaned_del_zip,cleaned_dest_city_name,shacct_no,billing_acct_no,ship_ref,piece_no,eShipperCompany,
               eShipperContact,eShipperAddress1,eShipperAddress2,eShipperAddress3,eShipperZip,eshipperCity,eShipperState,
               eshipperPhone,eshipperFax,esignName,esiteid,eclientVer,eclientApp,cSales_cd,csegment,csale_route,copen_date,
               cname,cstation,msales_name,mAcctatt,mchannel,marea,mcluster,mroute_name,mghost,meCOM,mopms,cntOfErr,errMemo,
               message_create_dtm_ecom,Montime,exemptEFR,cleaned_product_code,billing_acct_no_ctry,ezsite_authorizing,extra_charge,PLT,EshipMI,plt_account))

conn.commit()
conn.close()





