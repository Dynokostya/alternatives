import numpy as np


def find_way(arr: np.array):
    res = np.zeros((arr.shape[0], arr.shape[1]), dtype=int)

    # Start at the left down corner
    j = 0
    i = arr.shape[0] - 1
    res[i, j] = 1
    while i > 0 and j < arr.shape[1] - 1:
        temp = np.array([arr[i - 1, j], arr[i, j + 1], arr[i - 1, j + 1]])
        way = np.argmax(temp)
        if way == 0:
            res[i - 1, j] = 1
            i -= 1
        elif way == 1:
            res[i, j + 1] = 1
            j += 1
        else:
            res[i - 1, j + 1] = 1
            i -= 1
            j += 1
    if i == 0 and j < arr.shape[1] - 1:
        while j != arr.shape[1] - 1:
            res[i, j + 1] = 1
            j += 1
    if i != 0 and j == arr.shape[1] - 1:
        while i != 0:
            res[i - 1, j] = 1
            i -= 1
    return res


def main(rows, cols, max_value, min_value):
    data = np.random.randint(min_value, max_value + 1, size=(rows, cols))
    for row in data:
        print('  '.join([f'{elem:2d}' for elem in row]))
    print()
    res = find_way(data)
    for row in res:
        print('  '.join([f'{elem:2d}' for elem in row]))


main(5, 5, 20, -20)
