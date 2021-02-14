import random


def random_walks(n):
    x, y = 0, 0
    for i in range(n):
        dx, dy = random.choice([(-1, 0), (1, 0), (0, 1), (0, -1)])
        x += dx
        y += dy
    d = abs(x) + abs(y)
    #print((x, y), f"The distance from home is: {d}")
    return d


tries = 100


def percentage(attempts):
    for i in range(1, 31):
        num = 0
        for n in range(attempts):
            d = random_walks(i)
            if d <= 4:
                num += 1
        print(f"For {i} steps: Percentage = {float((num/attempts)*100)} %")


percentage(tries)
