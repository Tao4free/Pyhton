def wait():
    for n in range(10000000):
        print("now is {}".format(n), end='\r', flush=True)
    return n


for n in range(5):
    data = wait()
    print(data)
    # while True: 
