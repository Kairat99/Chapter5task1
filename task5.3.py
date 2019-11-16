def hackerrankInString(s):
    res = 'YES'
    for item in 'hackerrank':
        count = s.count(item)
        if count < 1:
            res = 'NO'
            break
        index = s.find(item)
        s = s[index+1:]
    return res