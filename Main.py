import threading
import time
from ast import Num
from codecs import utf_16_be_decode
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from User import *
from Windows import *
sums = []

User.userNum = input("Welcome, you need 3 players to play. Enter 3 if you do: ")
Rounds = input("How many rounds would you like to play?: ")
numRounds = int(Rounds)
for x in range(1, int(User.userNum) + 1):
    if x == 1:
        name = input("Enter user1 name: ")
        Windows.user1_name = name
        user1 = User(name)
    if x == 2:
        name = input("Enter user2 name: ")
        Windows.user2_name = name
        user2 = User(name)
    if x == 3:
        name = input("Enter user3 name: ")
        Windows.user3_name = name
        user3 = User(name)

while (numRounds >= 1):
    Cards.create_decks()
    print("the dealer has selected two cards, please play wisely and your decks have been given to you, please choose your cards without looking at them")
    res = sum(random.sample(range(1, 100), 2))
    
    print("It is "+ user1.name +" turn now, choose two cards and click on end turn")
    User.clicks = 0
    Windows.createBoard(1)
    sums.insert(0, User.sum)
    User.sum = 0
    time.sleep(1)
   
    print("It is "+ user2.name +" turn now, choose two cards and click on end turn")
    Windows.createBoard(2)
    User.clicks = 0
    sums.insert(0, User.sum)
    User.sum = 0
    time.sleep(1)

    print("It is "+ user3.name +" turn now, choose two cards and click on end turn")
    Windows.createBoard(3)
    User.clicks = 0
    sums.insert(0, User.sum)
    User.sum = 0
   
    for x in range(0, 3):
        sums[x] = sums[x] - res
    
    if sums[2] > sums[1] and sums[2] > sums[0]:
        print(user3.name + " is the winner of this round and they get a point")
        user3.count = user3.count + 1
    if sums[1] > sums[2] and sums[1] > sums[0]:
        print(user2.name + " is the winner of this round and they get a point")
        user2.count = user2.count + 1
    if sums[0] > sums[1] and sums[0] > sums[2]:
        print(user1.name + " is the winner of this round and they get a point")
        user1.count = user1.count + 1

    numRounds = numRounds - 1
    sums = []
counts = [user1.count, user2.count, user3.count]
if counts[2] > counts[1] and counts[2] > counts[0]:
        print(user3.name + " is the winner of this game with a total of " + str(user3.count) + " points")
elif counts[1] > counts[2] and counts[1] > counts[0]:
        print(user2.name + " is the winner of this game with a total of " + str(user2.count) + " points")
elif counts[0] > counts[1] and counts[0] > counts[2]:
        print(user1.name + " is the winner of this game with a total of " + str(user1.count) + " points" )
elif counts[0] == counts[2]:
    print("there was a tie between " + user1.name + " and " + user3.name + " this game")
elif counts[0] == counts[1]:
    print("there was a tie between " + user1.name + " and " + user2.name + " this game")
elif counts[1] == counts[2]:
    print("there was a tie between " + user2.name + " and " + user3.name + " this game")
    
