from threading import Thread
from time import sleep


def cal_cube(numbers):

    print("calculating cube of numbers----------")

    for num in numbers:
        print("Cube :", num*num*num)
        sleep(1)



def cal_squire(numbers):

    print("calculating squire of numbers----------")

    for num in numbers:
        print("Squire : ", num*num)
        sleep(1)

arr = [2, 3, 4, 5, 6]
t1 = Thread(target = cal_squire, args = (arr, ))
t2 = Thread(target=cal_cube, args=(arr, ))


t1.start()
t2.start()

t1.join()
t2.join()