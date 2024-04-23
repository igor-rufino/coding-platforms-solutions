def diagonalDifference(arr):
    arr_len = len(arr)

    left_to_right = 0
    right_to_left = 0

    for i in range(arr_len):
        left_to_right += arr[i][i]
        right_to_left += arr[i][arr_len - i - 1]

    return abs(left_to_right - right_to_left)
