t = int(input())

for i in range(t):
    a, b, c = map(int, input().split())
    total_slices = a + b + c
    if total_slices % 3 != 0:
        print(-1)
    else:
        target_slices = total_slices // 3
        moves = 0
        if a < target_slices:
            moves += target_slices - a
        if b < target_slices:
            moves += target_slices - b
        if c < target_slices:
            moves += target_slices - c
        print(moves // 2)