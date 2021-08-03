import random
from time import sleep

from client import Client

if __name__ == '__main__':
    i = Client()
    while True:
        a = random.randint(0, 4), random.randint(1, 3)
        i.send_data(*a)
        print(*a)
        sleep(1)
