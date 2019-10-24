import sqlite3


def calrAll(month):
    conn = sqlite3.connect("db/dhl.db")
    c = conn.cursor()
    print("-----------------------------")

    # PLT部分/ 全部运单
    all_awb = c.execute("SELECT COUNT(*) FROM ecom_base_" + month).fetchone()[0]
    plt_awb = c.execute("SELECT COUNT(*) FROM ecom_base_" + month + " WHERE PLT = 'Y'").fetchone()[0]
    plt_awb = plt_awb / all_awb
    print("PLT占比::", plt_awb)

    # 全部 60 PLT账号/全部 60账号
    prepay_acc = c.execute("SELECT COUNT(*) FROM ecom_base_" + month + " WHERE billing_acct_no LIKE '6%';").fetchone()[0]
    prepay_acc_plt = c.execute("SELECT COUNT(*) FROM ecom_base_" + month + " WHERE billing_acct_no LIKE '6%' AND PLT = 'Y';").fetchone()[0]
    pre_plt_awb = prepay_acc_plt / prepay_acc
    print("60账号PLT占比::", pre_plt_awb)

    # 全部 9596PLT账号/全部 9596账号
    imp_acc = c.execute("SELECT COUNT(*) FROM ecom_base_" + month + " WHERE billing_acct_no LIKE '9%';").fetchone()[0]
    imp_acc_plt = c.execute("SELECT COUNT(*) FROM ecom_base_" + month + " WHERE billing_acct_no LIKE '9%' AND PLT = 'Y';").fetchone()[0]
    imp_plt_awb = imp_acc_plt / imp_acc
    print("95/96账号PLT占比::", imp_plt_awb)
    print("-----------------------------")

    # PLT部分/ 全部运单 (除领添)
    all_awb1 = c.execute("SELECT COUNT(*) FROM ecom_base_" + month + " WHERE orig_fclty IS NOT 'GZD';").fetchone()[0]
    plt_awb1 = c.execute("SELECT COUNT(*) FROM ecom_base_" + month + " WHERE orig_fclty IS NOT 'GZD' AND PLT = 'Y';").fetchone()[0]
    plt_awb1 = plt_awb1 / all_awb1
    print("PLT(除领添)占比::", plt_awb1)

    # 全部 60 PLT账号/全部 60账号
    prepay_acc1 = c.execute("SELECT COUNT(*) FROM ecom_base_" + month + " WHERE orig_fclty IS NOT 'GZD' AND billing_acct_no LIKE '60%';").fetchone()[0]
    prepay_acc_plt1 = c.execute("SELECT COUNT(*) FROM ecom_base_" + month + " WHERE orig_fclty IS NOT 'GZD' AND billing_acct_no LIKE '60%' AND PLT = 'Y';").fetchone()[0]
    pre_plt_awb1 = prepay_acc_plt1 / prepay_acc1
    print("60账号(除领添)PLT占比::", pre_plt_awb1)

    # 全部 9596PLT账号/全部 9596账号
    imp_acc1 = c.execute("SELECT COUNT(*) FROM ecom_base_" + month + " WHERE billing_acct_no LIKE '9%';").fetchone()[0]
    imp_acc_plt1 = c.execute("SELECT COUNT(*) FROM ecom_base_" + month + " WHERE billing_acct_no LIKE '9%' AND PLT = 'Y';").fetchone()[0]
    imp_plt_awb1 = imp_acc_plt1 / imp_acc1
    print("95/96账号(除领添)PLT占比::", imp_plt_awb1)
    print("-----------------------------")

    # ESHIP OPS
    ops = c.execute(
        "SELECT COUNT(*) FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC';").fetchone()[0]
    ops_plt = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR 'DDHLCNESHIPC' ) WHERE PLT = 'Y';").fetchone()[0]
    ops_plt_awb = ops_plt / ops
    print("ESHIP OPS PLT占比::", ops_plt_awb)

    # ESHIP GZW
    gzw = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'GZW'").fetchone()[0]
    gzw_plt = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'GZW' AND PLT = 'Y'").fetchone()[0]
    gzw_plt_awb = gzw_plt / gzw
    print("ESHIP GZW PLT占比::", gzw_plt_awb)

    # ESHIP GZH
    gzh = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'GZH'").fetchone()[0]
    gzh_plt = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'GZH' AND PLT = 'Y'").fetchone()[0]
    gzh_plt_awb = gzh_plt / gzh
    print("ESHIP GZH PLT占比::", gzh_plt_awb)

    # ESHIP GZP
    gzp = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'GZP'").fetchone()[0]
    gzp_plt = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'GZP' AND PLT = 'Y'").fetchone()[0]
    gzp_plt_awb = gzp_plt / gzp
    print("ESHIP GZP PLT占比::", gzp_plt_awb)

    # ESHIP GZE
    gze = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'GZE'").fetchone()[0]
    gze_plt = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'GZE' AND PLT = 'Y'").fetchone()[0]
    gze_plt_awb = gze_plt / gze
    print("ESHIP GZE PLT占比::", gze_plt_awb)

    # ESHIP GZS
    gzs = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'GZS'").fetchone()[0]
    gzs_plt = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'GZS' AND PLT = 'Y'").fetchone()[0]
    gzs_plt_awb = gzs_plt / gzs
    print("ESHIP GZS PLT占比::", gzs_plt_awb)

    # ESHIP FON
    fon = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'FON'").fetchone()[0]
    fon_plt = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'FON' AND PLT = 'Y'").fetchone()[0]
    fon_plt_awb = fon_plt / fon
    print("ESHIP FON PLT占比::", fon_plt_awb)

    # ESHIP FOS
    fos = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'FOS'").fetchone()[0]
    fos_plt = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'FOS' AND PLT = 'Y'").fetchone()[0]
    fos_plt_awb = fos_plt / fos
    print("ESHIP FOS PLT占比::", fos_plt_awb)

    # ESHIP ZHQ
    zhq= c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'ZHQ'").fetchone()[0]
    zhq_plt = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'ZHQ' AND PLT = 'Y'").fetchone()[0]
    zhq_plt_awb = zhq_plt / zhq
    print("ESHIP ZHQ PLT占比::", zhq_plt_awb)

    # ESHIP NNG
    nng = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'NNG'").fetchone()[0]
    nng_plt = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'NNG' AND PLT = 'Y'").fetchone()[0]
    nng_plt_awb = nng_plt / nng
    print("ESHIP NNG PLT占比::", nng_plt_awb)

    # ESHIP ZHA
    zha = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'ZHA'").fetchone()[0]
    zha_plt = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'ZHA' AND PLT = 'Y'").fetchone()[0]
    zha_plt_awb = zha_plt / zha
    print("ESHIP ZHA PLT占比::", zha_plt_awb)

    # ESHIP HKE
    hke = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'HKE'").fetchone()[0]
    hke_plt = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE orig_fclty = 'HKE' AND PLT = 'Y'").fetchone()[0]
    hke_plt_awb = hke_plt / hke
    print("ESHIP HKE PLT占比::", hke_plt_awb)
    print("-----------------------------")

    # GZA
    gza_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZA';")
    for row in gza_total_result:
        gza_total = row[0]
    gza_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZA' AND PLT = 'Y';")
    for row in gza_plt_total_result:
        gza_plt_total = row[0]
    gza_plt = gza_plt_total / gza_total
    # print("--------------------------")
    # print("GZA Total::", gza_total)
    # print("GZA PLT Total::", gza_plt_total)
    print("GZA PLT占比::", gza_plt)

    # GZB
    gzb_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZB';")
    for row in gzb_total_result:
        gzb_total = row[0]
    gzb_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZB' AND PLT = 'Y';")
    for row in gzb_plt_total_result:
        gzb_plt_total = row[0]
    gzb_plt = gzb_plt_total / gzb_total
    # print("--------------------------")
    # print("GZB Total::", gzb_total)
    # print("GZB PLT Total::", gzb_plt_total)
    print("GZB PLT占比::", gzb_plt)

    # GZC+GDA
    gzc_gda_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZC' OR cSales_cd = 'GDA';")
    for row in gzc_gda_total_result:
        gzc_gda_total = row[0]
    gzc_gda_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZC' OR cSales_cd = 'GDA') WHERE PLT = 'Y';")
    for row in gzc_gda_plt_total_result:
        gzc_gda_plt_total = row[0]
    gzc_gda_plt = gzc_gda_plt_total / gzc_gda_total
    # print("--------------------------")
    # print("GZC+GDA Total::", gzc_gda_total)
    # print("GZC+GDA PLT Total::", gzc_gda_plt_total)
    print("GZC+GDA PLT占比::", gzc_gda_plt)

    # GZD
    gzd_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZD';")
    for row in gzd_total_result:
        gzd_total = row[0]
    gzd_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZD' AND PLT = 'Y';")
    for row in gzd_plt_total_result:
        gzd_plt_total = row[0]
    gzd_plt = gzd_plt_total / gzd_total
    # print("--------------------------")
    # print("GZD Total::", gzd_total)
    # print("GZD PLT Total::", gzd_plt_total)
    print("GZD PLT占比::", gzd_plt)

    # GZF
    gzf_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZF';")
    for row in gzf_total_result:
        gzf_total = row[0]
    gzf_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZF' AND PLT = 'Y';")
    for row in gzf_plt_total_result:
        gzf_plt_total = row[0]
    gzf_plt = gzf_plt_total / gzf_total
    # print("--------------------------")
    # print("GZF Total::", gzf_total)
    # print("GZF PLT Total::", gzf_plt_total)
    print("GZF PLT占比::", gzf_plt)

    # GWC
    gwc_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWC';")
    for row in gwc_total_result:
        gwc_total = row[0]
    gwc_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWC' AND PLT = 'Y';")
    for row in gwc_plt_total_result:
        gwc_plt_total = row[0]
    gwc_plt = gwc_plt_total / gwc_total
    # print("--------------------------")
    # print("GWC Total::", gwc_total)
    # print("GWC PLT Total::", gwc_plt_total)
    print("GWC PLT占比::", gwc_plt)

    # GWE
    gwe_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWE';")
    for row in gwe_total_result:
        gwe_total = row[0]
    gwe_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWE' AND PLT = 'Y';")
    for row in gwe_plt_total_result:
        gwe_plt_total = row[0]
    gwe_plt = gwe_plt_total / gwe_total
    # print("--------------------------")
    # print("GWE Total::", gwe_total)
    # print("GWE PLT Total::", gwe_plt_total)
    print("GWE PLT占比::", gwe_plt)

    # GWF
    gwf_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWF';")
    for row in gwf_total_result:
        gwf_total = row[0]
    gwf_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWF' AND PLT = 'Y';")
    for row in gwf_plt_total_result:
        gwf_plt_total = row[0]
    gwf_plt = gwf_plt_total / gwf_total
    # print("--------------------------")
    # print("GWF Total::", gwf_total)
    # print("GWF PLT Total::", gwf_plt_total)
    print("GWF PLT占比::", gwf_plt)

    # GWG
    gwg_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWG';")
    for row in gwg_total_result:
        gwg_total = row[0]
    gwg_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWG' AND PLT = 'Y';")
    for row in gwg_plt_total_result:
        gwg_plt_total = row[0]
    gwg_plt = gwg_plt_total / gwg_total
    # print("--------------------------")
    # print("GWG Total::", gwg_total)
    # print("GWG PLT Total::", gwg_plt_total)
    print("GWG PLT占比::", gwg_plt)

    # GWH
    gwh_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWH';")
    for row in gwh_total_result:
        gwh_total = row[0]
    gwh_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWH' AND PLT = 'Y';")
    for row in gwh_plt_total_result:
        gwh_plt_total = row[0]
    gwh_plt = gwh_plt_total / gwh_total
    # print("--------------------------")
    # print("GWH Total::", gwh_total)
    # print("GWH PLT Total::", gwh_plt_total)
    print("GWH PLT占比::", gwh_plt)

    # GEB
    geb_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GEB';")
    for row in geb_total_result:
        geb_total = row[0]
    geb_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GEB' AND PLT = 'Y';")
    for row in geb_plt_total_result:
        geb_plt_total = row[0]
    geb_plt = geb_plt_total / geb_total
    # print("--------------------------")
    # print("GEB Total::", geb_total)
    # print("GEB PLT Total::", geb_plt_total)
    print("GEB PLT占比::", geb_plt)

    # GEC
    geC_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GEC';")
    for row in geC_total_result:
        geC_total = row[0]
    geC_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GEC' AND PLT = 'Y';")
    for row in geC_plt_total_result:
        geC_plt_total = row[0]
    geC_plt = geC_plt_total / geC_total
    # print("--------------------------")
    # print("GEC Total::", geC_total)
    # print("GEC PLT Total::", geC_plt_total)
    print("GEC PLT占比::", geC_plt)

    # GED
    ged_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GED';")
    for row in ged_total_result:
        ged_total = row[0]
    ged_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GED' AND PLT = 'Y';")
    for row in ged_plt_total_result:
        ged_plt_total = row[0]
    ged_plt = ged_plt_total / ged_total
    # print("--------------------------")
    # print("GED Total::", ged_total)
    # print("GED PLT Total::", ged_plt_total)
    print("GED PLT占比::", ged_plt)

    # GEE
    gee_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GEE';")
    for row in gee_total_result:
        gee_total = row[0]
    gee_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GEE' AND PLT = 'Y';")
    for row in gee_plt_total_result:
        gee_plt_total = row[0]
    gee_plt = gee_plt_total / gee_total
    # print("--------------------------")
    # print("GEE Total::", gee_total)
    # print("GEE PLT Total::", gee_plt_total)
    print("GEE PLT占比::", gee_plt)

    # GEF
    gef_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GEF';")
    for row in gef_total_result:
        gef_total = row[0]
    gef_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GEF' AND PLT = 'Y';")
    for row in gef_plt_total_result:
        gef_plt_total = row[0]
    gef_plt = gef_plt_total / gef_total
    # print("--------------------------")
    # print("GEF Total::", gef_total)
    # print("GEF PLT Total::", gef_plt_total)
    print("GEF PLT占比::", gef_plt)

    # GPO
    gpo_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GPO';")
    for row in gpo_total_result:
        gpo_total = row[0]
    gpo_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GPO' AND PLT = 'Y';")
    for row in gpo_plt_total_result:
        gpo_plt_total = row[0]
    gpo_plt = gpo_plt_total / gpo_total
    # print("--------------------------")
    # print("GPO Total::", gpo_total)
    # print("GPO PLT Total::", gpo_plt_total)
    print("GPO PLT占比::", gpo_plt)

    # tba_total_result = c.execute("SELECT COUNT(*) FROM ecom_base_"+month+" WHERE cSales_cd = 'GPP'")
    #     # for row in tba_total_result:
    #     #     tba_total = row[0]
    #     # tba_plt_total_result = c.execute("SELECT COUNT(*) FROM ecom_base_"+month+" WHERE cSales_cd = 'GPP' AND PLT = 'Y'")
    #     # for row in tba_plt_total_result:
    #     #     tba_plt_total = row[0]
    #     #
    #     # tba_plt = tba_plt_total / tba_total
    #     # if tba_plt == 0:
    #     #     pass
    #     # print("--------------------------")
    #     # print("TBA Total::", tba_total)
    #     # print("TBA PLT Total::", tba_plt_total)
    #     # print("TBA PLT占比::", tba_plt)

    # GPB
    gpb_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GPB';")
    for row in gpb_total_result:
        gpb_total = row[0]
    gpb_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GPB' AND PLT = 'Y';")
    for row in gpb_plt_total_result:
        gpb_plt_total = row[0]
    gpb_plt = gpb_plt_total / gpb_total
    # print("--------------------------")
    # print("GPB Total::", gpb_total)
    # print("GPB PLT Total::", gpb_plt_total)
    print("GPB PLT占比::", gpb_plt)

    # GPC
    gpc_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GPC';")
    for row in gpc_total_result:
        gpc_total = row[0]
    gpc_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GPC' AND PLT = 'Y';")
    for row in gpc_plt_total_result:
        gpc_plt_total = row[0]
    gpc_plt = gpc_plt_total / gpc_total
    # print("--------------------------")
    # print("GPC Total::", gpc_total)
    # print("GPC PLT Total::", gpc_plt_total)
    print("GPC PLT占比::", gpc_plt)

    # GPD
    gpd_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GPD';")
    for row in gpd_total_result:
        gpd_total = row[0]
    gpd_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GPD' AND PLT = 'Y';")
    for row in gpd_plt_total_result:
        gpd_plt_total = row[0]
    gpd_plt = gpd_plt_total / gpd_total
    # print("--------------------------")
    # print("GPD Total::", gpd_total)
    # print("GPD PLT Total::", gpd_plt_total)
    print("GPD PLT占比::", gpd_plt)

    # GPE
    gpe_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GPE';")
    for row in gpe_total_result:
        gpe_total = row[0]
    gpe_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GPE' AND PLT = 'Y';")
    for row in gpe_plt_total_result:
        gpe_plt_total = row[0]
    gpe_plt = gpe_plt_total / gpe_total
    # print("--------------------------")
    # print("GPE Total::", gpe_total)
    # print("GPE PLT Total::", gpe_plt_total)
    print("GPE PLT占比::", gpe_plt)

    # GHB
    ghb_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHB';")
    for row in ghb_total_result:
        ghb_total = row[0]
    ghb_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHB' AND PLT = 'Y';")
    for row in ghb_plt_total_result:
        ghb_plt_total = row[0]
    ghb_plt = ghb_plt_total / ghb_total
    # print("--------------------------")
    # print("GHB Total::", ghb_total)
    # print("GHB PLT Total::", ghb_plt_total)
    print("GHB PLT占比::", ghb_plt)

    # GHC
    ghc_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHC';")
    for row in ghc_total_result:
        ghc_total = row[0]
    ghc_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHC' AND PLT = 'Y';")
    for row in ghc_plt_total_result:
        ghc_plt_total = row[0]
    ghc_plt = ghc_plt_total / ghc_total
    # print("--------------------------")
    # print("GHC Total::", ghc_total)
    # print("GHC PLT Total::", ghc_plt_total)
    print("GHC PLT占比::", ghc_plt)

    # GHD
    ghd_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHD';")
    for row in ghd_total_result:
        ghd_total = row[0]
    ghd_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHD' AND PLT = 'Y';")
    for row in ghd_plt_total_result:
        ghd_plt_total = row[0]
    ghd_plt = ghd_plt_total / ghd_total
    # print("--------------------------")
    # print("GHD Total::", ghd_total)
    # print("GHD PLT Total::", ghd_plt_total)
    print("GHD PLT占比::", ghd_plt)

    # GHE
    ghe_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHE';")
    for row in ghe_total_result:
        ghe_total = row[0]
    ghe_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHE' AND PLT = 'Y';")
    for row in ghe_plt_total_result:
        ghe_plt_total = row[0]
    ghe_plt = ghe_plt_total / ghe_total
    # print("--------------------------")
    # print("GHE Total::", ghe_total)
    # print("GHE PLT Total::", ghe_plt_total)
    print("GHE PLT占比::", ghe_plt)

    # FNE
    fne_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FNE';")
    for row in fne_total_result:
        fne_total = row[0]
    fne_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FNE' AND PLT = 'Y';")
    for row in fne_plt_total_result:
        fne_plt_total = row[0]
    fne_plt = fne_plt_total / fne_total
    # print("--------------------------")
    # print("FNE Total::", fne_total)
    # print("FNE PLT Total::", fne_plt_total)
    print("FNE PLT占比::", fne_plt)

    # FNF
    fnf_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FNF';")
    for row in fnf_total_result:
        fnf_total = row[0]
    fnf_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FNF' AND PLT = 'Y';")
    for row in fnf_plt_total_result:
        fnf_plt_total = row[0]
    fnf_plt = fnf_plt_total / fnf_total
    # print("--------------------------")
    # print("FNF Total::", fnf_total)
    # print("FNF PLT Total::", fnf_plt_total)
    print("FNF PLT占比::", fnf_plt)

    # FNH
    fnh_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FNH';")
    for row in fnh_total_result:
        fnh_total = row[0]
    fnh_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FNH' AND PLT = 'Y';")
    for row in fnh_plt_total_result:
        fnh_plt_total = row[0]
    fnh_plt = fnh_plt_total / fnh_total
    # print("--------------------------")
    # print("FNH Total::", fnh_total)
    # print("FNH PLT Total::", fnh_plt_total)
    print("FNH PLT占比::", fnh_plt)

    # FNK
    fnk_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FNK';")
    for row in fnk_total_result:
        fnk_total = row[0]
    fnk_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FNK' AND PLT = 'Y';")
    for row in fnk_plt_total_result:
        fnk_plt_total = row[0]
    fnk_plt = fnk_plt_total / fnk_total
    # print("--------------------------")
    # print("FNK Total::", fnk_total)
    # print("FNK PLT Total::", fnk_plt_total)
    print("FNK PLT占比::", fnk_plt)

    # ZQC
    zqc_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'ZQC';")
    for row in zqc_total_result:
        zqc_total = row[0]
    zqc_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'ZQC' AND PLT = 'Y';")
    for row in zqc_plt_total_result:
        zqc_plt_total = row[0]
    zqc_plt = zqc_plt_total / zqc_total
    # print("--------------------------")
    # print("ZQC Total::", zqc_total)
    # print("ZQC PLT Total::", zqc_plt_total)
    print("ZQC PLT占比::", zqc_plt)

    # NNB
    nnb_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'NNB';")
    for row in nnb_total_result:
        nnb_total = row[0]
    nnb_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'NNB' AND PLT = 'Y';")
    for row in nnb_plt_total_result:
        nnb_plt_total = row[0]
    nnb_plt = nnb_plt_total / nnb_total
    # print("--------------------------")
    # print("NNB Total::", nnb_total)
    # print("NNB PLT Total::", nnb_plt_total)
    print("NNB PLT占比::", nnb_plt)

    # FSA
    fsa_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FSA';")
    for row in fsa_total_result:
        fsa_total = row[0]
    fsa_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FSA' AND PLT = 'Y';")
    for row in fsa_plt_total_result:
        fsa_plt_total = row[0]
    fsa_plt = fsa_plt_total / fsa_total
    # print("--------------------------")
    # print("FSA Total::", fsa_total)
    # print("FSA PLT Total::", fsa_plt_total)
    print("FSA PLT占比::", fsa_plt)

    # FSB
    fsb_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FSB';")
    for row in fsb_total_result:
        fsb_total = row[0]
    fsb_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FSB' AND PLT = 'Y';")
    for row in fsb_plt_total_result:
        fsb_plt_total = row[0]
    fsb_plt = fsb_plt_total / fsb_total
    # print("--------------------------")
    # print("FSB Total::", fsb_total)
    # print("FSB PLT Total::", fsb_plt_total)
    print("FSB PLT占比::", fsb_plt)

    # FSC
    fsc_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FSC';")
    for row in fsc_total_result:
        fsc_total = row[0]
    fsc_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FSC' AND PLT = 'Y';")
    for row in fsc_plt_total_result:
        fsc_plt_total = row[0]
    fsc_plt = fsc_plt_total / fsc_total
    # print("--------------------------")
    # print("FSC Total::", fsc_total)
    # print("FSC PLT Total::", fsc_plt_total)
    print("FSC PLT占比::", fsc_plt)

    # FSD
    fsd_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FSD';")
    for row in fsd_total_result:
        fsd_total = row[0]
    fsd_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FSD' AND PLT = 'Y';")
    for row in fsd_plt_total_result:
        fsd_plt_total = row[0]
    fsd_plt = fsd_plt_total / fsd_total
    # print("--------------------------")
    # print("FSD Total::", fsd_total)
    # print("FSD PLT Total::", fsd_plt_total)
    print("FSD PLT占比::", fsd_plt)

    # HAC
    hac_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'HAC';")
    for row in hac_total_result:
        hac_total = row[0]
    hac_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'HAC' AND PLT = 'Y';")
    for row in hac_plt_total_result:
        hac_plt_total = row[0]
    hac_plt = hac_plt_total / hac_total
    # print("--------------------------")
    # print("HAC Total::", hac_total)
    # print("HAC PLT Total::", hac_plt_total)
    print("HAC PLT占比::", hac_plt)

    # ZHC
    zhc_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'ZHC';")
    for row in zhc_total_result:
        zhc_total = row[0]
    zhc_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'ZHC' AND PLT = 'Y';")
    for row in zhc_plt_total_result:
        zhc_plt_total = row[0]
    zhc_plt = zhc_plt_total / zhc_total
    # print("--------------------------")
    # print("ZHC Total::", zhc_total)
    # print("ZHC PLT Total::", zhc_plt_total)
    print("ZHC PLT占比::", zhc_plt)

    # GEO
    geo_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GEO';")
    for row in geo_total_result:
        geo_total = row[0]
    geo_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GEO' AND PLT = 'Y';")
    for row in geo_plt_total_result:
        geo_plt_total = row[0]
    geo_plt = geo_plt_total / geo_total
    # print("--------------------------")
    # print("GEO Total::", geo_total)
    # print("GEO PLT Total::", geo_plt_total)
    print("GEO PLT占比::", geo_plt)

    # GEN+GWN
    gen_gwn_gda_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GEN' OR cSales_cd = 'GWN';")
    for row in gen_gwn_gda_total_result:
        gen_gwn_gda_total = row[0]
    gen_gwn_gda_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GEN' OR cSales_cd = 'GWN') WHERE PLT = 'Y';")
    for row in gen_gwn_gda_plt_total_result:
        gen_gwn_gda_plt_total = row[0]
    gen_gwn_gda_plt = gen_gwn_gda_plt_total / gen_gwn_gda_total
    # print("--------------------------")
    # print("GEN+GWN Total::", gen_gwn_gda_total)
    # print("GEN+GWN PLT Total::", gen_gwn_gda_plt_total)
    print("GEN+GWN PLT占比::", gen_gwn_gda_plt)

    # GWO
    gwo_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWO';")
    for row in gwo_total_result:
        gwo_total = row[0]
    gwo_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWO' AND PLT = 'Y';")
    for row in gwo_plt_total_result:
        gwo_plt_total = row[0]
    gwo_plt = gwo_plt_total / gwo_total
    # print("--------------------------")
    # print("GWO Total::", gwo_total)
    # print("GWO PLT Total::", gwo_plt_total)
    print("GWO PLT占比::", gwo_plt)

    # GWQ
    gwq_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWQ';")
    for row in gwq_total_result:
        gwq_total = row[0]
    gwq_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWQ' AND PLT = 'Y';")
    for row in gwq_plt_total_result:
        gwq_plt_total = row[0]
    gwq_plt = gwq_plt_total / gwq_total
    # print("--------------------------")
    # print("GWQ Total::", gwq_total)
    # print("GWQ PLT Total::", gwq_plt_total)
    print("GWQ PLT占比::", gwq_plt)

    # GZV+GWS
    gzv_gws_gda_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZV' OR cSales_cd = 'GWS';")
    for row in gzv_gws_gda_total_result:
        gzv_gws_gda_total = row[0]
    gzv_gws_gda_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZV' OR cSales_cd = 'GWS') WHERE PLT = 'Y';")
    for row in gzv_gws_gda_plt_total_result:
        gzv_gws_gda_plt_total = row[0]
    gzv_gws_gda_plt = gzv_gws_gda_plt_total / gzv_gws_gda_total
    # print("--------------------------")
    # print("GZV+GWS Total::", gzv_gws_gda_total)
    # print("GZV+GWS PLT Total::", gzv_gws_gda_plt_total)
    print("GZV+GWS PLT占比::", gzv_gws_gda_plt)

    # GZY
    gzy_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZY';")
    for row in gzy_total_result:
        gzy_total = row[0]
    gzy_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GZY' AND PLT = 'Y';")
    for row in gzy_plt_total_result:
        gzy_plt_total = row[0]
    gzy_plt = gzy_plt_total / gzy_total
    # print("--------------------------")
    # print("GZY Total::", gzy_total)
    # print("GZY PLT Total::", gzy_plt_total)
    print("GZY PLT占比::", gzy_plt)

    # FNM
    fnm_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FNM';")
    for row in fnm_total_result:
        fnm_total = row[0]
    fnm_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FNM' AND PLT = 'Y';")
    for row in fnm_plt_total_result:
        fnm_plt_total = row[0]
    fnm_plt = fnm_plt_total / fnm_total
    # print("--------------------------")
    # print("FNM Total::", fnm_total)
    # print("FNM PLT Total::", fnm_plt_total)
    print("FNM PLT占比::", fnm_plt)

    # FSY+FNN
    fsy_fnn_gda_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FSY' OR cSales_cd = 'FNN';")
    for row in fsy_fnn_gda_total_result:
        fsy_fnn_gda_total = row[0]
    fsy_fnn_gda_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FSY' OR cSales_cd = 'FNN') WHERE PLT = 'Y';")
    for row in fsy_fnn_gda_plt_total_result:
        fsy_fnn_gda_plt_total = row[0]
    fsy_fnn_gda_plt = fsy_fnn_gda_plt_total / fsy_fnn_gda_total
    # print("--------------------------")
    # print("FSY+FNN Total::", fsy_fnn_gda_total)
    # print("FSY+FNN PLT Total::", fsy_fnn_gda_plt_total)
    print("FSY+FNN PLT占比::", fsy_fnn_gda_plt)

    # FSV
    fsv_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FSV';")
    for row in fsv_total_result:
        fsv_total = row[0]
    fsv_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'FSV' AND PLT = 'Y';")
    for row in fsv_plt_total_result:
        fsv_plt_total = row[0]
    fsv_plt = fsv_plt_total / fsv_total
    # print("--------------------------")
    # print("FSV Total::", fsv_total)
    # print("FSV PLT Total::", fsv_plt_total)
    print("FSV PLT占比::", fsv_plt)

    # GPU
    gpu_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GPU';")
    for row in gpu_total_result:
        gpu_total = row[0]
    gpu_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GPU' AND PLT = 'Y';")
    for row in gpu_plt_total_result:
        gpu_plt_total = row[0]
    gpu_plt = gpu_plt_total / gpu_total
    # print("--------------------------")
    # print("GPU Total::", gpu_total)
    # print("GPU PLT Total::", gpu_plt_total)
    print("GPU PLT占比::", gpu_plt)

    # GHP
    ghp_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHP';")
    for row in ghp_total_result:
        ghp_total = row[0]
    ghp_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHP' AND PLT = 'Y';")
    for row in ghp_plt_total_result:
        ghp_plt_total = row[0]
    ghp_plt = ghp_plt_total / ghp_total
    # print("--------------------------")
    # print("GHP Total::", ghp_total)
    # print("GHP PLT Total::", ghp_plt_total)
    print("GHP PLT占比::", ghp_plt)

    # GHO+GPR
    siting_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHO' OR cSales_cd = 'GPR';")
    for row in siting_total_result:
        siting_total = row[0]
    siting_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHO' OR cSales_cd = 'GPR') WHERE PLT = 'Y';")
    for row in siting_plt_total_result:
        siting_plt_total = row[0]
    gho_gpr = siting_plt_total / siting_total
    # print("--------------------------")
    # print("GHO+GPR Total::", siting_total)
    # print("GHO+GPR PLT Total::", siting_plt_total)
    print("GHO+GPR PLT占比::", gho_gpr)

    # GHT+GPV+F12+FNP+NNK+ZQF+HAI+ZHL
    moji_total_result = c.execute(
        "	SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHT' OR cSales_cd = 'GPV' OR cSales_cd = 'F12' OR cSales_cd = 'FNP' OR cSales_cd = 'NNK' OR cSales_cd = 'ZQF' OR cSales_cd = 'HAI' OR cSales_cd = 'ZHL';")
    for row in moji_total_result:
        moji_total = row[0]
    moji_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GHT' OR cSales_cd = 'GPV' OR cSales_cd = 'F12' OR cSales_cd = 'FNP' OR cSales_cd = 'NNK' OR cSales_cd = 'ZQF' OR cSales_cd = 'HAI' OR cSales_cd = 'ZHL') WHERE PLT = 'Y';")
    for row in moji_plt_total_result:
        moji_plt_total = row[0]
    moji_plt = moji_plt_total / moji_total
    # print("--------------------------")
    # print("GHT+GPV+F12+FNP+NNK+ZQF+HAI+ZHL+L105 Total::", moji_total)
    # print("GHT+GPV+F12+FNP+NNK+ZQF+HAI+ZHL+L105 PLT Total::", moji_plt_total)
    print("GHT+GPV+F12+FNP+NNK+ZQF+HAI+ZHL PLT占比::", moji_plt)

    # GWT+GZU+GET
    yaying_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWT' OR cSales_cd = 'GZU' OR cSales_cd = 'GET';")
    for row in yaying_total_result:
        yaying_total = row[0]
    yaying_plt_total_result = c.execute(
        "SELECT COUNT(*) FROM (SELECT * FROM (SELECT * FROM ecom_base_" + month + " WHERE esiteid = 'PEK0000009055SPS' OR esiteid = 'DDHLCNESHIPC') WHERE cSales_cd = 'GWT' OR cSales_cd = 'GZU' OR cSales_cd = 'GET') WHERE PLT = 'Y';")
    for row in yaying_plt_total_result:
        yaying_plt_total = row[0]
    yaying_plt = yaying_plt_total / yaying_total
    # print("--------------------------")
    # print("GWT+GZU+GET Total::", yaying_total)
    # print("GWT+GZU+GET PLT Total::", yaying_plt_total)
    print("GWT+GZU+GET PLT占比::", yaying_plt)
    print("-----------------------------")

    c.execute(
        "INSERT INTO ecom_plt_monthly VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,\
        ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (month, plt_awb, pre_plt_awb, imp_plt_awb,plt_awb1, pre_plt_awb1, imp_plt_awb1, ops_plt_awb,
         gzw_plt_awb, gzh_plt_awb, gzp_plt_awb,gze_plt_awb, gzs_plt_awb, fon_plt_awb, fos_plt_awb,
         zhq_plt_awb, nng_plt_awb, zha_plt_awb, hke_plt_awb,gza_plt, gzb_plt, gzc_gda_plt, gzd_plt, gzf_plt,
         gwc_plt, gwe_plt, gwf_plt, gwg_plt, gwh_plt,geb_plt, geC_plt, ged_plt, gee_plt, gef_plt,gpo_plt,
         gpb_plt, gpc_plt, gpd_plt, gpe_plt,ghb_plt, ghc_plt, ghd_plt, ghe_plt, fne_plt,fnf_plt, fnh_plt,
         fnk_plt, zqc_plt, nnb_plt,fsa_plt, fsb_plt, fsc_plt, fsd_plt, hac_plt,zhc_plt, geo_plt, gen_gwn_gda_plt,
         gwo_plt, gwq_plt,gzv_gws_gda_plt, gzy_plt, fnm_plt, fsy_fnn_gda_plt,fsv_plt, gpu_plt, ghp_plt, gho_gpr, moji_plt, yaying_plt))

    conn.commit()
    conn.close()
