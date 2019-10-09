#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import numpy

from termcolor import colored


#count array
numbers = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "60",
    "61",
    "62",
    "63",
    "64",
    "65",
    "66",
    "67",
    "68",
    "69",
    "70",
    "71",
    "72",
    "73",
    "74",
    "75",
    "76",
    "77",
    "78",
    "79",
    "80",
    "81",
    "82",
    "83",
    "84",
    "85",
    "86",
    "87",
    "88",
    "89",
    "90",
    "91",
    "92",
    "93",
    "94",
    "95",
    "96",
    "97",
    "98",
    "99",
    "100"
]


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
        print(colored(f"{str(int(output))}", "red"))


def print2():
    sortnumber = quicksort(numbers)

    # print counted numbers in array
    for sortnumber in range(len(sortnumber)):
        output = ""
        
        for n in range(len(numbers[sortnumber])):
            output = str(output + str(numbers[sortnumber][n]))
        
        # print in terminal
        print(colored(f"{str(int(output))}", "red"))


def main():
    print1()
    print2()


if __name__ == "__main__":
    main()
    sys.exit()

