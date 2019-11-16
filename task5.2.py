
def funnyString(s):
    new_s = s[::-1]

    char1_1 = list(map(ord, s))[:-1]
    char1_2 = list(map(ord, s))[1:]

    char2_1 = list(map(ord, new_s))[:-1]
    char2_2 = list(map(ord, new_s))[1:]

    res1 = [a - b for a, b in zip(char1_1, char1_2)]
    res2 = [a - b for a, b in zip(char2_1, char2_2)]

    abs_res1 = []
    abs_res2 = []

    for x in res1:
        if x < 0:
            x = abs(x)
            abs_res1.append(x)
        else:
            abs_res1.append(x)
    
    for x in res2:
        if x < 0:
            x = abs(x)
            abs_res2.append(x)
        else:
            abs_res2.append(x)

    if abs_res1 == abs_res2:
        return 'Funny'
    else:
        return 'Not Funny'
