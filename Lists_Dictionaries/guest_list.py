def guest_list(guests):
    for x in guests:
        print("{name} is {age:d} years old and work as {job}.".format(name = x[0], age = x[1], job = x[2]))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])
