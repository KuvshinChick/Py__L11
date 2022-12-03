#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def mult():
    product = 1
    while True:
        try:
            num = int(input("Введите число: "))
        except ValueError:
            print("Вы ввели неверное число")
            return

        if num == 0:
            break
        else:
            product = product * num

    return product


if __name__ == '__main__':
    print(f"Произведение чисел: {mult()}")
