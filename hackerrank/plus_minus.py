def plusMinus(arr):
    positives = 0
    negatives = 0
    zeros = 0
    for i in arr:
        if i > 0:
            positives = positives + 1
        elif i < 0:
            negatives = negatives + 1
        else:
            zeros = zeros + 1
    print("{:.6f}".format(positives / len(arr)))
    print("{:.6f}".format(negatives / len(arr)))
    print("{:.6f}".format(zeros / len(arr)))
