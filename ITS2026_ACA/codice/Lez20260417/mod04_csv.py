import csv

with open("auto.csv", mode="r", newline="", encoding="utf-8") as f:
    # reader = csv.reader(f)
    reader = csv.DictReader(f)

    marche = list()
    for row in reader:
        print(row("Marca", "Nessuna"))

print(marche)