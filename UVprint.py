import random

def _excute_(a, b, c):
    mx = a/2
    my = b/2
    mz = c/2
    for i in range(50):
        x = random.randint(0, a)
        y = random.randint(0, b)
        z = random.randint(0, c)

        print(str((x - mx)/a)+str((y-my)/b)+str((z-mz)/c)+'\n')

_excute_(100, 100, 100)
