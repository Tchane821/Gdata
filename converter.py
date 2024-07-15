"""
Created by Tchane821 - 2024
For convert CXP files in CSV files
"""
import os
from datetime import date

# DEFINES
file_source = "./data"
file_out = "./csv"
data_start_idx = 213

print("Conversion start... pls wait")

# LIST OF FILES
files_names = [f"{file_source}/{file_name}" for file_name in os.listdir(file_source)]


# CXP TO CSV
def get_attributes(tab_txt):
    """

    :param tab_txt:
    :return:
    """
    res = dict()
    res["exe"] = ('-'.join(tab_txt[1][1].split(" ")[:3])).replace('/', '-')
    res["id"] = tab_txt[21][1]
    res["nb_samples"] = int(tab_txt[11][1])
    res["age"] = date.today().year - int(tab_txt[24][1].split("/")[2])
    res["sex"] = int(tab_txt[25][1])  # 1 = Men
    res["weight"] = int(tab_txt[26][1])
    res["height"] = int(tab_txt[27][1])
    return res


def get_data(tab_txt):
    """

    :param tab_txt:
    :return:
    """
    return tab_txt[data_start_idx:-1]


def cxp2csv(file_name):
    """

    :param file_name:
    """
    with open(file_name) as fn:
        file_stream = fn.read()
        tab_txt = [line.strip().split("\t") for line in file_stream.split("\n")]
        # for line in tab_txt:
        #     print(line)
        attributes = get_attributes(tab_txt)
        # for k in attributes.keys():
        #     print(f"{k}: {attributes[k]}")
        data = get_data(tab_txt)
        # for line in data:
        #     print(line)

    file_out_name = (f'{file_out}/{file_name.split("/")[1]}_s{attributes["nb_samples"]}_a{attributes["age"]}'
                     f'_i{attributes["id"]}_e{attributes["exe"]}_x{attributes["sex"]}'
                     f'_w{attributes["weight"]}_h{attributes["height"]}.csv')
    with open(file_out_name, 'w') as nf:
        nf.write("force;vitesse;position\n")
        for line in data:
            nf.write((';'.join(line) + '\n'))
            # nf.write((';'.join(line) + '\n').replace('.', ','))


for file_name in files_names:
    cxp2csv(file_name)

print("Conversion done !")
