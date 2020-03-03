import sqlite3
import pandas as pd
import xlwt
from ecom.Models.Item import Item


def calrAndWrite(month):
    # pandas load data from sqlite3。
    conn = sqlite3.connect('db/dhl.db')
    sql = "SELECT awb_no,orig_fclty,shacct_no,esiteid,cSales_cd,cleaned_product_code,PLT FROM shipment_" + month + " \
		   WHERE shacct_no NOT LIKE 'F%' AND shacct_no NOT LIKE '';"

    # return DataFrame object
    df = pd.read_sql(sql, conn)

    # non_doc = All Awb expect Doc
    non_doc = df.loc[(df['cleaned_product_code'].isin(['3', '4', '8', 'E', 'F', 'H', 'J', 'M', 'P', 'Q', 'V', 'Y']))]

    ######################
    # All PLT %
    all_plt_awb = non_doc.loc[non_doc['PLT'] == 'Y'].count().tolist()[0]
    plt = all_plt_awb / non_doc.count().tolist()[0]
    # print(all_awb)
    # print(all_plt_awb)
    print("All PLT: ", plt)

    # Pre acc % / DataFrame.str() -> convert it to string, and you can use string methods
    pre = non_doc.loc[non_doc['shacct_no'].str.startswith('60')]
    pre_plt = pre.loc[pre['PLT'] == 'Y'].count().tolist()[0]
    pre_plt = pre_plt / pre.count().tolist()[0]
    # print(pre)
    # print(pre_plt)
    print("PRE ACC PLT: ", pre_plt)

    # IMP acc %
    imp = non_doc.loc[(non_doc['shacct_no'].str.startswith('95')) | (non_doc['shacct_no'].str.startswith('96'))]
    imp_plt = imp[imp['PLT'] == 'Y'].count().tolist()[0]
    imp_plt = imp_plt / imp.count().tolist()[0]
    # print(imp.count().tolist()[0])
    # print(imp_plt)
    print("IMP ACC PLT: ", imp_plt)

    ######################
    # All PLT not GZD
    all_nogzd = non_doc.loc[non_doc['orig_fclty'] != 'GZD']
    all_plt_nogzd = all_nogzd.loc[all_nogzd['PLT'] == 'Y'].count().tolist()[0]
    all_plt_nogzd = all_plt_nogzd / all_nogzd.count().tolist()[0]
    # print(all_nogzd.sort_values(by='shacct_no', ascending=False))
    # print(all_plt_nogzd)
    print("All PLT NO GZD: ", all_plt_nogzd)

    # Pre acc NO GZD %
    pre_nogzd = all_nogzd.loc[all_nogzd['shacct_no'].str.startswith('60')]
    pre_plt_nogzd = pre_nogzd.loc[pre_nogzd['PLT'] == 'Y'].count().tolist()[0]
    pre_plt_nogzd = pre_plt_nogzd / pre_nogzd.count().tolist()[0]
    print("Pre PLT NO GZD: ", pre_plt_nogzd)

    # IMP acc NO GZD %
    imp_nogzd = all_nogzd.loc[
        all_nogzd['shacct_no'].str.startswith('95') | (all_nogzd['shacct_no'].str.startswith('96'))]
    imp_plt_nogzd = imp_nogzd.loc[imp_nogzd['PLT'] == 'Y'].count().tolist()[0]
    imp_plt_nogzd = imp_plt_nogzd / imp_nogzd.count().tolist()[0]
    print("Pre PLT NO GZD: ", imp_plt_nogzd)

    ######################
    # ESHIP OPS PLT %
    eship = non_doc.loc[non_doc['esiteid'].isin(['PEK0000009055SPS', 'DDHLCNESHIPC'])]
    eship_plt = eship.loc[eship['PLT'] == 'Y'].count().tolist()[0]
    ops_plt = eship_plt / eship.count().tolist()[0]
    print("OPS PLT: ", ops_plt)

    # ESHIP GZW PLT %
    gzw = eship.loc[eship['orig_fclty'].isin(['GZW'])]
    gzw_plt = gzw.loc[gzw['PLT'] == 'Y'].count().tolist()[0]
    gzw_plt = gzw_plt / gzw.count().tolist()[0]
    print("GZW PLT: ", gzw_plt)

    # ESHIP GZH PLT %
    gzh = eship.loc[eship['orig_fclty'].isin(['GZH'])]
    gzh_plt = gzh.loc[gzh['PLT'] == 'Y'].count().tolist()[0]
    gzh_plt = gzh_plt / gzh.count().tolist()[0]
    print("GZH PLT: ", gzh_plt)

    # ESHIP GZP PLT %
    gzp = eship.loc[eship['orig_fclty'].isin(['GZP'])]
    gzp_plt = gzp.loc[gzp['PLT'] == 'Y'].count().tolist()[0]
    gzp_plt = gzp_plt / gzp.count().tolist()[0]
    print("GZP PLT: ", gzp_plt)

    # ESHIP GZE PLT %
    gze = eship.loc[eship['orig_fclty'].isin(['GZE'])]
    gze_plt = gze.loc[gze['PLT'] == 'Y'].count().tolist()[0]
    gze_plt = gze_plt / gze.count().tolist()[0]
    print("GZE PLT: ", gze_plt)

    # ESHIP GZS PLT %
    gzs = eship.loc[eship['orig_fclty'].isin(['GZS'])]
    gzs_plt = gzs.loc[gzs['PLT'] == 'Y'].count().tolist()[0]
    gzs_plt = gzs_plt / gzs.count().tolist()[0]
    print("GZS PLT: ", gzs_plt)

    # ESHIP FON PLT %
    fon = eship.loc[eship['orig_fclty'].isin(['FON'])]
    fon_plt = fon.loc[fon['PLT'] == 'Y'].count().tolist()[0]
    fon_plt = fon_plt / fon.count().tolist()[0]
    print("FON PLT: ", fon_plt)

    # ESHIP FOS PLT %
    fos = eship.loc[eship['orig_fclty'].isin(['FOS'])]
    fos_plt = fos.loc[fos['PLT'] == 'Y'].count().tolist()[0]
    fos_plt = fos_plt / fos.count().tolist()[0]
    print("FOS PLT: ", fos_plt)

    # ESHIP ZHQ PLT %
    zhq = eship.loc[eship['orig_fclty'].isin(['ZHQ'])]
    zhq_plt = zhq.loc[zhq['PLT'] == 'Y'].count().tolist()[0]
    zhq_plt = zhq_plt / zhq.count().tolist()[0]
    print("ZHQ PLT: ", zhq_plt)

    # ESHIP NNG PLT %
    nng = eship.loc[eship['orig_fclty'].isin(['NNG'])]
    nng_plt = nng.loc[nng['PLT'] == 'Y'].count().tolist()[0]
    nng_plt = nng_plt / nng.count().tolist()[0]
    print("NNG PLT: ", nng_plt)

    # ESHIP ZHA PLT %
    zha = eship.loc[eship['orig_fclty'].isin(['ZHA'])]
    zha_plt = zha.loc[zha['PLT'] == 'Y'].count().tolist()[0]
    zha_plt = zha_plt / zha.count().tolist()[0]
    print("ZHA PLT: ", zha_plt)

    # ESHIP HKE PLT %
    hke = eship.loc[eship['orig_fclty'].isin(['HKE'])]
    hke_plt = hke.loc[hke['PLT'] == 'Y'].count().tolist()[0]
    hke_plt = hke_plt / hke.count().tolist()[0]
    print("HKE PLT: ", hke_plt)

    # Sale Eship
    sale_eship = eship.loc[
        eship['cSales_cd'].isin(['GZA', 'GZB', 'GZC', 'GZG', 'GDA', 'GZD', 'GZF', 'GWC', 'GWE', 'GWF',
                                 'GWG', 'GWH', 'GEB', 'GEC', 'GED', 'GEE', 'GEF', 'GPO', 'GPB', 'GPC',
                                 'GPD', 'GPE', 'GHB', 'GHC', 'GHD', 'GHE', 'FNE', 'FNF', 'FNH', 'FNK',
                                 'ZQC', 'NNB', 'FSA', 'FSB', 'FSC', 'FSD', 'HAC', 'ZHC', 'GEO', 'GEN',
                                 'GWN', 'GWO', 'GWQ', 'GZV', 'GWS', 'GZY', 'FNM', 'FSY', 'FNN', 'FSV',
                                 'GPU', 'GHP', 'GHO', 'GPR', 'GEN', 'GWN', 'GWT', 'GZU', 'GET', 'GHT',
                                 'GPV', 'F12', 'FNP', 'NNK', 'ZQF', 'HAI', 'ZHL'])]

    sale_eship_plt = sale_eship.loc[eship['PLT'] == 'Y'].count().tolist()[0]
    sale_plt = sale_eship_plt / sale_eship.count().tolist()[0]
    print("SALE PLT: ", sale_plt)

    #####################
    # ESHIP GZA+GZB+GZC+GDA+GZD+GZF PLT %
    james = eship.loc[eship['cSales_cd'].isin(['GZA', 'GZB', 'GZC', 'GZG', 'GDA', 'GZD', 'GZF'])]
    james_plt = james.loc[james['PLT'] == 'Y'].count().tolist()[0]
    james_plt = james_plt / james.count().tolist()[0]
    print("郭靖 PLT: ", james_plt)

    # ESHIP GWC+GWE+GWF+GWG+GWH PLT %
    austin = eship.loc[eship['cSales_cd'].isin(['GWC', 'GWE', 'GWF', 'GWG', 'GWH'])]
    austin_plt = austin.loc[austin['PLT'] == 'Y'].count().tolist()[0]
    austin_plt = austin_plt / austin.count().tolist()[0]
    print("于慧显 PLT: ", austin_plt)

    # ESHIP GEB+GEC+GED+GEE+GEF PLT %
    ivy = eship.loc[eship['cSales_cd'].isin(['GEB', 'GEC', 'GED', 'GEE', 'GEF'])]
    ivy_plt = ivy.loc[ivy['PLT'] == 'Y'].count().tolist()[0]
    ivy_plt = ivy_plt / ivy.count().tolist()[0]
    print("黄懿徽 PLT: ", ivy_plt)

    # ESHIP GPO+GPB+GPC+GPD+GPE PLT %
    louis = eship.loc[eship['cSales_cd'].isin(['GPO', 'GPB', 'GPC', 'GPD', 'GPE'])]
    louis_plt = louis.loc[louis['PLT'] == 'Y'].count().tolist()[0]
    louis_plt = louis_plt / louis.count().tolist()[0]
    print("林煜 PLT: ", louis_plt)

    # ESHIP GHB+GHC+GHD+GHE PLT %
    elaine = eship.loc[eship['cSales_cd'].isin(['GHB', 'GHC', 'GHD', 'GHE'])]
    elaine_plt = elaine.loc[elaine['PLT'] == 'Y'].count().tolist()[0]
    # print(elaine_plt)
    elaine_plt = elaine_plt / elaine.count().tolist()[0]
    # print(elaine.count().tolist()[0])
    print("谢琳 PLT: ", elaine_plt)

    # ESHIP FNE+FNF+FNF+FNH+FNK+ZQC+NNB PLT %
    colin = eship.loc[eship['cSales_cd'].isin(['FNE', 'FNF', 'FNF', 'FNH', 'FNK', 'ZQC', 'NNB'])]
    colin_plt = colin.loc[colin['PLT'] == 'Y'].count().tolist()[0]
    colin_plt = colin_plt / colin.count().tolist()[0]
    print("郭光澈 PLT: ", colin_plt)

    # ESHIP FSA+FSB+FSC+FSD+HAC+ZHC PLT %
    yaoqi = eship.loc[eship['cSales_cd'].isin(['FSA', 'FSB', 'FSC', 'FSD', 'HAC', 'ZHC'])]
    yaoqi_plt = yaoqi.loc[yaoqi['PLT'] == 'Y'].count().tolist()[0]
    yaoqi_plt = yaoqi_plt / yaoqi.count().tolist()[0]
    print("方耀祺(代) PLT: ", yaoqi_plt)

    # ESHIP GEO+GEN+GWN+GWO+GWQ+GZV+GWS+GZY+FNM+FSY+FNN+FSV+GPU+GHP+GHO+GPR+GEN+GWN PLT %
    elizabeth = eship.loc[eship['cSales_cd'].isin(
        ['GEO', 'GEN', 'GWN', 'GWO', 'GWQ', 'GZV', 'GWS', 'GZY', 'FNM', 'FSY', 'FNN', 'FSV', 'GPU', 'GHP', 'GHO', 'GPR',
         'GEN', 'GWN'])]
    elizabeth_plt = elizabeth.loc[elizabeth['PLT'] == 'Y'].count().tolist()[0]
    elizabeth_plt = elizabeth_plt / elizabeth.count().tolist()[0]
    print("陈欣 PLT: ", elizabeth_plt)

    # ESHIP GWT+GZU+GET+GHT+GPV+F12+FNP+NNK+ZQF+HAI+ZHL PLT %
    hellen = eship.loc[
        eship['cSales_cd'].isin(['GWT', 'GZU', 'GET', 'GHT', 'GPV', 'F12', 'FNP', 'NNK', 'ZQF', 'HAI', 'ZHL'])]
    hellen_plt = hellen.loc[hellen['PLT'] == 'Y'].count().tolist()[0]
    hellen_plt = hellen_plt / hellen.count().tolist()[0]
    print("黎凯伦 PLT: ", hellen_plt)

    #####################
    # ESHIP GZA PLT %
    gza = eship.loc[eship['cSales_cd'].isin(['GZA'])]
    gza_plt = gza.loc[gza['PLT'] == 'Y'].count().tolist()[0]
    gza_plt = gza_plt / gza.count().tolist()[0]
    print("GZA PLT: ", gza_plt)

    # ESHIP GZB PLT %
    gzb = eship.loc[eship['cSales_cd'].isin(['GZB'])]
    gzb_plt = gzb.loc[gzb['PLT'] == 'Y'].count().tolist()[0]
    gzb_plt = gzb_plt / gzb.count().tolist()[0]
    print("GZB PLT: ", gzb_plt)

    # ESHIP GZC PLT %
    gzc = eship.loc[eship['cSales_cd'].isin(['GZC'])]
    gzc_plt = gzc.loc[gzc['PLT'] == 'Y'].count().tolist()[0]
    gzc_plt = gzc_plt / gzc.count().tolist()[0]
    print("GZC PLT: ", gzc_plt)

    # ESHIP GZG+GDA PLT %
    gzg_gda = eship.loc[eship['cSales_cd'].isin(['GZG', 'GDA'])]
    gzg_gda_plt = gzg_gda.loc[gzg_gda['PLT'] == 'Y'].count().tolist()[0]
    gzg_gda_plt = gzg_gda_plt / gzg_gda.count().tolist()[0]
    print("GZG+GDA PLT: ", gzg_gda_plt)

    # ESHIP GZD PLT %
    gzd = eship.loc[eship['cSales_cd'].isin(['GZD'])]
    gzd_plt = gzd.loc[gzd['PLT'] == 'Y'].count().tolist()[0]
    gzd_plt = gzd_plt / gzd.count().tolist()[0]
    print("GZD PLT: ", gzd_plt)

    # ESHIP GZF PLT %
    gzf = eship.loc[eship['cSales_cd'].isin(['GZF'])]
    gzf_plt = gzf.loc[gzf['PLT'] == 'Y'].count().tolist()[0]
    gzf_plt = gzf_plt / gzf.count().tolist()[0]
    print("GZF PLT: ", gzf_plt)

    # ESHIP GWC PLT %
    gwc = eship.loc[eship['cSales_cd'].isin(['GWC'])]
    gwc_plt = gwc.loc[gwc['PLT'] == 'Y'].count().tolist()[0]
    gwc_plt = gwc_plt / gwc.count().tolist()[0]
    print("GWC PLT: ", gwc_plt)

    # ESHIP GWE PLT %
    gwe = eship.loc[eship['cSales_cd'].isin(['GWE'])]
    gwe_plt = gwe.loc[gwe['PLT'] == 'Y'].count().tolist()[0]
    gwe_plt = gwe_plt / gwe.count().tolist()[0]
    print("GWE PLT: ", gwe_plt)

    # ESHIP GWF PLT %
    gwf = eship.loc[eship['cSales_cd'].isin(['GWF'])]
    gwf_plt = gwf.loc[gwf['PLT'] == 'Y'].count().tolist()[0]
    gwf_plt = gwf_plt / gwf.count().tolist()[0]
    print("gwf PLT: ", gwf_plt)

    # ESHIP GWG PLT %
    gwg = eship.loc[eship['cSales_cd'].isin(['GWG'])]
    gwg_plt = gwg.loc[gwg['PLT'] == 'Y'].count().tolist()[0]
    gwg_plt = gwg_plt / gwg.count().tolist()[0]
    print("GWG PLT: ", gwg_plt)

    # ESHIP GWH PLT %
    gwh = eship.loc[eship['cSales_cd'].isin(['GWH'])]
    gwh_plt = gwh.loc[gwh['PLT'] == 'Y'].count().tolist()[0]
    gwh_plt = gwh_plt / gwh.count().tolist()[0]
    print("GWH PLT: ", gwh_plt)

    # ESHIP GEB PLT %
    geb = eship.loc[eship['cSales_cd'].isin(['GEB'])]
    geb_plt = geb.loc[geb['PLT'] == 'Y'].count().tolist()[0]
    geb_plt = geb_plt / geb.count().tolist()[0]
    print("GEB PLT: ", geb_plt)

    # ESHIP GEC PLT %
    gec = eship.loc[eship['cSales_cd'].isin(['GEC'])]
    gec_plt = gec.loc[gec['PLT'] == 'Y'].count().tolist()[0]
    gec_plt = gec_plt / gec.count().tolist()[0]
    print("GEC PLT: ", gec_plt)

    # ESHIP GED PLT %
    ged = eship.loc[eship['cSales_cd'].isin(['GED'])]
    ged_plt = ged.loc[ged['PLT'] == 'Y'].count().tolist()[0]
    ged_plt = ged_plt / ged.count().tolist()[0]
    print("GED PLT: ", ged_plt)

    # ESHIP GEE PLT %
    gee = eship.loc[eship['cSales_cd'].isin(['GEE'])]
    gee_plt = gee.loc[gee['PLT'] == 'Y'].count().tolist()[0]
    gee_plt = gee_plt / gee.count().tolist()[0]
    print("GEE PLT: ", gee_plt)

    # ESHIP GEF PLT %
    gef = eship.loc[eship['cSales_cd'].isin(['GEF'])]
    gef_plt = gef.loc[gef['PLT'] == 'Y'].count().tolist()[0]
    gef_plt = gef_plt / gef.count().tolist()[0]
    print("GEF PLT: ", gef_plt)

    # ESHIP GPO PLT %
    gpo = eship.loc[eship['cSales_cd'].isin(['GPO'])]
    gpo_plt = gpo.loc[gpo['PLT'] == 'Y'].count().tolist()[0]
    gpo_plt = gpo_plt / gpo.count().tolist()[0]
    print("GPO PLT: ", gpo_plt)

    # ESHIP GPB PLT %
    gpb = eship.loc[eship['cSales_cd'].isin(['GPB'])]
    gpb_plt = gpb.loc[gpb['PLT'] == 'Y'].count().tolist()[0]
    gpb_plt = gpb_plt / gpb.count().tolist()[0]
    print("GPB PLT: ", gpb_plt)

    # ESHIP GPC PLT %
    gpc = eship.loc[eship['cSales_cd'].isin(['GPC'])]
    gpc_plt = gpc.loc[gpc['PLT'] == 'Y'].count().tolist()[0]
    gpc_plt = gpc_plt / gpc.count().tolist()[0]
    print("GPC PLT: ", gpc_plt)

    # ESHIP GPD PLT %
    gpd = eship.loc[eship['cSales_cd'].isin(['GPD'])]
    gpd_plt = gpd.loc[gpd['PLT'] == 'Y'].count().tolist()[0]
    gpd_plt = gpd_plt / gpd.count().tolist()[0]
    print("GPD PLT: ", gpd_plt)

    # ESHIP GPE PLT %
    gpe = eship.loc[eship['cSales_cd'].isin(['GPE'])]
    gpe_plt = gpe.loc[gpe['PLT'] == 'Y'].count().tolist()[0]
    gpe_plt = gpe_plt / gpe.count().tolist()[0]
    print("GPE PLT: ", gpe_plt)

    # ESHIP GHB PLT %
    ghb = eship.loc[eship['cSales_cd'].isin(['GHB'])]
    ghb_plt = ghb.loc[ghb['PLT'] == 'Y'].count().tolist()[0]
    ghb_plt = ghb_plt / ghb.count().tolist()[0]
    print("GHB PLT: ", ghb_plt)

    # ESHIP GHC PLT %
    ghc = eship.loc[eship['cSales_cd'].isin(['GHC'])]
    ghc_plt = ghc.loc[ghc['PLT'] == 'Y'].count().tolist()[0]
    ghc_plt = ghc_plt / ghc.count().tolist()[0]
    print("GHC PLT: ", ghc_plt)

    # ESHIP GHD PLT %
    ghd = eship.loc[eship['cSales_cd'].isin(['GHD'])]
    ghd_plt = ghd.loc[ghd['PLT'] == 'Y'].count().tolist()[0]
    ghd_plt = ghd_plt / ghd.count().tolist()[0]
    print("GHD PLT: ", ghd_plt)

    # ESHIP GHE PLT %
    ghe = eship.loc[eship['cSales_cd'].isin(['GHE'])]
    ghe_plt = ghe.loc[ghe['PLT'] == 'Y'].count().tolist()[0]
    # print(ghe_plt)
    ghe_plt = ghe_plt / ghe.count().tolist()[0]
    # print(ghe.count().tolist()[0])
    print("GHE PLT: ", ghe_plt)

    # ESHIP FNE PLT %
    fne = eship.loc[eship['cSales_cd'].isin(['FNE'])]
    fne_plt = fne.loc[fne['PLT'] == 'Y'].count().tolist()[0]
    fne_plt = fne_plt / fne.count().tolist()[0]
    print("FNE PLT: ", fne_plt)

    # ESHIP FNF PLT %
    fnf = eship.loc[eship['cSales_cd'].isin(['FNF'])]
    fnf_plt = fnf.loc[fnf['PLT'] == 'Y'].count().tolist()[0]
    fnf_plt = fnf_plt / fnf.count().tolist()[0]
    print("FNF PLT: ", fnf_plt)

    # ESHIP FNH PLT %
    fnh = eship.loc[eship['cSales_cd'].isin(['FNH'])]
    fnh_plt = fnh.loc[fnh['PLT'] == 'Y'].count().tolist()[0]
    fnh_plt = fnh_plt / fnh.count().tolist()[0]
    print("FNH PLT: ", fnh_plt)

    # ESHIP FNK PLT %
    fnk = eship.loc[eship['cSales_cd'].isin(['FNK'])]
    fnk_plt = fnk.loc[fnk['PLT'] == 'Y'].count().tolist()[0]
    fnk_plt = fnk_plt / fnk.count().tolist()[0]
    print("FNK PLT: ", fnk_plt)

    # ESHIP ZQC PLT %
    zqc = eship.loc[eship['cSales_cd'].isin(['ZQC'])]
    zqc_plt = zqc.loc[zqc['PLT'] == 'Y'].count().tolist()[0]
    zqc_plt = zqc_plt / zqc.count().tolist()[0]
    print("ZQC PLT: ", zqc_plt)

    # ESHIP NNB PLT %
    nnb = eship.loc[eship['cSales_cd'].isin(['NNB'])]
    nnb_plt = nnb.loc[nnb['PLT'] == 'Y'].count().tolist()[0]
    nnb_plt = nnb_plt / nnb.count().tolist()[0]
    print("NNB PLT: ", nnb_plt)

    # ESHIP FSA PLT %
    fsa = eship.loc[eship['cSales_cd'].isin(['FSA'])]
    fsa_plt = fsa.loc[fsa['PLT'] == 'Y'].count().tolist()[0]
    fsa_plt = fsa_plt / fsa.count().tolist()[0]
    print("FSA PLT: ", fsa_plt)

    # ESHIP FSB PLT %
    fsb = eship.loc[eship['cSales_cd'].isin(['FSB'])]
    fsb_plt = fsb.loc[fsb['PLT'] == 'Y'].count().tolist()[0]
    fsb_plt = fsb_plt / fsb.count().tolist()[0]
    print("FSB PLT: ", fsb_plt)

    # ESHIP FSC PLT %
    fsc = eship.loc[eship['cSales_cd'].isin(['FSC'])]
    fsc_plt = fsc.loc[fsc['PLT'] == 'Y'].count().tolist()[0]
    fsc_plt = fsc_plt / fsc.count().tolist()[0]
    print("FSC PLT: ", fsc_plt)

    # ESHIP FSD PLT %
    fsd = eship.loc[eship['cSales_cd'].isin(['FSD'])]
    fsd_plt = fsd.loc[fsd['PLT'] == 'Y'].count().tolist()[0]
    fsd_plt = fsd_plt / fsd.count().tolist()[0]
    print("FSD PLT: ", fsd_plt)

    # ESHIP HAC PLT %
    hac = eship.loc[eship['cSales_cd'].isin(['HAC'])]
    hac_plt = hac.loc[hac['PLT'] == 'Y'].count().tolist()[0]
    hac_plt = hac_plt / hac.count().tolist()[0]
    print("HAC PLT: ", hac_plt)

    # ESHIP ZHC PLT %
    zhc = eship.loc[eship['cSales_cd'].isin(['ZHC'])]
    zhc_plt = zhc.loc[zhc['PLT'] == 'Y'].count().tolist()[0]
    zhc_plt = zhc_plt / zhc.count().tolist()[0]
    print("ZHC PLT: ", zhc_plt)

    # ESHIP GEO PLT %
    geo = eship.loc[eship['cSales_cd'].isin(['GEO'])]
    geo_plt = geo.loc[geo['PLT'] == 'Y'].count().tolist()[0]
    geo_plt = geo_plt / geo.count().tolist()[0]
    print("GEO PLT: ", geo_plt)

    # ESHIP GEN+GWN PLT %
    gen_gwn = eship.loc[eship['cSales_cd'].isin(['GEN', 'GWN'])]
    gen_gwn_plt = gen_gwn.loc[gen_gwn['PLT'] == 'Y'].count().tolist()[0]
    gen_gwn_plt = gen_gwn_plt / gen_gwn.count().tolist()[0]
    print("GEN+GWN PLT: ", gen_gwn_plt)

    # ESHIP GWO PLT %
    gwo = eship.loc[eship['cSales_cd'].isin(['GWO'])]
    gwo_plt = gwo.loc[gwo['PLT'] == 'Y'].count().tolist()[0]
    gwo_plt = gwo_plt / gwo.count().tolist()[0]
    print("GWO PLT: ", gwo_plt)

    # ESHIP GWQ PLT %
    gwq = eship.loc[eship['cSales_cd'].isin(['GWQ'])]
    gwq_plt = gwq.loc[gwq['PLT'] == 'Y'].count().tolist()[0]
    gwq_plt = gwq_plt / gwq.count().tolist()[0]
    print("GWQ PLT: ", gwq_plt)

    # ESHIP GZV+GWS PLT %
    gzv_gws = eship.loc[eship['cSales_cd'].isin(['GZV', 'GWS'])]
    gzv_gws_plt = gzv_gws.loc[gzv_gws['PLT'] == 'Y'].count().tolist()[0]
    gzv_gws_plt = gzv_gws_plt / gzv_gws.count().tolist()[0]
    print("GZV+GWS PLT: ", gzv_gws_plt)

    # ESHIP GZY PLT %
    gzy = eship.loc[eship['cSales_cd'].isin(['GZY'])]
    gzy_plt = gzy.loc[gzy['PLT'] == 'Y'].count().tolist()[0]
    gzy_plt = gzy_plt / gzy.count().tolist()[0]
    print("GZY PLT: ", gzy_plt)

    # ESHIP FNM PLT %
    fnm = eship.loc[eship['cSales_cd'].isin(['FNM'])]
    fnm_plt = fnm.loc[fnm['PLT'] == 'Y'].count().tolist()[0]
    fnm_plt = fnm_plt / fnm.count().tolist()[0]
    print("FNM PLT: ", fnm_plt)

    # ESHIP FSY+FNN PLT %
    fsy_fnn = eship.loc[eship['cSales_cd'].isin(['FSY', 'FNN'])]
    fsy_fnn_plt = fsy_fnn.loc[fsy_fnn['PLT'] == 'Y'].count().tolist()[0]
    fsy_fnn_plt = fsy_fnn_plt / fsy_fnn.count().tolist()[0]
    print("FSY+FNN PLT: ", fsy_fnn_plt)

    # ESHIP FSV PLT %
    fsv = eship.loc[eship['cSales_cd'].isin(['FSV'])]
    fsv_plt = fsv.loc[fsv['PLT'] == 'Y'].count().tolist()[0]
    fsv_plt = fsv_plt / fsv.count().tolist()[0]
    print("FSV PLT: ", fsv_plt)

    # ESHIP GPU PLT %
    gpu = eship.loc[eship['cSales_cd'].isin(['GPU'])]
    gpu_plt = gpu.loc[gpu['PLT'] == 'Y'].count().tolist()[0]
    gpu_plt = gpu_plt / gpu.count().tolist()[0]
    print("GPU PLT: ", gpu_plt)

    # ESHIP GHP PLT %
    ghp = eship.loc[eship['cSales_cd'].isin(['GHP'])]
    ghp_plt = ghp.loc[ghp['PLT'] == 'Y'].count().tolist()[0]
    ghp_plt = ghp_plt / ghp.count().tolist()[0]
    print("GHP PLT: ", ghp_plt)

    # ESHIP GHO+GPR PLT %
    gho_gpr = eship.loc[eship['cSales_cd'].isin(['GHO', 'GPR'])]
    gho_gpr_plt = gho_gpr.loc[gho_gpr['PLT'] == 'Y'].count().tolist()[0]
    gho_gpr_plt = gho_gpr_plt / gho_gpr.count().tolist()[0]
    print("GHO+GPR PLT: ", gho_gpr_plt)

    # ESHIP GHT+GPV+F12+FNP+NNK+ZQF+HAI+ZHL PLT %
    moji = eship.loc[eship['cSales_cd'].isin(['GHT', 'GPV', 'F12', 'FNP', 'NNK', 'ZQF', 'HAI', 'ZHL'])]
    moji_plt = moji.loc[moji['PLT'] == 'Y'].count().tolist()[0]
    moji_plt = moji_plt / moji.count().tolist()[0]
    print("GHT+GPV+F12+FNP+NNK+ZQF+HAI+ZHL PLT: ", moji_plt)

    # ESHIP GWT+GZU+GET PLT %
    haiyan = eship.loc[eship['cSales_cd'].isin(['GWT', 'GZU', 'GET'])]
    haiyan_plt = haiyan.loc[haiyan['PLT'] == 'Y'].count().tolist()[0]
    haiyan_plt = haiyan_plt / haiyan.count().tolist()[0]
    print("GWT+GZU+GET PLT: ", haiyan_plt)


    data_list = [month, plt, pre_plt, imp_plt, all_plt_nogzd, pre_plt_nogzd, imp_plt_nogzd, ops_plt,
                 gzw_plt, gzh_plt, gzp_plt, gze_plt, gzs_plt, fon_plt, fos_plt, zhq_plt, nng_plt, zha_plt, hke_plt,sale_plt,
                 james_plt, austin_plt, ivy_plt, louis_plt, elaine_plt, colin_plt, yaoqi_plt, elizabeth_plt,hellen_plt,
                 gza_plt, gzb_plt, gzc_plt, gzg_gda_plt, gzd_plt, gzf_plt, gwc_plt, gwe_plt, gwf_plt, gwg_plt, gwh_plt,
                 geb_plt, gec_plt, ged_plt, gee_plt, gef_plt, gpo_plt, gpb_plt, gpc_plt, gpd_plt, gpe_plt, ghb_plt,
                 ghc_plt, ghd_plt, ghe_plt, fne_plt, fnf_plt, fnh_plt, fnk_plt, zqc_plt, nnb_plt, fsa_plt, fsb_plt,
                 fsc_plt, fsd_plt, hac_plt, zhc_plt, geo_plt, gen_gwn_plt, gwo_plt, gwq_plt, gzv_gws_plt, gzy_plt,
                 fnm_plt, fsy_fnn_plt, fsv_plt, gpu_plt, ghp_plt, gho_gpr_plt, moji_plt, haiyan_plt]

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
    sheet = workbook.add_sheet('PLT', cell_overwrite_ok=True)
    row = sheet.row(0)
    row.write(0, "All PLT")
    row.write(1, month + "占比")


    item = Item()

    for x in range(1, len(item.name_list)):
        row = sheet.row(x)
        row.write(0, item.name_list[x])
        row.write(1, data_list[x], style)

    workbook.save("ecom/Report/ecom_plt_" + month + ".xlsx")
    print('ecom plt report 已生成 ')
    print('-----------------------')

    conn.commit()
    conn.close()
