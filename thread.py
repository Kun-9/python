import time
import threading

def print_time():
    for i in range(100):
        time.sleep(2)
        print("name : %s, num : %d " % (threading.current_thread().getName(), i))

def print_time2():
    while(1):
        a = input()
        print("name : %s, input : %s " % (threading.current_thread().getName(), a))

if __name__ == "__main__":
    t = threading.Thread(target=print_time)
    t2 = threading.Thread(target=print_time2)
    t.start()
    t2.start()
    