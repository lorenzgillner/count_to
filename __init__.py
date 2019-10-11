#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import numpy
import random
from termcolor import colored


#count array
numbers = [str(x) for x in range(0, 100)]
colors = ["red", "white", "blue"]
sortnumber = []

def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort(left) + middle + quicksort(right)

def print1():
    # print counted numbers in array
    for number in range(len(numbers)):
        output = ""
        
        for n in range(len(numbers[number])):
            output = str(output + str(numbers[number][n]))
    
        # print in terminal
        print(colored(f"{str(int(output))}", colors[random.randint(0,2)]))


def print2():
    sortnumber = quicksort(numbers)

    # print counted numbers in array
    for sortnumber in range(len(sortnumber)):
        output = ""
        
        for n in range(len(numbers[sortnumber])):
            output = str(output + str(numbers[sortnumber][n]))
        
        # print in terminal
        print(colored(f"{str(int(output))}", colors[random.randint(0,2)]))


def main():
    print1()
    print2()


if __name__ == "__main__":
    main()


