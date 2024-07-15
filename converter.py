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
def get_attributes(tab_txt, f_name):
    """

    :param f_name:
    :param tab_txt:
    :return:
    """
    res = dict()
    default_value = "D00D"
    try:
        res["exe"] = ('-'.join(tab_txt[1][1].split(" ")[:3])).replace('/', '-')
    except IndexError:
        print(f"\tErr: EXE Attribute(s) is missing for {f_name}.")
        res["exe"] = default_value
    try:
        res["id"] = tab_txt[21][1]
    except IndexError:
        print(f"\tErr: ID Attribute(s) is missing for {f_name}.")
        res["id"] = default_value
    try:
        res["nb_samples"] = int(tab_txt[11][1])
    except IndexError:
        print(f"\tErr: NBSamples Attribute(s) is missing for {f_name}.")
        res["nb_samples"] = default_value
    try:
        res["age"] = date.today().year - int(tab_txt[24][1].split("/")[2])
    except IndexError:
        print(f"\tErr: AGE Attribute(s) is missing for {f_name}.")
        res["age"] = default_value
    try:
        res["sex"] = int(tab_txt[25][1])  # 1 = Men
    except IndexError:
        print(f"\tErr: SEX Attribute(s) is missing for {f_name}.")
        res["sex"] = default_value
    try:
        res["weight"] = int(tab_txt[26][1])
    except IndexError:
        print(f"\tErr: WEIGHT Attribute(s) is missing for {f_name}.")
        res["weight"] = default_value
    try:
        res["height"] = int(tab_txt[27][1])
    except IndexError:
        print(f"\tErr: HEIGHT Attribute(s) is missing for {f_name}.")
        res["height"] = default_value
    return res


def cxp2csv(file_name):
    """

    :param file_name:
    """
    with open(file_name) as fn:
        file_stream = fn.read()
        tab_txt = [line.strip().split("\t") for line in file_stream.split("\n")]
        # for line in tab_txt:
        #     print(line)
        attributes = get_attributes(tab_txt, file_name)
        # for k in attributes.keys():
        #     print(f"{k}: {attributes[k]}")
        data = tab_txt[data_start_idx:-1]
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
