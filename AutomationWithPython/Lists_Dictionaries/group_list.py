def group_list(group, users):
    members = group + ": "
    for index, factor in enumerate(users):
        if users[-1] == users[index]:
            members += users[index]
            break
        members += users[index] + ", "

    return members

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"
print(group_list("SystemManage", ["Jun", "Hesun", "Mi"]))
