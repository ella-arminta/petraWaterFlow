arrHasil = []
width = 3
def addBottom(array):
    arrHasil.extend(array)

def addRight(array):
    rows = len(arrHasil)
    cols = width
    for i in range(len(array)):
        arrHasil[i].extend(array[i])
        arrHasil[i] += [8] * (cols - len(array[i]))

    # supaya gk bolong
    for i in range(len(arrHasil)):
        print('loop ',i,'count ',len(arrHasil[i]))
        if len(arrHasil[i]) < len(arrHasil[0]):
            count = len(arrHasil[0]) - len(arrHasil[i])
            for j in range(count):
                arrHasil[i].append(1)
            


# arr1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# arr2 = [[0, 1, 0], [0, 1, 0], [0, 1, 0]]
# arr3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


# addBottom(arr1)
# print(arrHasil)
# for row in arrHasil:
#     print(' '.join(map(str, row)))
# # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# addBottom(arr2)
# print(arrHasil)
# for row in arrHasil:
#     print(' '.join(map(str, row)))
# # Output: [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 1, 0], [0, 1, 0]]

# addRight(arr3)
# print(arrHasil)
# for row in arrHasil:
#     print(' '.join(map(str, row)))

# addBottom([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
# addBottom([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
# addRight([[9, 9, 9], [9, 9, 9], [9, 9, 9]])
# for row in arrHasil:
#     print(' '.join(map(str, row)))
# Output:
# [[0, 0, 0, 1, 2, 3],
#  [0, 0, 0, 4, 5, 6],
#  [0, 0, 0, 7, 8, 9],
#  [0, 1, 0, 0, 0, 0],
#  [0, 1, 0, 0, 0, 0],
#  [0, 1, 0, 0, 0, 0]]