# -*- coding: utf-8 -*-

import math

rounds = int(input())

for i in range(rounds):
    warriors = int(input())
    if warriors == 1:
        print(warriors)
    else:
        equation = (math.sqrt((warriors * 8) + 1) - 1 )/2
        print(int(equation))
