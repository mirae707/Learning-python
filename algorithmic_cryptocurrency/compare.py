Num1, Num2 = input("정수 2개를 입력해주세요.").split()
num1 = int(Num1)
num2 = int(Num2)
if num1 == num2:
    print(num1, "과(와)", num2, "는 같습니다.")
elif num1 > num2:
    print(num1, "(가)이", num2, "보다 더 큽니다.")
else:
    print(num2, "(가)이", num1, "보다 더 큽니다.")
