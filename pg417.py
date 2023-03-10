"""How to launch a function as a separate process"""

import multiprocessing
import time

def clock(interval):
    while True:
        print("The time is %s"%time.ctime())
        time.sleep(interval)

if __name__ == "__main__":
    p = multiprocessing.Process(target=clock, args=(15,))
    p.start()