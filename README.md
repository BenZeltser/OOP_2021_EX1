

# OOP-2021-EX-1
A Python Implemented Project as an assignment for Object Oriented Programming Course in Ariel University -  Computer Science 
The issue within the the project is to take over a problem of implementing an Offline Elevator algorithm using principles
of Object-Oriented Porgramming.


**#Sources Used:** 
  1. https://www.youtube.com/watch?v=BCN9mQOT3RQ
  2. https://www.youtube.com/watch?v=siqiJAJWUVg
  3. https://github.com/thevarunjain/elevator-system
  4. Ex0 Document.



**#Define the Space of the Problem:**
    Within a building, given a number of smart Elevators we implement an Offline algorithm that minimizes arrival time
    (time that starts as the Passenger calls the Elevator and until he arrives at the destination). to all Passengers. 



**#The Algorithm:**
  let there be a building with n floors and k Elevators. 
  if K>1 
  We divide the elevetors into two groups based on their index, odd will take care of the "up calls" while even indexes will take care of "down calls"
  whenever a new call is being read by the program, it will search between all the available elevetors. assigning the elevetors with the shortest travel 
  time to the source of the call.
  If only a single Elevator Exists within the buildingClass, it will first serve the Upcalls, And when finished, The Downcalls.



**#FlowChart - a FlowChart that describes the proccess of the working classes**

![flowchart](https://user-images.githubusercontent.com/92685838/142691458-4f7fd3c9-8331-4607-9146-29425a804523.png)




**#UML Diagram that describes the classes working inside the program**

![image](https://user-images.githubusercontent.com/92685838/142691160-107d7549-f47b-4ed7-b9c3-3404987c7cdc.png)


Project Teacher by: Prof. Boaz Ben Moshe
Project Teacher Assistants: Itay lashovar, Achia Zigler
Porject authors: Ben zeltser - 313327579, Tomer Levi - 208849620
