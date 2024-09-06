numbers = [[10, 20, 30], [40, 50, 60, 70, 80,], [90, 100, 110], [1542]]

for i in range(len(numbers)):
    for j in range(len(numbers[i])):
        print(numbers[i][j], end=", ")
    print()