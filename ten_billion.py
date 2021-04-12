# 200만원씩 투자했을 때 
# 아주 훌륭한 포트폴리오를 기준으로 연 10% 정도 수익률이 나온다고 가정하면
# 10억 모으는데 얼마나 걸릴까?

total = 0
keep = 0
print("매월 투자한 금액과 연 수익률로 10억 달성하는데 얼마난 걸리는지 계산해주는 프로그램입니다.(최대 20년치 까지 계산합니다.)\n")
month = int(input("매월 투자할 금액을 입력하세요.(만원 단위로 입력하세요. 예) 200만원 -> 200): "))
profit = int(input("목표 연 수익률을 입력하세요.(% 단위로 입력하세요. 예) 20% -> 20): "))
print(f"\n----- {month}만원씩 연 {profit}% 수익률 포트폴리오로 투자했을 경우 -----\n")
for i in range(1, 21, 1):
    total += month * 12
    total *= 1 + (profit / 100)
    total = round(total, 0)
    if 100000 < total:
        if keep == 0:
            keep = i
    if 10000 > total:
        total = int(total)
        print(f"{i}년차 잔고는 {total}만 원입니다.")
    else:
        uk = int(total / 10000)
        man = int(total % 10000)
        print(f"{i}년차 잔고는 {uk}억 {man}만 원입니다.")

if keep <= 10:
    print(f"\n축하드립니다! 10년안에 십억을 모으시겠네요.\n10억을 모으는데 걸리는 시간은 {keep}년 입니다!")
else:
    print(f"\n분발하세요! 10년안에 십억을 모으시긴 글렀습니다.\n10억을 모으는데 걸리는 시간은 {keep}년 입니다!")
