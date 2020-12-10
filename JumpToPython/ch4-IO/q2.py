# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
def avg(*args):
    total = 0
    for i in args:
        total += i
    return total / len(args)

print(avg(1, 2, 3, 4, 5, 6, 7))
