CREATE TABLE ecom_test(
    sd_dtm  CHAR(30),
    awb_no  CHAR(20),
    orig_ctry   CHAR(10),
    orig_stn    CHAR(10),
    orig_fclty  CHAR(10),
    cleaned_orig_city_name  CHAR(60),
    sd_route_id CHAR(10),
    dest_ctry   CHAR(10),
    cleaned_del_zip CHAR(10),
    cleaned_dest_city_name  CHAR(60),
    shacct_no   CHAR(20),
    billing_acct_no INT,
    ship_ref    CHAR(60),
    piece_no    CHAR(10),
    eShipperCompany CHAR(60),
    eShipperContact CHAR(60),
    eShipperAddress1   CHAR(90),
    eShipperAddress2    CHAR(90),
    eShipperAddress3    CHAR(90),
    eShipperZip CHAR(10),
    eshipperCity    CHAR(35),
    eShipperState   CHAR(35),
    eshipperPhone   CHAR(10),
    eshipperFax     CHAR(35),
    esignName   CHAR(35),
    esiteid     CHAR(35),
    eclientVer  CHAR(35),
    eclientApp  CHAR(35),
    cSales_cd   CHAR(10),
    csegment    CHAR(10),
    csale_route CHAR(10),
    copen_date  CHAR(10),
    cname   CHAR(90),
    cstation    CHAR(10),
    msales_name CHAR(10),
    mAcctatt    CHAR(10),
    mchannel    CHAR(20),
    marea   CHAR(10),
    mcluster CHAR(10),
    mroute_name CHAR(10),
    mghost  CHAR(10),
    meCOM   CHAR(10),
    mopms   CHAR(10),
    cntOfErr    CHAR(10),
    errMemo     CHAR(10),
    message_create_dtm_ecom REAL,
    Montime CHAR(10),
    exemptEFR   CHAR(35),
    cleaned_product_code    CHAR(5),
    billing_acct_no_ctry    CHAR(20),
    ezsite_authorizing  CHAR(5),
    extra_charge    CHAR(35),
    PLT CHAR(5),
    EshipMI int,
    plt_account int
);
