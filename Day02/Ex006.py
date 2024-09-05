# for x in range(5):
#     print(f"안녕하세요{x+1}")
#
# print("#" * 100)
#
# for x in "안녕하세요":
#     print(x)
# print("#" * 100)
# for x in ["안","녕","하","세","요"]:
#     print(x, end = "\t\t\t" )
# print("오" * 500)

# sum = 1.0
#
# for i in range(5):
#     sum *= i+1
#
# print(f"i : {i+1}, 합계 : {sum}")

# sum = 0
#
# for i in range(0,201,5):
#     sum += i
#     print(i, end=",")
#
# print(f"\n5의 배수의 합 : {sum}")
#
# for i in range(100,301):
#     if i % 3 == 0:
#         print(f"3의 배수 : {i}", end=", ")
#
# word = input("문자열을 입력하세요")
# for i in word:
#     print(i, end="\t")

for i in range(1,10):
    for j in range(1,10):
        print(f"{i} x {j} : {i*j}", end="\t")
    print()
    print("-"*107)
