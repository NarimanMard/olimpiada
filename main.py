import csv
""" Импортируем м"""
with open('space.txt', encoding="utf8") as file, open("spase_new", "w", encoding='utf8', newline='') :
    r = csv.DictReader(file, delimiter= '*')
    for row in r:
        w = csv.DictReader(file,)
        print(row)
