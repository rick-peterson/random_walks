import random


def random_walks(n):
    x, y = 0, 0
    for i in range(n):
        dx, dy = random.choice([(-1, 0), (1, 0), (0, 1), (0, -1)])
        x += dx
        y += dy
    return (x, y)


print(random_walks(10))
