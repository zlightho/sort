import logging

from smallest_index.smallest import find_smallest


def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        newArr.append(arr.pop(smallest))
    logging.info("before: ", arr)
    logging.info("after: ", newArr)
    return newArr


selectionSort([2, 3, 5, 6, 10])
