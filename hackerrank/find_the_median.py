def findMedian(arr):
    sorted_arr = sorted(arr)

    arr_len = len(arr)
    middle_len = int(arr_len / 2)

    middle_n = sorted_arr[middle_len]

    return middle_n
