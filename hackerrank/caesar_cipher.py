def caesarCipher(s, k):
    alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
    alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    ls = []
    for c in s:
        if c.isupper():
            ls.append(alphabet_upper[(alphabet_upper.index(c) + k) % 26])
        elif c.islower():
            ls.append(alphabet_lower[(alphabet_lower.index(c) + k) % 26])
        else:
            ls.append(c)

    encrypted_string = "".join(ls)
    return encrypted_string
