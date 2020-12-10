# 주어진 자연수가 홀수인지 짝수인지 판별해주는 함수(is_odd)를 작성해 보자.
def is_odd(n):
    if n % 2 == 0:
        print("The number is an even.")
    else:
        print("The number is an odd.")

number = int(input("Enter a number: "))
is_odd(number)
