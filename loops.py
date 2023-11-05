a = (1, 2, 3, 4, 5)
for i in a:
    print(i)
for i in enumerate(a):
    print(i)
list1 = list(a)
list1.append(99)
print(list1)

# _ MEANS it doesn't matter
for _ in range(5):
    print('sag')