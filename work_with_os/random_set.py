import string
import random
import time

def id_generator(size=5, chars=string.ascii_uppercase, digits=string.digits):
    data = []
    head = random.choice(chars)
    body = [random.choice(digits) for _ in range(size-1)]
    data.append(head)
    data.extend(body)
    return ''.join(data)


while True:
    nihao = id_generator(5)
    print(nihao)
    time.sleep(0.5)
