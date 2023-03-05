def palindrome_recursion(s):
    s = s.lower()
    if len(s) < 1:
        return True
    else:
        if s[0] == s[-1]:
            return palindrome_recursion(s[1:-1])
        else:
            return False
s = 'Казак'
print(palindrome_recursion(s))
def palindrom_reverse(s):
    s = s.lower()
    if s == s[::-1]:
        return True
    else:
        return False
print(palindrom_reverse(s))
def palindrom_ukazatel(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] == s[-i-1]:
            return True
        else:
            return False
print(palindrom_ukazatel(s))



