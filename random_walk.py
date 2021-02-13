import random


def random_walks(n):
    x = 0
    y = 0
    l = -1
    r = 1
    u = 1
    d = -1
    step = random.choice([l, r, u, d])
    for i in range(n):
        x += step
        y += step
        return (x, y)


print(random_walks(10))
