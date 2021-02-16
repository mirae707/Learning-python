coin = [25, 28, 32, 45, 17, 19]

def pickup_even(numbers):
    n = 0
    ret = []
    while n < len(numbers):
        if numbers[n] % 2 == 0:
            ret.append(numbers[n])
            n = n + 1
        elif numbers[n] % 2 == 1:
            n = n + 1
    return ret

print(pickup_even(coin))
