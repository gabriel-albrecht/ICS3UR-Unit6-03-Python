#!/usr/bin/env python3

# Created by Gabriel A
# Created on Jan 2021
# This program generates random integers and identifies the lowest

import random


def minimum(random_number):
    # this function identifies the largest integer in the list

    lowest = random_number[0]

    for loop_counter in random_number:
        if lowest <= loop_counter:
            continue
        elif lowest > loop_counter:
            lowest = loop_counter

    return lowest


def main():
    # this function uses a list

    random_number = []

    # process
    for loop_counter in range(0, 10):
        a_single_number = random.randint(0, 100)
        random_number.append(a_single_number)

    print("Here are 10 completely random numbers:\n")

    for loop_counter in range(0, 10):
        print("{0} ".format(random_number[loop_counter]), end="")

    # call functions
    number = minimum(random_number)

    # output
    print("\n\nThe lowest number in this list is: {0}".format(number))


if __name__ == "__main__":
    main()
