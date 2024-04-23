def miniMaxSum(arr):
    min_value = min(arr)
    max_value = max(arr)

    min_sum = sum(arr) - max_value
    max_sum = sum(arr) - min_value

    print(f"{min_sum} {max_sum}")
