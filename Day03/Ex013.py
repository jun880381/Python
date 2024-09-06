# name = '홍지수'
# scores = {'kor':90, 'eng':89, 'math':95, 'science':88}
# print(scores)
#
# scores['kor'] = 70
# print(scores['kor'])
#
# scores['music'] = 100
# print(scores)
#
# del scores['science']
# print(scores)
#
# print(f"이름 : {name}")
# print(f"국어 : {scores['kor']}")
# print(f"영어 : {scores['eng']}")
# print(f"수학 : {scores['math']}")

phones: dict = {"갤럭시 S5" : 2014, "갤럭시 S7" : 2016, "갤럭시 노트8" : 2017, "갤럭시 S9": 2018,}

for key in phones :
    print(phones[key])
print(len(phones))