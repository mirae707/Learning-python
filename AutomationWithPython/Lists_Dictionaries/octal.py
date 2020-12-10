def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"), (2,"w"), (1,"x")]
    for x in [int(n) for n in str(octal)]:
        for value, letter in value_letters:
            if x >= value:
                result += letter
                x -= value
            else:
                result += "-"
    return result

print(octal_to_string(755))
print(octal_to_string(644))
print(octal_to_string(750))
print(octal_to_string(600))
print(octal_to_string(573))
