numbers = [1, 2, 3, 4, 5]


def double(numbers: list) -> list:
    list = []
    for el in numbers:
        list.append(el * 2)
    return list


print(double(numbers))


def count_words(phrase: str):
    return len(phrase.split(','))

print(count_words("hi,my,name,is,arian"))