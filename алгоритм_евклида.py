# 1 способ - Линейный
a = 21
b = 35
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)

print("#"*35)

# 2 способ остаток от деления
a = 345
b = 555

while b > 0:
    a, b = b, a%b
print(a)     