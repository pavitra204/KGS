#Threading
#single threading
from threading import Thread
import time
class Task1(Thread):
    def run(self):
        for i in range(0,5):
            print(i)
            time.sleep(2)
class Task2(Thread):
    def run(self):
        for i in range(5,0,-1):
            print(i)
            time.sleep(2)
t1=Task1()
t2=Task2()
t1.run()
t2.run()
print("Threading is completed")
print("============================================")
#multi threading
class Task1(Thread):
    def run(self):
        for i in range(5,0,-1):
            if i%2==0:
                print(i,"even")
                time.sleep(2)
            else:
                print(i,"odd")
class Task2(Thread):
    def run(self):
        for i in range(5,0,-1):
            if i%2==0:
                print(i,"even")
                time.sleep(2)
            else:
                print(i,"odd")
t1=Task1()
t2=Task2()
t1.start()
t2.start()
t1.join()
t2.join()
print("Threading is completed")




