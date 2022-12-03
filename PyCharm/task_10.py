#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def cylinder():

    def circle():
        return math.pi * r ** 2

    try:
        r = float(input("Введите радиус: "))
        h = float(input("Введите высоту: "))
    except ValueError:
        return

    side = 2 * math.pi * r * h

    answer = input("1 - площадь боковой поверхности, 2 - полной?: ")
    if answer == '1':
        print(f"S боковой поверхности = {side:.2f}")
    elif answer == '2':
        print(f"S полной поверхности = {side + circle() * 2:.2f}")
    else:
        print("Вы ввели неверную команду")


if __name__ == '__main__':
    cylinder()
