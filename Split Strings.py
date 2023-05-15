def solution(s):
    lst = []
    if len(s) % 2 != 0:
        s = s + '_'
    while len(s) != 0:
        lst.append(s[:2])
        s = s[2:]
    return lst


