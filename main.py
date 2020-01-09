import numpy as np


def getAr(startIndex, array):
    array = array[array != 0]
    while len(array) == 1:
        return array[0]
    for i in range(startIndex, len(array), 2):
        array[i] = 0

    if array[len(array) - 1] == 0:
        return getAr(1, array)
    else:
        return getAr(0, array)


warrior=int(input("how many warrior join the war ? "))
a=np.arange(1,warrior+1)
print(getAr(1,a))
