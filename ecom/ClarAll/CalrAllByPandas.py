import sqlite3
import pandas as pd


def calrAllByPandas(month):
	# pandas load data from sqlite3。
	conn = sqlite3.connect('db/dhl.db')
	sql = "SELECT awb_no,orig_fclty,shacct_no,esiteid,cSales_cd,cleaned_product_code,PLT FROM ecom_base_" + month + " \
		   WHERE shacct_no NOT LIKE 'F%' AND shacct_no NOT LIKE 'C%' AND shacct_no NOT LIKE '';"

	# return DataFrame object
	df = pd.read_sql(sql, conn)

	# non_doc = All Awb expect Doc
	non_doc = df.loc[(df['cleaned_product_code'].isin(['3', '4', '8', 'E', 'F', 'H', 'J', 'M', 'P', 'Q', 'V', 'Y']))]

	######################
	# All PLT percentage
	all_plt_awb = non_doc.loc[non_doc['PLT'] == 'Y'].count().tolist()[0]
	plt = all_plt_awb / non_doc.count().tolist()[0]
	# print(all_awb)
	# print(all_plt_awb)
	print("All PLT: ", plt)

	# Pre acc percentage / DataFrame.str() -> convert it to string, and you can use string methods
	pre = non_doc.loc[non_doc['shacct_no'].str.startswith('60')]
	pre_plt = pre.loc[pre['PLT'] == 'Y'].count().tolist()[0]
	pre_plt = pre_plt / pre.count().tolist()[0]
	# print(pre)
	# print(pre_plt)
	print("PRE ACC PLT: ", pre_plt)

	# IMP acc percentage
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

	# Pre acc NO GZD percentage
	pre_nogzd = all_nogzd.loc[all_nogzd['shacct_no'].str.startswith('60')]
	pre_plt_nogzd = pre_nogzd.loc[pre_nogzd['PLT'] == 'Y'].count().tolist()[0]
	pre_plt_nogzd = pre_plt_nogzd / pre_nogzd.count().tolist()[0]
	print("Pre PLT NO GZD: ", pre_plt_nogzd)

	# IMP acc NO GZD percentage
	imp_nogzd = all_nogzd.loc[
		all_nogzd['shacct_no'].str.startswith('95') | (all_nogzd['shacct_no'].str.startswith('96'))]
	imp_plt_nogzd = imp_nogzd.loc[imp_nogzd['PLT'] == 'Y'].count().tolist()[0]
	imp_plt_nogzd = imp_plt_nogzd / imp_nogzd.count().tolist()[0]
	print("Pre PLT NO GZD: ", imp_plt_nogzd)

	######################
	# ESHIP OPS PLT percentage
	eship = non_doc.loc[non_doc['esiteid'].isin(['PEK0000009055SPS', 'DDHLCNESHIPC'])]
	eship_plt = eship.loc[eship['PLT'] == 'Y'].count().tolist()[0]
	ops_plt = eship_plt / eship.count().tolist()[0]
	print("OPS PLT: ", ops_plt)

	# ESHIP GZW PLT percentage
	gzw = eship.loc[eship['orig_fclty'].isin(['GZW'])]
	gzw_plt = gzw.loc[gzw['PLT'] == 'Y'].count().tolist()[0]
	gzw_plt = gzw_plt / gzw.count().tolist()[0]
	print("GZW PLT: ", gzw_plt)

	# ESHIP GZH PLT percentage
	gzh = eship.loc[eship['orig_fclty'].isin(['GZH'])]
	gzh_plt = gzh.loc[gzh['PLT'] == 'Y'].count().tolist()[0]
	gzh_plt = gzh_plt / gzh.count().tolist()[0]
	print("GZH PLT: ", gzh_plt)

	# ESHIP GZP PLT percentage
	gzp = eship.loc[eship['orig_fclty'].isin(['GZP'])]
	gzp_plt = gzp.loc[gzp['PLT'] == 'Y'].count().tolist()[0]
	gzp_plt = gzp_plt / gzp.count().tolist()[0]
	print("GZP PLT: ", gzp_plt)

	# ESHIP GZE PLT percentage
	gze = eship.loc[eship['orig_fclty'].isin(['GZE'])]
	gze_plt = gze.loc[gze['PLT'] == 'Y'].count().tolist()[0]
	gze_plt = gze_plt / gze.count().tolist()[0]
	print("GZE PLT: ", gze_plt)

	# ESHIP GZS PLT percentage
	gzs = eship.loc[eship['orig_fclty'].isin(['GZS'])]
	gzs_plt = gzs.loc[gzs['PLT'] == 'Y'].count().tolist()[0]
	gzs_plt = gzs_plt / gzs.count().tolist()[0]
	print("GZS PLT: ", gzs_plt)

	# ESHIP FON PLT percentage
	fon = eship.loc[eship['orig_fclty'].isin(['FON'])]
	fon_plt = fon.loc[fon['PLT'] == 'Y'].count().tolist()[0]
	fon_plt = fon_plt / fon.count().tolist()[0]
	print("FON PLT: ", fon_plt)

	# ESHIP FOS PLT percentage
	fos = eship.loc[eship['orig_fclty'].isin(['FOS'])]
	fos_plt = fos.loc[fos['PLT'] == 'Y'].count().tolist()[0]
	fos_plt = fos_plt / fos.count().tolist()[0]
	print("FOS PLT: ", fos_plt)

	# ESHIP ZHQ PLT percentage
	zhq = eship.loc[eship['orig_fclty'].isin(['ZHQ'])]
	zhq_plt = zhq.loc[zhq['PLT'] == 'Y'].count().tolist()[0]
	zhq_plt = zhq_plt / zhq.count().tolist()[0]
	print("ZHQ PLT: ", zhq_plt)

	# ESHIP NNG PLT percentage
	nng = eship.loc[eship['orig_fclty'].isin(['NNG'])]
	nng_plt = nng.loc[nng['PLT'] == 'Y'].count().tolist()[0]
	nng_plt = nng_plt / nng.count().tolist()[0]
	print("NNG PLT: ", nng_plt)

	# ESHIP ZHA PLT percentage
	zha = eship.loc[eship['orig_fclty'].isin(['ZHA'])]
	zha_plt = zha.loc[zha['PLT'] == 'Y'].count().tolist()[0]
	zha_plt = zha_plt / zha.count().tolist()[0]
	print("ZHA PLT: ", zha_plt)

	# ESHIP HKE PLT percentage
	hke = eship.loc[eship['orig_fclty'].isin(['HKE'])]
	hke_plt = hke.loc[hke['PLT'] == 'Y'].count().tolist()[0]
	hke_plt = hke_plt / hke.count().tolist()[0]
	print("HKE PLT: ", hke_plt)

	#####################
	# ESHIP GZA+GZB+GZC+GDA+GZD+GZF PLT percentage
	james = eship.loc[eship['cSales_cd'].isin(['GZA', 'GZB', 'GZC', 'GDA', 'GZD', 'GZF'])]
	james_plt = james.loc[james['PLT'] == 'Y'].count().tolist()[0]
	james_plt = james_plt / james.count().tolist()[0]
	print("郭靖 PLT: ", james_plt)

	# ESHIP GWC+GWE+GWF+GWG+GWH PLT percentage
	austin = eship.loc[eship['cSales_cd'].isin(['GWC', 'GWE', 'GWF', 'GWG', 'GWH'])]
	austin_plt = austin.loc[austin['PLT'] == 'Y'].count().tolist()[0]
	austin_plt = austin_plt / austin.count().tolist()[0]
	print("于慧显 PLT: ", austin_plt)

	# ESHIP GEB+GEC+GED+GEE+GEF PLT percentage
	ivy = eship.loc[eship['cSales_cd'].isin(['GEB', 'GEC', 'GED', 'GEE', 'GEF'])]
	ivy_plt = ivy.loc[ivy['PLT'] == 'Y'].count().tolist()[0]
	ivy_plt = ivy_plt / ivy.count().tolist()[0]
	print("黄懿徽 PLT: ", ivy_plt)

	# ESHIP GPO+GPB+GPC+GPD+GPE PLT percentage
	louis = eship.loc[eship['cSales_cd'].isin(['GPO', 'GPB', 'GPC', 'GPD', 'GPE'])]
	louis_plt = louis.loc[louis['PLT'] == 'Y'].count().tolist()[0]
	louis_plt = louis_plt / louis.count().tolist()[0]
	print("林煜 PLT: ", louis_plt)

	# ESHIP GHB+GHC+GHD+GHE PLT percentage
	elaine = eship.loc[eship['cSales_cd'].isin(['GHB', 'GHC', 'GHD', 'GHE'])]
	elaine_plt = elaine.loc[elaine['PLT'] == 'Y'].count().tolist()[0]
	# print(elaine_plt)
	elaine_plt = elaine_plt / elaine.count().tolist()[0]
	# print(elaine.count().tolist()[0])
	print("谢琳 PLT: ", elaine_plt)

	# ESHIP FNE+FNF+FNF+FNH+FNK+ZQC+NNB PLT percentage
	colin = eship.loc[eship['cSales_cd'].isin(['FNE', 'FNF', 'FNF', 'FNH', 'FNK', 'ZQC', 'NNB'])]
	colin_plt = colin.loc[colin['PLT'] == 'Y'].count().tolist()[0]
	colin_plt = colin_plt / colin.count().tolist()[0]
	print("郭光澈 PLT: ", colin_plt)

	# ESHIP FSA+FSB+FSC+FSD+HAC+ZHC PLT percentage
	yaoqi = eship.loc[eship['cSales_cd'].isin(['FSA', 'FSB', 'FSC', 'FSD', 'HAC', 'ZHC'])]
	yaoqi_plt = yaoqi.loc[yaoqi['PLT'] == 'Y'].count().tolist()[0]
	yaoqi_plt = yaoqi_plt / yaoqi.count().tolist()[0]
	print("方耀祺(代) PLT: ", yaoqi_plt)

	# ESHIP GEO+GEN+GWN+GWO+GWQ+GZV+GWS+GZY+FNM+FSY+FNN+FSV+GPU+GHP+GHO+GPR+GEN+GWN PLT percentage
	elizabeth = eship.loc[eship['cSales_cd'].isin(
		['GEO', 'GEN', 'GWN', 'GWO', 'GWQ', 'GZV', 'GWS', 'GZY', 'FNM', 'FSY', 'FNN', 'FSV', 'GPU', 'GHP', 'GHO', 'GPR',
		 'GEN', 'GWN'])]
	elizabeth_plt = elizabeth.loc[elizabeth['PLT'] == 'Y'].count().tolist()[0]
	elizabeth_plt = elizabeth_plt / elizabeth.count().tolist()[0]
	print("陈欣 PLT: ", elizabeth_plt)

	# ESHIP GWT+GZU+GET+GHT+GPV+F12+FNP+NNK+ZQF+HAI+ZHL PLT percentage
	hellen = eship.loc[
		eship['cSales_cd'].isin(['GWT', 'GZU', 'GET', 'GHT', 'GPV', 'F12', 'FNP', 'NNK', 'ZQF', 'HAI', 'ZHL'])]
	hellen_plt = hellen.loc[hellen['PLT'] == 'Y'].count().tolist()[0]
	hellen_plt = hellen_plt / hellen.count().tolist()[0]
	print("黎凯伦 PLT: ", hellen_plt)

	#####################
	# ESHIP GZA PLT percentage
	gza = eship.loc[eship['cSales_cd'].isin(['GZA'])]
	gza_plt = gza.loc[gza['PLT'] == 'Y'].count().tolist()[0]
	gza_plt = gza_plt / gza.count().tolist()[0]
	print("GZA PLT: ", gza_plt)

	# ESHIP GZB PLT percentage
	gzb = eship.loc[eship['cSales_cd'].isin(['GZB'])]
	gzb_plt = gzb.loc[gzb['PLT'] == 'Y'].count().tolist()[0]
	gzb_plt = gzb_plt / gzb.count().tolist()[0]
	print("GZB PLT: ", gzb_plt)

	# ESHIP GZC+GDA PLT percentage
	gzc_gda = eship.loc[eship['cSales_cd'].isin(['GZC', 'GDA'])]
	gzc_gda_plt = gzc_gda.loc[gzc_gda['PLT'] == 'Y'].count().tolist()[0]
	gzc_gda_plt = gzc_gda_plt / gzc_gda.count().tolist()[0]
	print("GZC+GDA PLT: ", gzc_gda_plt)

	# ESHIP GZD PLT percentage
	gzd = eship.loc[eship['cSales_cd'].isin(['GZD'])]
	gzd_plt = gzd.loc[gzd['PLT'] == 'Y'].count().tolist()[0]
	gzd_plt = gzd_plt / gzd.count().tolist()[0]
	print("GZD PLT: ", gzd_plt)

	# ESHIP GZF PLT percentage
	gzf = eship.loc[eship['cSales_cd'].isin(['GZF'])]
	gzf_plt = gzf.loc[gzf['PLT'] == 'Y'].count().tolist()[0]
	gzf_plt = gzf_plt / gzf.count().tolist()[0]
	print("GZF PLT: ", gzf_plt)

	# ESHIP GWC PLT percentage
	gwc = eship.loc[eship['cSales_cd'].isin(['GWC'])]
	gwc_plt = gwc.loc[gwc['PLT'] == 'Y'].count().tolist()[0]
	gwc_plt = gwc_plt / gwc.count().tolist()[0]
	print("GWC PLT: ", gwc_plt)

	# ESHIP GWE PLT percentage
	gwe = eship.loc[eship['cSales_cd'].isin(['GWE'])]
	gwe_plt = gwe.loc[gwe['PLT'] == 'Y'].count().tolist()[0]
	gwe_plt = gwe_plt / gwe.count().tolist()[0]
	print("GWE PLT: ", gwe_plt)

	# ESHIP GWF PLT percentage
	gwf = eship.loc[eship['cSales_cd'].isin(['GWF'])]
	gwf_plt = gwf.loc[gwf['PLT'] == 'Y'].count().tolist()[0]
	gwf_plt = gwf_plt / gwf.count().tolist()[0]
	print("gwf PLT: ", gwf_plt)

	# ESHIP GWG PLT percentage
	gwg = eship.loc[eship['cSales_cd'].isin(['GWG'])]
	gwg_plt = gwg.loc[gwg['PLT'] == 'Y'].count().tolist()[0]
	gwg_plt = gwg_plt / gwg.count().tolist()[0]
	print("GWG PLT: ", gwg_plt)

	# ESHIP GWH PLT percentage
	gwh = eship.loc[eship['cSales_cd'].isin(['GWH'])]
	gwh_plt = gwh.loc[gwh['PLT'] == 'Y'].count().tolist()[0]
	gwh_plt = gwh_plt / gwh.count().tolist()[0]
	print("GWH PLT: ", gwh_plt)

	# ESHIP GEB PLT percentage
	geb = eship.loc[eship['cSales_cd'].isin(['GEB'])]
	geb_plt = geb.loc[geb['PLT'] == 'Y'].count().tolist()[0]
	geb_plt = geb_plt / geb.count().tolist()[0]
	print("GEB PLT: ", geb_plt)

	# ESHIP GEC PLT percentage
	gec = eship.loc[eship['cSales_cd'].isin(['GEC'])]
	gec_plt = gec.loc[gec['PLT'] == 'Y'].count().tolist()[0]
	gec_plt = gec_plt / gec.count().tolist()[0]
	print("GEC PLT: ", gec_plt)

	# ESHIP GED PLT percentage
	ged = eship.loc[eship['cSales_cd'].isin(['GED'])]
	ged_plt = ged.loc[ged['PLT'] == 'Y'].count().tolist()[0]
	ged_plt = ged_plt / ged.count().tolist()[0]
	print("GED PLT: ", ged_plt)

	# ESHIP GEE PLT percentage
	gee = eship.loc[eship['cSales_cd'].isin(['GEE'])]
	gee_plt = gee.loc[gee['PLT'] == 'Y'].count().tolist()[0]
	gee_plt = gee_plt / gee.count().tolist()[0]
	print("GEE PLT: ", gee_plt)

	# ESHIP GEF PLT percentage
	gef = eship.loc[eship['cSales_cd'].isin(['GEF'])]
	gef_plt = gef.loc[gef['PLT'] == 'Y'].count().tolist()[0]
	gef_plt = gef_plt / gef.count().tolist()[0]
	print("GEF PLT: ", gef_plt)

	# ESHIP GPO PLT percentage
	gpo = eship.loc[eship['cSales_cd'].isin(['GPO'])]
	gpo_plt = gpo.loc[gpo['PLT'] == 'Y'].count().tolist()[0]
	gpo_plt = gpo_plt / gpo.count().tolist()[0]
	print("GPO PLT: ", gpo_plt)

	# ESHIP GPB PLT percentage
	gpb = eship.loc[eship['cSales_cd'].isin(['GPB'])]
	gpb_plt = gpb.loc[gpb['PLT'] == 'Y'].count().tolist()[0]
	gpb_plt = gpb_plt / gpb.count().tolist()[0]
	print("GPB PLT: ", gpb_plt)

	# ESHIP GPC PLT percentage
	gpc = eship.loc[eship['cSales_cd'].isin(['GPC'])]
	gpc_plt = gpc.loc[gpc['PLT'] == 'Y'].count().tolist()[0]
	gpc_plt = gpc_plt / gpc.count().tolist()[0]
	print("GPC PLT: ", gpc_plt)

	# ESHIP GPD PLT percentage
	gpd = eship.loc[eship['cSales_cd'].isin(['GPD'])]
	gpd_plt = gpd.loc[gpd['PLT'] == 'Y'].count().tolist()[0]
	gpd_plt = gpd_plt / gpd.count().tolist()[0]
	print("GPD PLT: ", gpd_plt)

	# ESHIP GPE PLT percentage
	gpe = eship.loc[eship['cSales_cd'].isin(['GPE'])]
	gpe_plt = gpe.loc[gpe['PLT'] == 'Y'].count().tolist()[0]
	gpe_plt = gpe_plt / gpe.count().tolist()[0]
	print("GPE PLT: ", gpe_plt)

	# ESHIP GHB PLT percentage
	ghb = eship.loc[eship['cSales_cd'].isin(['GHB'])]
	ghb_plt = ghb.loc[ghb['PLT'] == 'Y'].count().tolist()[0]
	ghb_plt = ghb_plt / ghb.count().tolist()[0]
	print("GHB PLT: ", ghb_plt)

	# ESHIP GHC PLT percentage
	ghc = eship.loc[eship['cSales_cd'].isin(['GHC'])]
	ghc_plt = ghc.loc[ghc['PLT'] == 'Y'].count().tolist()[0]
	ghc_plt = ghc_plt / ghc.count().tolist()[0]
	print("GHC PLT: ", ghc_plt)

	# ESHIP GHD PLT percentage
	ghd = eship.loc[eship['cSales_cd'].isin(['GHD'])]
	ghd_plt = ghd.loc[ghd['PLT'] == 'Y'].count().tolist()[0]
	ghd_plt = ghd_plt / ghd.count().tolist()[0]
	print("GHD PLT: ", ghd_plt)

	# ESHIP GHE PLT percentage
	ghe = eship.loc[eship['cSales_cd'].isin(['GHE'])]
	ghe_plt = ghe.loc[ghe['PLT'] == 'Y'].count().tolist()[0]
	# print(ghe_plt)
	ghe_plt = ghe_plt / ghe.count().tolist()[0]
	# print(ghe.count().tolist()[0])
	print("GHE PLT: ", ghe_plt)

	# ESHIP FNE PLT percentage
	fne = eship.loc[eship['cSales_cd'].isin(['FNE'])]
	fne_plt = fne.loc[fne['PLT'] == 'Y'].count().tolist()[0]
	fne_plt = fne_plt / fne.count().tolist()[0]
	print("FNE PLT: ", fne_plt)

	# ESHIP FNF PLT percentage
	fnf = eship.loc[eship['cSales_cd'].isin(['FNF'])]
	fnf_plt = fnf.loc[fnf['PLT'] == 'Y'].count().tolist()[0]
	fnf_plt = fnf_plt / fnf.count().tolist()[0]
	print("FNF PLT: ", fnf_plt)

	# ESHIP FNH PLT percentage
	fnh = eship.loc[eship['cSales_cd'].isin(['FNH'])]
	fnh_plt = fnh.loc[fnh['PLT'] == 'Y'].count().tolist()[0]
	fnh_plt = fnh_plt / fnh.count().tolist()[0]
	print("FNH PLT: ", fnh_plt)

	# ESHIP FNK PLT percentage
	fnk = eship.loc[eship['cSales_cd'].isin(['FNK'])]
	fnk_plt = fnk.loc[fnk['PLT'] == 'Y'].count().tolist()[0]
	fnk_plt = fnk_plt / fnk.count().tolist()[0]
	print("FNK PLT: ", fnk_plt)

	# ESHIP ZQC PLT percentage
	zqc = eship.loc[eship['cSales_cd'].isin(['ZQC'])]
	zqc_plt = zqc.loc[zqc['PLT'] == 'Y'].count().tolist()[0]
	zqc_plt = zqc_plt / zqc.count().tolist()[0]
	print("ZQC PLT: ", zqc_plt)

	# ESHIP NNB PLT percentage
	nnb = eship.loc[eship['cSales_cd'].isin(['NNB'])]
	nnb_plt = nnb.loc[nnb['PLT'] == 'Y'].count().tolist()[0]
	nnb_plt = nnb_plt / nnb.count().tolist()[0]
	print("NNB PLT: ", nnb_plt)

	# ESHIP FSA PLT percentage
	fsa = eship.loc[eship['cSales_cd'].isin(['FSA'])]
	fsa_plt = fsa.loc[fsa['PLT'] == 'Y'].count().tolist()[0]
	fsa_plt = fsa_plt / fsa.count().tolist()[0]
	print("FSA PLT: ", fsa_plt)

	# ESHIP FSB PLT percentage
	fsb = eship.loc[eship['cSales_cd'].isin(['FSB'])]
	fsb_plt = fsb.loc[fsb['PLT'] == 'Y'].count().tolist()[0]
	fsb_plt = fsb_plt / fsb.count().tolist()[0]
	print("FSB PLT: ", fsb_plt)

	# ESHIP FSC PLT percentage
	fsc = eship.loc[eship['cSales_cd'].isin(['FSC'])]
	fsc_plt = fsc.loc[fsc['PLT'] == 'Y'].count().tolist()[0]
	fsc_plt = fsc_plt / fsc.count().tolist()[0]
	print("FSC PLT: ", fsc_plt)

	# ESHIP FSD PLT percentage
	fsd = eship.loc[eship['cSales_cd'].isin(['FSD'])]
	fsd_plt = fsd.loc[fsd['PLT'] == 'Y'].count().tolist()[0]
	fsd_plt = fsd_plt / fsd.count().tolist()[0]
	print("FSD PLT: ", fsd_plt)

	# ESHIP HAC PLT percentage
	hac = eship.loc[eship['cSales_cd'].isin(['HAC'])]
	hac_plt = hac.loc[hac['PLT'] == 'Y'].count().tolist()[0]
	hac_plt = hac_plt / hac.count().tolist()[0]
	print("HAC PLT: ", hac_plt)

	# ESHIP ZHC PLT percentage
	zhc = eship.loc[eship['cSales_cd'].isin(['ZHC'])]
	zhc_plt = zhc.loc[zhc['PLT'] == 'Y'].count().tolist()[0]
	zhc_plt = zhc_plt / zhc.count().tolist()[0]
	print("ZHC PLT: ", zhc_plt)

	# ESHIP GEO PLT percentage
	geo = eship.loc[eship['cSales_cd'].isin(['GEO'])]
	geo_plt = geo.loc[geo['PLT'] == 'Y'].count().tolist()[0]
	geo_plt = geo_plt / geo.count().tolist()[0]
	print("GEO PLT: ", geo_plt)

	# ESHIP GEN+GWN PLT percentage
	gen_gwn = eship.loc[eship['cSales_cd'].isin(['GEN', 'GWN'])]
	gen_gwn_plt = gen_gwn.loc[gen_gwn['PLT'] == 'Y'].count().tolist()[0]
	gen_gwn_plt = gen_gwn_plt / gen_gwn.count().tolist()[0]
	print("GEN+GWN PLT: ", gen_gwn_plt)

	# ESHIP GWO PLT percentage
	gwo = eship.loc[eship['cSales_cd'].isin(['GWO'])]
	gwo_plt = gwo.loc[gwo['PLT'] == 'Y'].count().tolist()[0]
	gwo_plt = gwo_plt / gwo.count().tolist()[0]
	print("GWO PLT: ", gwo_plt)

	# ESHIP GWQ PLT percentage
	gwq = eship.loc[eship['cSales_cd'].isin(['GWQ'])]
	gwq_plt = gwq.loc[gwq['PLT'] == 'Y'].count().tolist()[0]
	gwq_plt = gwq_plt / gwq.count().tolist()[0]
	print("GWQ PLT: ", gwq_plt)

	# ESHIP GZV+GWS PLT percentage
	gzv_gws = eship.loc[eship['cSales_cd'].isin(['GZV', 'GWS'])]
	gzv_gws_plt = gzv_gws.loc[gzv_gws['PLT'] == 'Y'].count().tolist()[0]
	gzv_gws_plt = gzv_gws_plt / gzv_gws.count().tolist()[0]
	print("GZV+GWS PLT: ", gzv_gws_plt)

	# ESHIP GZY PLT percentage
	gzy = eship.loc[eship['cSales_cd'].isin(['GZY'])]
	gzy_plt = gzy.loc[gzy['PLT'] == 'Y'].count().tolist()[0]
	gzy_plt = gzy_plt / gzy.count().tolist()[0]
	print("GZY PLT: ", gzy_plt)

	# ESHIP FNM PLT percentage
	fnm = eship.loc[eship['cSales_cd'].isin(['FNM'])]
	fnm_plt = fnm.loc[fnm['PLT'] == 'Y'].count().tolist()[0]
	fnm_plt = fnm_plt / fnm.count().tolist()[0]
	print("FNM PLT: ", fnm_plt)

	# ESHIP FSY+FNN PLT percentage
	fsy_fnn = eship.loc[eship['cSales_cd'].isin(['FSY', 'FNN'])]
	fsy_fnn_plt = fsy_fnn.loc[fsy_fnn['PLT'] == 'Y'].count().tolist()[0]
	fsy_fnn_plt = fsy_fnn_plt / fsy_fnn.count().tolist()[0]
	print("FSY+FNN PLT: ", fsy_fnn_plt)

	# ESHIP FSV PLT percentage
	fsv = eship.loc[eship['cSales_cd'].isin(['FSV'])]
	fsv_plt = fsv.loc[fsv['PLT'] == 'Y'].count().tolist()[0]
	fsv_plt = fsv_plt / fsv.count().tolist()[0]
	print("FSV PLT: ", fsv_plt)

	# ESHIP GPU PLT percentage
	gpu = eship.loc[eship['cSales_cd'].isin(['GPU'])]
	gpu_plt = gpu.loc[gpu['PLT'] == 'Y'].count().tolist()[0]
	gpu_plt = gpu_plt / gpu.count().tolist()[0]
	print("GPU PLT: ", gpu_plt)

	# ESHIP GHP PLT percentage
	ghp = eship.loc[eship['cSales_cd'].isin(['GHP'])]
	ghp_plt = ghp.loc[ghp['PLT'] == 'Y'].count().tolist()[0]
	ghp_plt = ghp_plt / ghp.count().tolist()[0]
	print("GHP PLT: ", ghp_plt)

	# ESHIP GHO+GPR PLT percentage
	gho_gpr = eship.loc[eship['cSales_cd'].isin(['GHO', 'GPR'])]
	gho_gpr_plt = gho_gpr.loc[gho_gpr['PLT'] == 'Y'].count().tolist()[0]
	gho_gpr_plt = gho_gpr_plt / gho_gpr.count().tolist()[0]
	print("GHO+GPR PLT: ", gho_gpr_plt)

	# ESHIP GHT+GPV+F12+FNP+NNK+ZQF+HAI+ZHL PLT percentage
	moji = eship.loc[eship['cSales_cd'].isin(['GHT', 'GPV', 'F12', 'FNP', 'NNK', 'ZQF', 'HAI', 'ZHL'])]
	moji_plt = moji.loc[moji['PLT'] == 'Y'].count().tolist()[0]
	moji_plt = moji_plt / moji.count().tolist()[0]
	print("GHT+GPV+F12+FNP+NNK+ZQF+HAI+ZHL PLT: ", moji_plt)

	# ESHIP GWT+GZU+GET PLT percentage
	haiyan = eship.loc[eship['cSales_cd'].isin(['GWT', 'GZU', 'GET'])]
	haiyan_plt = haiyan.loc[haiyan['PLT'] == 'Y'].count().tolist()[0]
	haiyan_plt = haiyan_plt / haiyan.count().tolist()[0]
	print("GWT+GZU+GET PLT: ", haiyan_plt)

	conn.execute(
		"INSERT INTO ecom_plt_monthly VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?, \
		?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
		(month, plt, pre_plt, imp_plt, all_plt_nogzd, pre_plt_nogzd, imp_plt_nogzd, ops_plt,
		 gzw_plt, gzh_plt, gzp_plt, gze_plt, gzs_plt, fon_plt, fos_plt, zhq_plt, nng_plt, zha_plt, hke_plt,
		 james_plt, austin_plt, ivy_plt, louis_plt, elaine_plt, colin_plt, yaoqi_plt, elizabeth_plt, hellen_plt,
		 gza_plt, gzb_plt, gzc_gda_plt, gzd_plt, gzf_plt, gwc_plt, gwe_plt, gwf_plt, gwg_plt, gwh_plt,
		 geb_plt, gec_plt, ged_plt, gee_plt, gef_plt, gpo_plt, gpb_plt, gpc_plt, gpd_plt, gpe_plt, ghb_plt,
		 ghc_plt, ghd_plt, ghe_plt, fne_plt, fnf_plt, fnh_plt, fnk_plt, zqc_plt, nnb_plt, fsa_plt, fsb_plt,
		 fsc_plt, fsd_plt, hac_plt, zhc_plt, geo_plt, gen_gwn_plt, gwo_plt, gwq_plt, gzv_gws_plt, gzy_plt,
		 fnm_plt, fsy_fnn_plt, fsv_plt, gpu_plt, ghp_plt, gho_gpr_plt, moji_plt, haiyan_plt))

	conn.commit()
	conn.close()
