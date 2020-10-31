f = open("sample.txt")
lines = f.readlines()
f.close()

total = 0
for line in lines:
    score = int(line)
    total += score

average = total / 10

f = open("result.txt", 'w')
f.write(str(average))
f.close
