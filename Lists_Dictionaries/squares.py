def squares(start, end):
    result = []
    for x in range(start, end+1):
        temp = x * x
        result.append(temp)
    return result

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
