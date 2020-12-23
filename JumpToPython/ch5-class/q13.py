# random 모듈을 사용하여 로또 번호(1~45 사이의 숫자 6개)를 생성해 보자(단 중복된 숫자가 있으면 안 됨.)
import random
#random.random()
#random.randint(1, 45)
#lottery = []
#for i in range(0, 6):
#    number = random.randint(1, 45)
#    if number in lottery:
#        i -= 1
#    else:
#        lottery.append(number)
#lottery.sort()
#print(lottery)
result = []
while len(result) < 6:
    num = random.randint(1, 45)
    if num not in result:
        result.append(num)

print(result)
