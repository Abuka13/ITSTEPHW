# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(int(input())))
#TODO task2
def two(n):
    while n != 1:
        if n % 2 != 0:
            return False
        n = n // 2
    return True
print(two(int(input())))