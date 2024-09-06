colors = ['yellow', 'white', 'red', 'blue']



print(colors)
for i in colors:
    print(i)


sliced_colors = colors[1:]
print(sliced_colors)

numbers = list(range(0,1001))
print(numbers)

v = [1, 2, 3] # vector = v
V = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
value1 =V[0][0]
print(value1)

values1 = V[0] # scalar 타입
print(type(values1)) # 리스트 타입

for i in range(0,len(V)):
    for j in range(0,len(V[i])):
        scalar = V[i][j]
        print(scalar, end=", ")
    print()

animals = ['사자', '토끼', '하이에나', '기린']
i = 0
size = len(animals)
while i < size:
    animal = animals[i]
    print(animal, end="\t ")
    i += 1
print(type(animal))

questions = ['tr_in', 'b_s', '_axi', 'air_lane']
answer = ['a', 'u', 't', 'p']
questions_size = len(questions)
correct_count = 0
incorrect_count = 0
for i in range(questions_size):
    q = (f"{questions[i]}에서 밑줄(_) 안에 들어갈 알파벳은? ")
    ans = input(q)
    if ans == answer[i]:
        print('정답입니다!')
        correct_count += 1
    else:
        print("틀렸습니다!")
        incorrect_count += 1
print(f"정답 개수 : {correct_count}, 오답 개수 : {incorrect_count}")
