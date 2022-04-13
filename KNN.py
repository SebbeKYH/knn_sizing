import pandas as pd
from math import sqrt



def get_data_frame():
    # Display all rows
    pd.set_option('display.max_rows', None)
    # Display all columns
    pd.set_option('display.max_columns', None)
    # Read the csv file to dataframe
    data_frame = pd.read_csv('./df_male_last_one.csv')
    return data_frame


def get_sizes(data_frame):
    # Store the sizes based on measurments from dataframe
    size = []
    for height, weight in zip (data_frame['height_cm'], data_frame['weight_hg']):
        if (height <= 169) & (weight <= 550):
            size.append('x-small')
        elif (height <= 178) & (weight <= 650):
            size.append('small')
        elif (height <= 182) & (weight <= 750):
            size.append('medium')
        elif (height <= 186) & (weight <= 850):
            size.append('large')
        elif (height <= 190) & (weight <= 900):
            size.append('x-large')
        elif (height <= 194) & (weight <= 950):
            size.append('xx-large')
        else:
            size.append('xxx-large')
    return size


def calculate_distance(test_row, train_row):
    # calculate the distance between points in user and dataframe
    distance = 0.0
    for i in range(len(test_row)):
        distance += (test_row[i] - train_row[i]) ** 2
    return sqrt(distance)


def get_neighbors(X_train, test_row, k_value):
    distances = list()
    for train_row in X_train:
        dist = calculate_distance(test_row, train_row)
        distances.append ((train_row, dist))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(k_value):
        neighbors.append(distances[i][0])
    return neighbors


def predict_classification(X_train, test_row, k_value):
    neighbors = get_neighbors(X_train, test_row, k_value)
    list_of_predictions = []
    for size in neighbors:
        list_of_predictions.append(size[2])
    prediction = max(set(list_of_predictions), key=list_of_predictions.count)
    return prediction


def k_nearest_nearest_neighbor(X_train, user_data, k_value):
    for row in user_data:
        output = predict_classification(X_train, user_data, k_value)
    return output


def main():
    # fething the dataframe
    python_data_frame = get_data_frame()

    # Fething the lists of sizes used later for reference
    sizes = get_sizes(python_data_frame)

    # Define y value
    y = sizes

    # Define X value
    df = pd.DataFrame(zip(python_data_frame['height_cm'],python_data_frame['weight_hg']))
    # Adding new column to dataframe
    df['Size'] = ''
    # Adding Size list to Size column in dataframe
    df['Size'] = y
    df.columns = ['height_cm', 'weight_hg', 'Size']
    # Creating a list of tuples with height, weight and Size
    X_train = list(zip(df.height_cm.tolist(), df.weight_hg.tolist(), df.Size.tolist()))



    # User input to list
    print('Enter height in cm below: ')
    user_height = int(input())
    print ('Enter weight in hg below: ')
    user_weight = int(input())
    user_data = list((user_height,user_weight))

    print('************************************')

    # Define k value for number of neighbors
    print(' Enter number of neighbors to compare with: ')
    k_value = int(input())


    print('************************************')

    # Find the nearest neighbor size
    nearest_neighbor = k_nearest_nearest_neighbor(X_train, user_data, k_value)

    # Print the nearest neighbor
    print('Recommended size for you is: '+ nearest_neighbor)


if __name__ == "__main__":
    main()
