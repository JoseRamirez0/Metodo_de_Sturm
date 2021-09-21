# -- coding: utf-8 --
"""
Created on Fri Sep 10 10:20:40 2021
@author: José Manuel Ramírez Olivera.
"""

A = [-2, 1, 0, -4, 0, 0, 1]

def division (P1, P2):   
    while True :

        c = 0
        a = P1[len(P1) - 1] / P2 [len(P2) - 1]

        for x in range (len(P2) - 1, -1, -1):
            b = a * P2 [x]
            d = P1[(len(P1) - 1) - c] - b
            P1[(len(P1) - 1) - c] = d
            c = c + 1
        
        x = len(P1) - 1

        while P1 [x] == 0:
            P1.pop(x)
            x = x - 1
        
        if len(P1) < len (P2):
            break

    P1 = [num * -1 for num in P1]

    return P1


def derivar (pol):
    pol_2 = []

    for x in range (len(pol) - 1, 0, -1):
        pol_2.append(pol[x] * x)
    
    pol_2 = list (reversed(pol_2))
    return pol_2

def sturm (a):
    
    print (a)
    b = derivar(a)
    print (b)

    while True:
        c = division(a, b)
        print (c)

        if len (c) != 1:
            a = b 
            b = c
        else:
            break

sturm(A)