from sklearn.neighbors.nearest_centroid import NearestCentroid
import numpy as np
from sklearn import neighbors


def rotate(l, n):
    return l[-n:] + l[:-n]

max_len = 300

# x_data is int list
def get_knn_prediction(x_data):
    packet_collect_dir = 'packet_collect/'
    x_list = []
    y_list = []

    for i in range(1, 11):
        file_path = packet_collect_dir + 'speech%d.txt' % i
        f = open(file_path, 'r')
        for line in f:
            numbers_str = line.split(' ')[0: len(line.split(' ')) - 1]
            numbers = map(int, numbers_str)
            if len(numbers) < 20:
                continue

            for j in range(max_len - len(numbers)):
                numbers.append(0)

            x_list.append(numbers)
            y_list.append(i)

    X = np.array(x_list)
    Y = np.array(y_list)
    knn = neighbors.KNeighborsRegressor(150, weights='distance')
    clf = knn.fit(X, Y)

    if len(x_data) < max_len:
        for j in range(max_len - len(x_data)):
            x_data.append(0)

    return clf.predict([x_data])[0]
