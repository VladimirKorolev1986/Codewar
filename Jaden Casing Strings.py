def to_jaden_case(string):
    l = []
    for i in string.split():
        l.append(i.capitalize())
    return ' '.join(l)

