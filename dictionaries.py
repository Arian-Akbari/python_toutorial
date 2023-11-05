# create an object and can work with it
# its awsome

# print(person['name'])
# print(person['shirt'])
# print(person['lovely'])

def introduce():
    person = {
        'name': 'arian',
        'shirt': True,
        'lovely': 52,
        'assets': 100,
        'dept': 50,
        'networth': lambda: person['assets'] - person['dept'],
        'fruits': ['apple', 'orange', 'milk'],
    }
    print("part1 {} part2 {} part3 {} and the networth is {} and fruits{}".format(person['name'], person['shirt'],
                                                                                  person['lovely'],
                                                                                  person['networth'](),
                                                                                  person['fruits']))
    print(person.values())
    print(list(person.keys()))

    things = {'health': 100, 'name': 'arian'}
    print(list(reversed(things)))
    things['health'] = 50
    print(things['health'])
    # dictionary is mutable -> it can be changed and altered


introduce()
