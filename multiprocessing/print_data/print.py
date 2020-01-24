from multiprocessing import Process, Pool
import sys
import time

step = 5000
names = [str(i) for i in range(step)]

def print_func(dummy='Hey'):
    # print(continent, end = ' ')
    for name in names:
        sys.stdout.write('\r'+ name)
        # print(name, end = ' ')

def normal():
    for name in names:
        print_func(continent=name)

def mul():
    procs = []
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        proc = Process(target=print_func, args=(name,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()


if __name__ == "__main__":  # confirms that the code is under main function
    print("Normal loop to print")
    start_time = time.time()
    for name in names:
        print_func()
    print("\n--- %s seconds ---" % (time.time() - start_time))
    print("\n")

    print("Process loop to print")
    start_time = time.time()
    procs = []
    proc = Process(target=print_func)  # instantiating without any argument
    procs.append(proc)
    proc.start()

    # instantiating process with arguments
    for name in names:
        # print(name)
        # proc = Process(target=print_func, args=(name,))
        proc = Process(target=print_func)
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()
    print("\n--- %s seconds ---" % (time.time() - start_time))
    print("\n")

    print("Pool loop to print")
    start_time = time.time()
    p = Pool(2)
    p.map(print_func, names)
    print("\n--- %s seconds ---" % (time.time() - start_time))
    print("\n")
