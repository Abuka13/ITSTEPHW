def balance(s):
    open = "("
    close = ")"
    if s.count(open) > s.count(close):
        while s.count(open) != s.count(close):
            s.replace('(','')
    else:
        while s.count(open) != s.count(close):
            s.replace(')','')
    return s
print(balance(input()))