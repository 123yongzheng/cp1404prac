# A
for i in range(0, 101, 10):
    print(i, end=' ')
print()

# B
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# C
n = int(input("Number of stars: "))
for i in range(n):
    print('*', end='')
print()

# D
n = int(input("Number of stars: "))
for i in range(1, n+1):
    for j in range(i):
        print('*', end='')
    print()