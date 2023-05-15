#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i <= 10 and i > 0:
        print(i)
        i -= 1
        if i == 0:
            print ("Happy New Year!")

happy_new_year()

def square_integers(int_list):
    # code goes here!
    return [int*int for int in int_list]

def fizzbuzz():
    # code goes here!
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)
