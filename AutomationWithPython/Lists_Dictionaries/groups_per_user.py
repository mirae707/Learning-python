def groups_per_user(group_dictionary):
    user_groups = {}
    for x in group_dictionary.keys():
        for y in group_dictionary[x]:
            if y in user_groups:
                user_groups.get(y).append(x)
                continue
            #if list(user_groups.kyes()) == y:
            user_groups[y] = [x]
    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"], "public": ["admin", "userB"], "administrator": ["admin"]}))
