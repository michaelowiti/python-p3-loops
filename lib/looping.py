#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
     i = 10
     while i >= 1:
        print(i)
        i -= 1
     print("Happy New Year!")


def square_integers(int_list):
    # code goes here!
    square_list=[]
    for num in int_list:
        square_list.append(num ** 2)
    return square_list    

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
