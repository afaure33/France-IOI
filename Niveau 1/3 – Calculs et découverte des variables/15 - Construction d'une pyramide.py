cubetmp = 17
totalcube = 1

for loop in range(8):
    totalcube += cubetmp ** 3
    cubetmp -= 2
print(totalcube)
