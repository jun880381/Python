# scores = [[75, 83, 90], [86, 86, 73], [76, 95, 83,], [89, 96, 69], [89, 76, 93]]
#
# for i in range(len(scores)):
#     for j in range(len(scores[i])):
#         print(scores[i][j], end=",")
#     print()
#     print("#" * 30)

strings = [['잠자리', '풍뎅이', '여치'], ['짜장면', '파스타', '피자', '국수']]
for i in range(len(strings)):
    for j in range(len(strings[i])):
        print(strings[i][j])
    print()

(x, y, z) = (10, 20, 30) # tuple
X1 = (10, 20, 30) # tuple
X2 = [10, 20, 30] # list

print(f"{type(X1)}, {type(X2)} , {type(x)}")

menu: tuple = ('짜장면', '우동', '짬뽕', '볶은밥')
print(menu)
print(menu[0])
print(menu[2])
print(menu[0:3])

tup1 = (10, 20, 30)
tup2 = (40, 50, 60)

tup3 = tup1 + tup2
print(tup3)

a = [1]
print(type(a))