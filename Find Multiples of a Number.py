def find_multiples(integer, limit):
    lst = []
    for i in range(integer, limit + 1):
        if i % integer == 0:
            lst.append(i)
    return lst


print(find_multiples(1, 2))
