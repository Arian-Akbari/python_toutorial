# sets are used to get unique stuff
pr1 = ['ruby', 'python', 'java']
pr2 = ['ruby', 'sql', 'java']
pr3 = pr1 + pr2
print(set(pr3))
print({1, 2, 3, 2})
print('go' in pr3)
print('ruby' in pr3)


def unique(pr):
    return set(pr)


print(pr3)
print(unique(pr3))
print(list(unique(pr3)))
temp = lambda pr3: list(set(pr3))
print(temp(['a', 'a', 'b']))

# special keywords
# list , len , max , min , set , dict
