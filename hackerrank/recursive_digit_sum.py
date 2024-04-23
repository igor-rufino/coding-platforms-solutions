def superDigit(n, k):
    def solve(n):
        if len(n) == 1:
            return n[0]

        sum = 0
        for digit in n:
            sum += int(digit)
        return solve(list(str(sum)))

    p = sum([int(digit) for digit in n]) * k
    result = solve(list(str(p)))
    return result
