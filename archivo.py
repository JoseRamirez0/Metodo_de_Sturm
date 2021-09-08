# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 10:41:29 2021
@author: Viviana Paloma Muñoz Sánchez
José Manuel Ramírez Olivera
María Fernanda Ramírez Sánchez
"""

A=[-2.0,1.0,0.0,-4.0,0.0,0.0,1.0]

def DER(B):
    Bp=[]
    for i in range(len(B)):
        Bp.append(i*B[i])
    for i in range(1,len(Bp)):
        Bp[i-1]=Bp[i]
    Bp[len(Bp)-1]=0
    return Bp

print("P0:",A)
print("P1:",DER(A))

def STURM(P0):
    x=len(P0)
    n=x-1
    #j=n
    P1=DER(P0)
    pn=[]
    #pnaux=[]
    #for i in range(x):
        #pnaux.append(0)
    for i in range(n,0,-1):
        if(P1[i-1]!=0):
            #pnaux[n]=(P0[n]/P1[n])
            aux=P0[i]/P1[i-1]
            print(aux)
            break
    for i in range(n,-1,-1):
        pn.insert(i,1)
        print(i)
    pn=[i for i in range(7)]
    print(pn)
    for i in range(4,-1,-1):
        pn[i]=4-i
    print(pn)
    
    for i in range(n-1):
        menor = i
        for j in range (i+1, n):
            if P0(n) < P0[menor]:
                menor = j
        temp = P0[menor]
        P0[menor] = P0[i]
        P0[i] = temp
    print(P0)

    
STURM(A)

