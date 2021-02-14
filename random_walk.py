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
    for i in range(attempts):
        num = 0
        for n in range(1, 31):
            d = random_walks(n)
            if d <= 4:
                num += 1
                print(f"For {n} steps the distance is {d}")
    print(f"Percentage = {num/attempts}")


percentage(tries)
