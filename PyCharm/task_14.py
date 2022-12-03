#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def get_input():
    return input("Введите строку: ")


def test_input(string):
    try:
        int(string)
        return True
    except ValueError:
        return False


def str_to_int(string):
    return int(string)


def print_int(string):
    print(string)


if __name__ == '__main__':
    s = get_input()
    test_input(s)
    if test_input(s):
        str_to_int(s)
        print_int(str_to_int(s))
    else:
        print("Не число")

