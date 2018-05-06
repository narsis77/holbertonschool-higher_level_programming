#!/usr/bin/python3
"""Module containing a function that prints two strings as a name"""


def say_my_name(first_name, last_name=""):
    """Prints two strings as a name"""
    print("My name is", end = " ")
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    print(first_name, end=" ")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print (last_name)
