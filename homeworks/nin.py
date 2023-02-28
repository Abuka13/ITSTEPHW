s = 'Hello World'
arr = []
empty = ''
for i in range(len(s)):
    arr.append(ord(s[i]))
print(arr)
arr = sorted(arr)
print(arr)
for i in range(len(arr)):
    empty+=chr(arr[i])
print(empty)
