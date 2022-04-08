import csv
import math
from sklearn.svm import SVC
import random
import operator

def splitting_dataset(filename, split, training_set=[], test_set=[]):
    with open ('refined_df_male_shirt.csv', 'r') as csvfile:
        lines = csv.reader(csvfile)
        data_set = list(lines)
        for x in range(len(data_set)-1):
            for y in range(4):
                data_set[x][y] = (data_set[x][y])
            if random.random() < split:
                training_set.append(data_set[x])
            else:
                test_set.append(data_set[x])

def k_distance(point_1, point_2, length):
    distance = 0
    for x in range(length):
        distance += pow((point_1[x] - point_2[x]), 2)
    return math.sqrt(distance)


def get_k_neighbour(train_set, test_point, k):
    distances = []
    lenght = len(test_point)-1
    for x in range(len(train_set)):
        dist = k_distance(test_point, train_set[x], lenght)
        distances.append((train_set[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbours = []
    for x in range(k):
        neighbours.append(distances[x][0])
    return neighbours


def get_response(neighbours_1):
    class_votes = {}
    for x in range(len(neighbours_1)):
        response = neighbours_1[x][-1]
        if response in class_votes:
            class_votes[response]+=1
        else:
            class_votes[response]=1
    sorted_votes = sorted(class_votes.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_votes

def get_accuracy(test_set, predictions):
    correct = 0
    for x in range (len(test_set)):
        if test_set[x][-1] is predictions[x]:
            correct +=1
    return (correct/float(len(test_set))) * 100.0


def main():
    with open(r'refined_df_male_shirt.csv') as csvfile:
        lines = csv.reader(csvfile)
        for row in lines:
            print(', '.join(row))

    print('***************************************************************************')

    training_set = []
    test_set = []
    splitting_dataset(r'refined_df_male_shirt.csv', 0.66, training_set, test_set)
    print('Train: ' + repr(len(training_set)))
    print ('Test: ' + repr(len(test_set)))

    print('***************************************************************************')

    data_1 = [2, 2, 2, 'a']
    data_2 = [4, 4, 4, 'b']
    distance = k_distance(data_1, data_2, 3)
    print('Distance: '+ repr(distance))

    print('***************************************************************************')

    train_set = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
    test_point = [5, 5, 5]
    k = 1
    neighbours = get_k_neighbour(train_set, test_point, 1)
    print(neighbours)

    print('***************************************************************************')

    neighbours_1 = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3, 'b']]
    print(get_response(neighbours_1))

    print('***************************************************************************')

    test_set = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
    predictions = ['a', 'a', 'a']
    accuracy = get_accuracy(test_set, predictions)
    print(accuracy)

if __name__ == "__main__":
    main()
