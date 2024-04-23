def solution(N):
    bin_N_string = str(bin(N))

    gap = 0
    max_gap = 0
    count = False
    
    for b in bin_N_string[2:]:
        if b == "1" and not count:
            count = True
            gap = 0
        if b == "0" and count:
            gap = gap + 1
        if b == "1" and count:
            if gap > max_gap:
                max_gap = gap
            gap = 0

    return max_gap