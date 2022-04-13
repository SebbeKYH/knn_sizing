from get_sizes import get_data_frame
from math import sqrt


def euclidean_distance (row1, row2):
    distance = 0.0
    for i in range(len(row1) - 1):
        distance += (row1[i] - row2[i]) ** 2
    return sqrt(distance)


def get_neighbors(train, test_row, num_neighbors):
    entries = train.to_numpy()
    dist_values = list()

    for train_row in entries:
        dist = euclidean_distance(test_row, (train_row[0], train_row[1]))
        dist_values.append((train_row, dist))

    dist_values.sort(key=lambda tup: tup[1])
    list_neighbors = list()

    for i in range(num_neighbors):
        list_neighbors.append(dist_values[i][0])

    output_values = [row[-1] for row in list_neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction


def main():
    weight = input('Please enter your weight: ')
    height = input('Please enter your height: ')

    df = get_data_frame()
    pred = get_neighbors(df,[float(weight), float(height)], 3)

    print(pred)


if __name__ == "__main__":
    main()
