n = int(input())
a = []

for i in range(n):
    a.append(list(map(int, input().split())))

count = 0
m = 0
for i in range(n - 1, -1, -1): # Цикл с шагом -1
    if a[i][n - 1 - i] > m:
        m = a[i][n - 1 - i]
        count += 1
print(m)
"""
["*","*","*","*"],
    ["*","*",".","."],
    ["*",".",".","."],
    ["*",".",".","."],
"""