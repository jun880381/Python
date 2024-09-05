# sum = 0;
# i = 1
# while i < 101:
#     sum += i
#     print(f"i 의 값 : {i}, 합계 : {sum}")
#     i += 1
#
s = "Python is widely used by a number of big companies"
i = 0
count = 0

while i < len(s.lower()):
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
        count += 1
        print(f"{s[i]}", end=", ")
    i += 1
print(f"모음 : {count}")