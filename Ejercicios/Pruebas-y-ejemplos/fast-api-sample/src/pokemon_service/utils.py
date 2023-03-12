import csv
import os


def load_from_file():
    with open(os.path.join(os.getcwd(), "resources", "pokemon.csv")) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            yield row
 