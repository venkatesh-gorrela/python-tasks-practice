# '''
# Process:
# The process is a program (set of instructions) in execution
# Process cannot share the memory

# Thread:
# Thread is light-weight processes
# Threads can be used to perform complicated tasks in the background without interrupting the main program.
# Threads can Share the memory

# run():is the entry point for a thread.

# start():method starts a thread by calling the run method.

# join([time]):waits for threads to terminate.

# isAlive():method checks whether a thread is still executing.

# getName():method returns the name of a thread.

# '''































# import threading
# from threading import *
# from time import sleep
# class Thread1(Thread):
#     def run(self):
#         for i in range(10):
#             print("This is 1st venky 1",i)
#             sleep(4)
# class Thread2(Thread):
#     def run(self):
#         for i in range(10):
#             print("This is 2nd hardik 2",i)
#             sleep(4)
# class Thread3(Thread):
#     def run(self):
#         for i in range(10):
#             print("This is 3rd venky 3",i)
#             sleep(4)
# class Thread4(Thread):
#     def run(self):
#         for i in range(10):
#             print("This is 4rth hardik 4",i)
#             sleep(4)
# t1=Thread1()
# t2=Thread2()
# t3=Thread3()
# t4=Thread4()
# t1.start()
# sleep(1)
# t2.start()
# sleep(1)
# t3.start()
# sleep(1)
# t4.start()





# import threading
# from threading import *
# from time import sleep
# class Thread1(Thread):
#     def run(self):
#         for i in range(10):
#             print("This is 1st venky 1",i)
#             sleep(4)
# class Thread2(Thread):
#     def run(self):
#         for i in range(10):
#             print("This is 2nd hardik 2",i)
#             sleep(4)
# t1=Thread1()
# t2=Thread2()
# t1.start()
# print(t1.is_alive())
# t1.join()
# print(t1.is_alive())
# sleep(1)
# t2.start()















# import threading
# print(threading.current_thread().getName())

















import threading
from threading import *
from time import sleep
class Thread1(Thread):
    def run(self):
        for i in range(10):
            print("This is 1st venky  1",i)
            sleep(2)
class Thread2(Thread):
    def run(self):
        for i in range(10):
            print("This is 2nd hardik 2",i)
            sleep(2)
t1=Thread1()
t2=Thread2()
t1.start()
sleep(1)
t2.start()
       
























