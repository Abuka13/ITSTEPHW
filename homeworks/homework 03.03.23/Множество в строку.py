s = []
s = sorted(s)
a = s[0]
b = s[0]
s1 = []
s2 = []
for i in range(1,len(s)):
    if s[i] == b + 1:
        b = s[i]
    else:
        s1.append((a, b))
        a = s[i]
        b = s[i]
s1.append((a, b))
for a, b in s1:
    if a == b:
        s2.append(str(a))
    else:
        s2.append(f"{a}-{b}")
print(*s2,sep=',')















