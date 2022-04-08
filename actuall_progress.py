import csv
from _csv import reader
import math

def get_data_frame():
    data_frame = []
    with open(r'df_male_round.csv') as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            data_frame.append(row)
    return data_frame

def get_sizes(data_frame):
    sizes = []
    for size in data_frame['chest_height_mm']:
        if data_frame <= 736:
            sizes.append('Small')



def main():
    data_frame = get_data_frame()
    print(get_sizes(data_frame))


if __name__ == "__main__":
    main()
