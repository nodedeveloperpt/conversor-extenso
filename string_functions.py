__author__ = 'Nuno'

def left(s, amount = 1, substring = ""):
    if (substring == ""):
        return s[:amount]
    else:
        if (len(substring) > amount):
            substring = substring[:amount]

    return substring + s[:-amount]

def right(s, amount = 1, substring = ""):
    if (substring == ""):
        return s[-amount:]
    else:
        if (len(substring) > amount):
            substring = substring[:amount]
    return s[:-amount] + substring

def mid(s, offset, amount=0):
    if amount==0:
        amount = len(s)
    return s[offset:offset+amount]

def trim(s):
    return s.strip(" ")