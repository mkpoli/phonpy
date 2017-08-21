# pylint: disable=C0103
# mkpoli: Hello pylint, this is a script so plz shut up :D
"""
A demonstration on phonpy.
"""
import csv
import phonpy

# Demo data is measured with Praat
# Data format based on http://lingtools.uoregon.edu/norm/norm1_help.php
file_path = "phonpy_demo.txt"

f1 = []
f2 = []
vowel = []
with open(file_path, "r", encoding="utf-16", newline="") as tsv_file:
    tsv_reader = csv.DictReader(tsv_file, delimiter="\t")
    for row in tsv_reader:
        f1.append(row["F1"])
        f2.append(row["F2"])
        vowel.append(row["vowel"])

phonpy.plot_vowels(f1, f2, vowel, standard=True)
