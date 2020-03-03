from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()


class Item():
    name_list = ['All PLT', '2019', '60', '96', '2019(除领添)', '60(除领添)', '96(除领添)', 'OPS', 'GZW', 'GZH', 'GZP', 'GZE',
                 'GZS', 'FON', 'FOS', 'ZHQ', 'NNG', 'ZHA', 'HKE', 'SLS', '郭靖', '于慧显', '黄懿徽', '林煜', '谢琳', '郭光澈',
                 '方耀祺（代）', '陈欣', '黎凯伦', 'GZA', 'GZB', 'GZC', 'GZG+GDA', 'GZD', 'GZF', 'GWC', 'GWE', 'GWF',
                 'GWG', 'GWH', 'GEB', 'GEC', 'GED', 'GEE', 'GEF', 'GPO', 'GPB', 'GPC', 'GPD', 'GPE', 'GHB', 'GHC',
                 'GHD', 'GHE',
                 'FNE', 'FNF', 'FNH', 'FNK', 'ZQC', 'NNB', 'FSA', 'FSB', 'FSC', 'FSD', 'HAC', 'ZHC', 'GEO', 'GEN+GWN',
                 'GWO', 'GWQ', 'GZV+GWS', 'GZY', 'FNM', 'FSY+FNN', 'FSV', 'GPU', 'GHP', 'GHO+GPR',
                 'GHT+GPV+F12+FNP+NNK+ZQF+HAI+ZHL', 'GWT+GZU+GET']


    __tablename__ = 'item_list'

    id = Column(Integer, primary_key=True)
