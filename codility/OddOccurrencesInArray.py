def solution(A):     
    s = set()
    for val in A:
        s.add(val) if val not in s else s.remove(val)

    return list(s)[0]