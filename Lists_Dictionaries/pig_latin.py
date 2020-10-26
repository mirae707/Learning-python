def pig_latin(text):
    say = "ay "
    # Separate the text into words
    words = text.split()
    for index, word in enumerate(words):
        words[index] = word[1:] + word[0] + say
    # Create the pig latin word and add it to the list
    # Turn the list back into a phrase
    return ''.join(words)

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

def pig_latin(text):
  say = "ay"
  result = ""
  # Separate the text into words
  words = text.split()
  for word in words:
    word = word[::-1]
    word = word + say
    result += word + " "
    # Create the pig latin word and add it to the list
    # Turn the list back into a phrase
  return result
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"
