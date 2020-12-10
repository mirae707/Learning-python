#!/usr/bin/env python3


def email_list(domains):
    emails = []
    for users in domains.keys():
        for user in domains[users]:
            emails.append("{name}@{domain}".format(name = user, domain = users))
    return emails

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))
