#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    x = float(input("Сколько кг собрано? x = "))

    if 0 < x < 50:
        a = 30 * x
        print(f"{a} рублей")
    elif 49 < x < 75:
        b = 50 * x
        print(f"{b} рублей")
    elif 74 < x < 90:
        v = 65 * x
        print(f"{v} рублей")
    elif x > 89:
        k = 70 * x + 20
        print(f"{k} рублей")
