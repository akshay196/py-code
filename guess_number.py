#!/usr/share/env python3

# Guess the number

from random import randint

target_number = randint(1,100)
chances = 3

while True:
    number = int(input("Enter a number from 1 to 100: "))
    if(chances == 0):
        print("No more chances left. Game over")
        break
    if(number > 100 or number < 1):
        print("Select number from 1 to 100 only")
        continue
    if(target_number == number):
        print("Correct! Game over")
        break
    if(number > target_number):
        print("Target is lesser than %d" %number)
        chances -= 1
    else:
        print("Target is bigger than %d" %number)
        chances -= 1




