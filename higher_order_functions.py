num = [1, 2, 3, 4]


def double_number(number):
    return number * 2


print(list(map(double_number, num)))

print(list(map(lambda num: num * 2, num)))
print(list(map(lambda num: num ** 2, num)))
print(list(map(lambda num: num ** num, num)))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(filter(lambda numbers: numbers % 2 == 0, numbers)))

# list comprehensions


print([number for number in numbers if number % 2 == 0])