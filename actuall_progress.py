import csv
from _csv import reader
import math

def get_weight():
    weight = []
    with open(r'df_male_weight.csv') as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            weight.append(row[1])
    return weight

def get_height():
    height = []
    with open (r'df_male_height.csv') as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            height.append(row[1])
    return height


def main():


if __name__ == "__main__":
    main()
