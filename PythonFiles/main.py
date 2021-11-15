import time
import numpy
import Names
import csv
import json
import _json
import threading
import time
from DoubleLinkedList import DoubleLinkedList
from DoubleLinkedList import Node

###JSON###

floorList = DoubleLinkedList()


# with open('Assignments/Ex1/data/Ex1_input/Ex1_Buildings/B5.json', 'r') as f:
#         jsonObject = json.loads(f.read())
#         x = len('elevators')
#         for i in range(x+1):
#             print("speed of "+str(i)+":")
#             print((jsonObject['_elevators'][i]["_minFloor"]))
#             print(jsonObject.get('_speed'))

###Threads###

# def p1():
#     time.sleep(3)
#     print("p1")
# def p2():
#     time.sleep(2)
#     print("p2")
# def p3():
#     time.sleep(1)
#     print("p3")
#
# x=threading.Thread(target=p1(),args=())
# x.start()
#
# y = threading.Thread(target=p2(),args=())
# y.start()
#
# z = threading.Thread(target=p3(),args=())
# z.start()
#
# print(threading.active_count())
# x.join()
#
# ####

def setbuildingName(input):
    buildingName = input
    return buildingName


def setoutputName(input):
    outputName = input
    return outputName


def setcallsName(input):
    callsName = input
    return callsName


if __name__ == '__main__':
    setbuildingName(input)
    setcallsName(input)
    setoutputName(input)


head = Node(0)
print(head.get_data())
alist = DoubleLinkedList(head)

x=-10
y=100
i = x
while(i<y):
    alist.insert_end(head.get_data()+i)
    i+=1

alist.traverse()
