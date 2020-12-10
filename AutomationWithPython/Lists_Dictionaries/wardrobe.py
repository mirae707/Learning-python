wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for x in wardrobe.keys():
    for y in wardrobe[x]:
        print("{color} {clothes}".format(color = y, clothes = x))
