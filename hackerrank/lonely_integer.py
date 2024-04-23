def lonelyinteger(a):
    unique_values = set()

    for n in a:
        if n not in unique_values:
            unique_values.add(n)
        else:
            unique_values.remove(n)

    return list(unique_values)[0]
