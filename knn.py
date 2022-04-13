import math
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import neighbors
from sklearn.metrics import f1_score
from get_sizes import get_chest_sizes
from get_sizes import get_waist_sizes
from get_sizes import get_weight_sizes
from get_sizes import get_height_sizes
from get_sizes import get_data_frame


def main():
    input_length = int(input('Enter lenght in milimeters: '))
    input_weight = int(input('Enhter weight in hektograms: '))

    # Calculate euclidian distance
    nearest_neighbor = []

    df = get_data_frame()
    for length in df['height_cm']:
        delta_y = abs(input_length) - abs(length)
    for weight in df['weight_hg']:
        delta_x = abs (input_weight) - abs(weight)
    hypotenuse = delta_y ** 2 + delta_x ** 2
    nearest_neighbor.append(math.sqrt(hypotenuse))

    # Making a test - train split
    X = df['height_cm']
    Y = df['weight_hg']
    X_train, X_val, y_train, y_val = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=20)

    scaler = StandardScaler()
    scaler.fit_transform(X_train)
    scaler.transform(X_val)

    f1_list = []
    k_list = []

    print('*' * 50)

    for k in range (1, 22, 2):
        clf = neighbors.KNeighborsClassifier(n_neighbors=k, n_jobs=-1)
        clf.fit(X_train, y_train)
        pred = clf.predict(X_val)
        f = f1_score(y_val, pred, average='macro')
        print(k, '=>', f)
        f1_list.append(f)
        k_list.append(k)

    print('*' * 50)

    best_f1_score = max(f1_list)
    best_k = k_list[f1_list.index(best_f1_score)]
    print ("Optimum K value=", best_k, "with F1 score=", best_f1_score)

    KNN_model = neighbors.KNeighborsClassifier(n_neighbors=best_k, n_jobs=-1)
    KNN_model.fit(X_train, y_train)
    pred = KNN_model.predict(X_val)
    accuracy = sum(y_val == pred) / (y_val.shape[0]) * 100

    print(f'Accuracy: {int(accuracy)}%')



if __name__ == "__main__":
    main()
