filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
for index, factor in enumerate(filenames):
    if factor[-3:] == "hpp":
        factor = factor.replace("hpp", "h")
        filenames[index] = factor

print(filenames)
