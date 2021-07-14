# 2자리 양수(10~99) 입력받기

print('2자리 양수를 입력하세요.')

while True:
    no = int(input('값을 입력하세요.: '))
    #if no >= 10 and no <= 99:      # and 사용
    #if not(no < 10 or no > 99):    # no >= 10 and no <= 99 와 같음 (드모르간의 법칙 사용)
    if 10 <= no <= 99:              # 비교 연산자 연속으로 사용
        break

print(f'입력받은 양수는 {no}입니다.')
