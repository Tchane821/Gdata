import pandas as pd
import os
import sys

# DEF VALUES
SEUIL_VITESSE = 1.0
SEUIL_FORCE = 15.0

print("Analyse stats start... pls wait")

csv_file_source = "./csv"
res_file_source = "./resultats.csv"
csv_files = [f"{csv_file_source}/{fn}" for fn in os.listdir(csv_file_source)]

# Check if res file exists and create if no
res_file = open(res_file_source, "w")
res_file.write("ID;TTcorrectValues;TTFLE;TTEXT;ISOFLE;ISOEXT\n")
res_file.close()

# get speed argument, default = 230
target_speed = sys.argv[0] if len(sys.argv) > 1 else 230

for csv_file in csv_files:
    with open(csv_file, "r") as data_stream:
        df = pd.read_csv(data_stream, sep=';')
        # print(df.head())
        # print(df.dtypes)

        # Filter
        df = df[abs(df['vitesse']) > SEUIL_VITESSE]  # speed < 0.1 => delete
        df = df[abs(df['force']) > SEUIL_FORCE]  # torque < 2.0 => delete

        # Stats
        nb_ext_iso = 0
        nb_ext_tt = 0
        nb_fle_iso = 0
        nb_fle_tt = 0
        for idx, tor, spd, pos in df.itertuples():
            if spd > 0:
                nb_fle_tt += 1
                if spd >= target_speed:
                    nb_fle_iso += 1
            if spd < 0:
                nb_ext_tt += 1
                if spd <= -1 * target_speed:
                    nb_ext_iso += 1

        with open(res_file_source, "a") as res_stream:
            res_stream.write(
                f"{csv_file.split("/")[2]};{nb_ext_tt + nb_fle_tt};{nb_fle_tt};{nb_ext_tt};{nb_fle_iso};{nb_ext_iso}\n")

        string_stats = (
            f"---\n\tFor : {csv_file.split("/")[2]}\n"
            f"NB TT correct values :\t{nb_fle_tt + nb_ext_tt}\n"
            f"NB TT FLE  :\t{nb_fle_tt}\n"
            f"NB TT EXT  :\t{nb_ext_tt}\n"
            f"NB ISO FLE :\t{nb_fle_iso}\n"
            f"NB ISO EXT :\t{nb_ext_iso}\n"
            f"%% TT ISO  :\t{((nb_ext_iso + nb_fle_iso) / (nb_fle_tt + nb_ext_tt) * 100):0.3f}\n"
            f"%% FLE ISO :\t{(nb_fle_iso / nb_fle_tt * 100):0.3f}\n"
            f"%% EXT ISO :\t{(nb_ext_iso / nb_ext_tt * 100):0.3f}\n"
        )
        print(string_stats)
