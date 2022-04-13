import pandas as pd
import math
from math import sqrt
from scipy.spatial import distance


def get_data_frame():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    data_frame = pd.read_csv('./df_male_last_one.csv')
    return data_frame


def get_sizes(data_frame):
    size = []
    for height, weight in zip (data_frame['height_cm'], data_frame['weight_hg']):
        if 170 <= height < 178 & weight <= 550 < 650:
            size.append('small')
        elif 174 >= height < 182 & weight <= 650 < 750:
            size.append('medium')
        elif 1076 >= height < 186 & weight <= 750 < 850:
            size.append('large')
        elif 178 <= height < 190 & weight <= 850 < 900:
            size.append('x-large')
        elif 180 <= height < 194 & weight <= 900 < 950:
            size.append('xx-large')
        elif height > 196 & weight > 1000:
            size.append('xxx-large')
        elif height < 169 & weight < 550:
            size.append('x-small')
    return size


def calculate_distance(user_data, X_train):
    distance = 0.0
    for i in range(len(user_data)-1):
        distance = (user_data[i] - X_train[i]) ** 2
    return sqrt(distance)

def get_neighbors(X_train, user_data, k_value):
    distances = []
    for train_row in X_train:
        dist = calculate_distance(user_data, train_row)
        distances.append ((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(k_value):
        neighbors.append(distances[i][0])
    return neighbors


#def knn(k, X_train, y, user_data):
#    distances = []
#    for i, df_data in enumerate(X_train):
#        dist = calculate_distance(df_data, user_data)
#        distances.append({'distance': dist, 'size': y[i]})
#    distances.sort(key=lambda data: data['distance'])
#    distances = distances[:k]


def main():
    # fething the dataframe
    python_data_frame = get_data_frame()

    # Fething the lists of sizes used later for reference
    sizes = get_sizes(python_data_frame)

    # Define X value
    df = pd.DataFrame(zip(python_data_frame['height_cm'],python_data_frame['weight_hg']))
    df.columns = ['height_cm', 'weight_hg']


    X_train = list(zip(df.height_cm.tolist(), df.weight_hg.tolist()))

    # Define y value
    y = sizes

    # Define k value for number of neighbors
    k_value = 3

    # User input to array
    user_height = int(input())
    user_weight = int(input())
    user_data = [user_height,user_weight]

    # Fething the euclidian distance between values in set and user value
    neighbors = get_neighbors(X_train, user_data, k_value)
    print(neighbors)




    # Input user information
    #user_height = input('Enter user height in cm : ')
    #user_weight = input('Enter user weight in kg: ')
    #user_weight = int(user_weight)
    #user_weight_hg = (user_weight*10)

    #nearest_neighbor = []
    #for length, weight in zip(python_data_frame['height_cm'], python_data_frame['weight_hg']):
    #    delta_y = abs(user_height) - abs (length)
    #    delta_x = abs(user_weight_hg) - abs (weight)
    #    hypotenuse = delta_y **2 + delta_x **2
    #    nearest_neighbor.append(math.sqrt(hypotenuse))


if __name__ == "__main__":
    main()
