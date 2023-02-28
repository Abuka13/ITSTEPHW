def balance(s):
    open = "("
    close = ")"
    if s.count(open) > s.count(close):
        s = str(s)
        while s.count(open) != s.count(close):
            s+=')'
    else:
        while s.count(open) != s.count(close):
            s = '(' + s
    return s
print(balance(input()))