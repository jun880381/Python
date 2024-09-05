# score = int(input("점수 입력 : "))
# result = ""
# if score > 90:
#     grade = "A"
# elif score > 80:
#     grade = "B"
# elif score > 70:
#     grade = "C"
# elif score > 60:
#     grade = "D"
# else:
#     grade = "F"
# result = grade
# print(f"Your grade is {result}")

print("기능 선택")
print("1. 더하기")
print("2. 빼기")
print("3. 곱하기")
print("4. 나누기")
print()

s = input("계산기 기능을 선택 하세요(1/2/3/4) : ")
num1 = int(input("첫 번째 정수를 입력하세요 : "))
num2 = int(input("두 번째 정수를 입력하세요 : "))
result = ""

if s == "+":
    result = num1 + num2
elif s == "-":
    result = num1 - num2
elif s == "*":
    result = num1 * num2
elif s == "/":
    while num2 == 0:
        num2 = int(input("0이 아닌 정수를 입력하세요 : "))
    result = num1 / num2

print(f"{num1} {s} {num2} = {result}")

