
# ? THE MONTY HALL PROBLEM: Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

import timeit
import random

# ** WORKING CODE IF SWITCH IS TRUE =D !!!--------------------------------------------------- 11/12/19
def monty_hall(n=1):
   """A probability function to test the Monty Hall Problem."""
   count = 0
   iterations = n
   print(f'{iterations} is number of iterations.')
   if n > 1000000:
      return print(f'Sorry, you cannot iterate {n} number of times.')
   while n >= 1 and n <= 1000000:
      n = n - 1
      doors = {
         'Door1' : 'GOAT',
         'Door2' : 'GOAT',
         'Door3' : 'GOAT',}
      car_door = random.randint(0,2)
      chosen_door = random.randint(0,2)
      if car_door == 0:
         doors['Door1'] = 'CAR'
      elif car_door == 1:
         doors['Door2'] = 'CAR'
      else:
         doors['Door3'] = 'CAR'
      if chosen_door == car_door:
         count += 0
      else:
         count += 1
      # print(doors)
      # print(f'{car_door + 1} is Car Door')
      # print(f'{chosen_door + 1} is Chosen Door')
      # print(f'{count} is Count')
   probability = (count / iterations)
   print(f'{int(probability * 100)}% probability of winning the car in {iterations} chances if switching after a GOAT is revealed.')

#timeit.timeit(print(1+5))
#print(monty_hall.__doc__)


monty_hall(10000)




# doors = {
#    'door1' : 'GOAT',
#    'door2' : 'GOAT',
#    'door3' : 'GOAT'
# }

# car_door = random.randint(1, 3)
# print(car_door)

# if car_door == 1:
#    doors['door1'] = 'CAR'
# elif car_door == 2:
#    doors['door2'] = 'CAR'
# else:
#    doors['door3'] = 'CAR'
# print(doors)

# def door_reveal():
#    choice = input('DOOR 1, DOOR 2, or DOOR 3?')
#    while choice == car_door:
#       other_door = random.randint(1, 3)
#       if other_door != car_door:
#          print(other_door)
      
# door_reveal()





# if choice == car_door:

#    print(f'There\'s a GOAT in door{})
#    switch = input('Would you like to switch?: ')
#    if switch =



# choice = input("DOOR 1, DOOR 2, or DOOR 3?")
# if choice == '1' or choice == '2':
#    print(f"You chose door {choice}")
#    keep_or_not = input('Would you like to keep it or switch? Type "keep" or "switch": ')
#    if keep_or_not == 'keep':
#       print('Sorry, you get the goat!')
#    else:
#       choice = input('Which door will you chose? DOOR 2, or DOOR 3?: ')
#       if choice != '3':
#          print("Sorry, you lose. The car is behind door number 3!")
#       else:
#          print("Good thing you switched, you got the car!")
# else:
#    print("You win")


# ** MONTY HALL USING DICT--------------------------------------------------- 11/12/19
# ! NOT FUNCTIONING CODE-----------------------------------------------------

# doors = {
#    'door1' : 'GOAT',
#    'door2' : 'GOAT',
#    'door3' : 'GOAT',
# }

# def monty_hall2():
#    car_door = doors['door1']
# monty_hall2()


# ** MONTY HALL USING LIST---------------------------------------------------
# ! NOT FUNCTIONING CODE-----------------------------------------------------
# def monty_hall():
#    chosen_door = random.randint(1,3)
#    print(chosen_door)
#    car_door = None
#    doors_list = ['GOAT','GOAT','GOAT',]
#    doors_list[random.randint(0,2)] = 'CAR'
#    for i in doors_list:
#       print(i)
#    if doors_list[0] == 'GOAT' and doors_list[1]  == 'GOAT':
#       car_door = 3
#       if chosen_door == car_door:
#          print('chosen door is 3!')
#    elif doors_list[0] == 'GOAT' and doors_list[2]  == 'GOAT':
#       car_door = 2
#       if chosen_door == car_door:
#          print('chosen door is 2!')
#    else:
#       car_door = 1
#       if chosen_door == car_door:
#          print('chosen door is 1!')

# print(monty_hall())