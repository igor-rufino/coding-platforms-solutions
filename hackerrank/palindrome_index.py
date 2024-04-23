def palindromeIndex(s):
    n = len(s)

    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            if s[i] == s[n - 2 - i] and s[i + 1] == s[n - 3 - i]:
                return n - 1 - i
            else:
                return i
    return -1
