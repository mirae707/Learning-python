class Person:
    apples = 0
    ideas = 0

johana = Person()
johana.apples = 1
johana.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
    temp = johana.apples
    you.apples = martin.apples
    me.apples = temp
    return you.apples, me.apples

def exchange_ideas(you, me):
    temp = johana.ideas
    you.ideas = martin.ideas
    me.ideas = temp
    return you.ideas, me.ideas

exchange_apples(johana, martin)
print("Johana has {} apples and Martin has {} apples".format(johana.apples, martin.apples))
exchange_ideas(johana, martin)
print("Johana has {} ideas and Martin has {} ideas".format(johana.ideas, martin.ideas))
