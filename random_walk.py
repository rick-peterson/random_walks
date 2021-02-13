import random


def random_walks(n):
    x = 0
    y = 0
    l = -1
    r = 1
    u = 1
    d = -1
    for i in range(n):
        step = random.choice([l, r, u, d])
        x += step
        step = random.choice([l, r, u, d])
        y += step
    return (x, y)


print(random_walks(10))
