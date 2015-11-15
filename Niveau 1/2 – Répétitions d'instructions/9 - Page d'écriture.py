x = "abc"

for loop1 in range(3):
    for loop2 in range(30):
        print(x[loop1:loop1 + 1], end="")
        print("_", end="")
    print()
