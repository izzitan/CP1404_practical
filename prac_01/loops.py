for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 110, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

stars = int(input("Number of stars: "))
for i in range(0, stars+1, 1):
    for j in range(i):
        print("*", end="")
    print(end="\n")
print()
