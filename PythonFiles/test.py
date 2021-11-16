import threading
import time
import timeit


start_time = time.time()

def t1():
    time.sleep(3)
    print("t1")


def t2():
    time.sleep(4)
    print("t2")


def t3():
    time.sleep(5)
    print("t3")
    print(timeit.timeit())



x = threading.Thread(target=t1,args=())
x.start()

y = threading.Thread(target=t2,args=())
y.start()

z = threading.Thread(target=t3,args=())
z.start()

print(threading.active_count())

for i in range(3123211):
    print("xxx")

print(time.time()-start_time)