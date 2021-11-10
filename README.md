# OOP-2021-EX-1
Python Implemented Offline Elevator algorithm Project as an assignment for Object Oriented Programming Course in Ariel University -  Computer Science 

#Sources Used: 
  1. https://www.youtube.com/watch?v=BCN9mQOT3RQ
  2. https://www.youtube.com/watch?v=siqiJAJWUVg
  3. https://github.com/thevarunjain/elevator-system
  4. Ex0 Document.


#Define the Space of the Problem: 
    Within a building, given a number of smart Elevators we implement an Offline algorithm that minimizes arrival time
    (time that starts as the Passenger calls the Elevator and until he arrives at the destination). to all Passengers. 


#The Algorithm:
  let there be a building with n floors and k Elevators. 
  
  
  We divide the Elevators by Index into 2 Categories: Elevators with an odd Index number that answer up calls, Even Index ones take down calls.
  By using two Arraylists we will sort the Elevator Calls into Upcalls and Downcalls. Each arraylist will be sorted by the source floor of the call.
  Each Elevator will take the closest call that it's defined to respond to. When a call is being responded, The Selected Elevator will continue through the 
  Call's path, Responding to calls along it's path to the Destination. 
  
  Before the Elevator Calls are Given, We will "spread" the k Elevators through the n floor, for every n/k floors (whole value) we will set an Elevator Car.
  By doing that we allow Every Elevator to be able to respond to a nearby call efficiently.
  
  If only a single Elevator Exists within the Building, it will first serve the Upcalls, And when finished, The Downcalls.
