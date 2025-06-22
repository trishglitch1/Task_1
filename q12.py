def is_palin(s):
    l = len(s)
    for i in range(l // 2):
       if s[i]! = s[l - 1 - i]:
           return False
    return True