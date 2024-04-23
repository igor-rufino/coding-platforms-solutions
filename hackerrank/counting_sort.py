def countingSort(arr):
    freq = [0] * 100

    for i in range(len(arr)):
        x = arr[i]
        freq[x] = freq[x] + 1

    return freq
