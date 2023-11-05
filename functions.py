a, b = int(input()), int(input())


def sum(a: int, b: int) -> int:
    return a + b


print(sum(a, b))

sum2 = lambda a, b: a + b
print(sum2(9 , 8))
