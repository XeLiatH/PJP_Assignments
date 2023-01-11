from threading import Thread
import time


def my_timer(name, delay, repeat):
    print("Timer {} started".format(name))
    while repeat > 0:
        time.sleep(delay)
        print("{} : {}".format(name, str(time.time())))
        repeat -= 1

    print("Timer {} has completed".format(name))
    

def main():
    th1 = Thread(target=my_timer, args=("cislo 1", 3, 5))
    th2 = Thread(target=my_timer, args=("cislo 2", 1, 2))

    th1.start()
    th2.start()

    print("\n Main task completed" )

if __name__ == '__main__':
    main()           