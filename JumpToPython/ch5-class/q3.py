# question 3. 
# filter와 lambda를 사용하여 리스트 [1, -2, 3, -5, 8, -3]에서 음수를 모두 제거해 보자.

a = [1, -2, 3, -5, 8, -3]

a = list(filter(lambda x: x >= 0, a))
print(a)
