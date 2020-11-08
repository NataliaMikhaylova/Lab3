#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = int(input("Ведите число: "))
    b = int(input("Ведите число: "))
    c = int(input("Ведите число: "))
    if b >= a <= c:
        print(a)
    elif a >= b <= c:
        print(b)
    else:
        print(c)
    if b <= a >= c:
        print(a)
    elif a <= b >= c:
        print(b)
    else:
        print(c)
