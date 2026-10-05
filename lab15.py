import random

n = 10

a = [round(random.uniform(-10, 10), 1) for i in range(n)]

positive = []

for x in a:
    if x > 0:
        positive.append(x)

if len(positive) > 0:
    minimum = min(positive)

    result = []

    for x in positive:
        if x == minimum:
            result.append(x)

    print("Массив:")
    print(a)

    print("Минимальные положительные элементы:")
    print(result)
else:
    print("Положительных элементов нет")
