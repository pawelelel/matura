'''

if B[i,j] pusta
    umiesc
else
    if nr ksiazki < nr ksiazki w przegrodce
        try umiesc B[i+1,2j-1]
    else
        try B[i+1, 2j]


Zadanie 1.1

14, 18, 12, 9, 20, 15, 17

  | 1 |
-------
0 | 14| 2
-----------
1 | 12| 18| 3 | 4
-------------------
2 | 9 |   | 15| 20| 5 | 6 | 7 | 8
-----------------------------------
3 |   |   |   |   |   | 17|   |   | 9 | 10| 11| 12| 13| 14| 15| 16
-------------------------------------------------------------------
4 |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |
-------------------------------------------------------------------

Zadanie 1.2

-------------------------
1             | 1 |  1  |
--------------|---|-----|
3             | 2 |  3  |
--------------|---|-----|
4             | 3 |  4  |
--------------|---|-----|
7             | 3 |  7  |
--------------|---|-----|
16            | 5 |  16 |
--------------|---|-----|
31            | 5 |  31 |
--------------|---|-----|
32            | 6 |  32 |
--------------|---|-----|
2^k-1 dla 2>0 | k |2^k-1|
-------------------------


Zadanie 1.3

9 2 12 10 14 13 15
10 8 4 6 15 12 13
'''

def Zadanie21(n):
    b = 0
    temp = n % 2
    while(n):
        mod = n % 2
        if mod != temp:
            temp = mod
            b = b + 1
        n = n // 2
    b=b+1
    return b

def bloki(n):
    b=0
    for i in range(len(n)-1):
        if n[i] != n[i+1]:
            b=b+1
    return b+1

def Zadanie22():
    lines = open('bin.txt').readlines()

    for i in range(len(lines)):
        lines[i] = lines[i][:-1]

    licznik=0
    for line in lines:
        if bloki(line) <= 2:
            licznik = licznik+1
    return licznik

def Zadanie23():
    lines = open('bin.txt').readlines()
    max = -1
    for i in lines:
        if int(i) > max:
            max = int(i)
    return str(max)

'''
Zadanie 2.4
123
'''

def xor(a, b):
    a = bin(a)
    b = bin(b)
    xor = ''
    for i in a:

    return xor

def Zadanie25():
    lines = open('bin_przyklad.txt').readlines()
    odp = open('wyniki2_5.txt', 'w')
    for l in lines:
        a = int(l, 2) // 2
        wynik = xor(int(l), a)
        odp.write(wynik)
    odp.close()

def Zadanie31():

'''
Zadanie 4
PF

Zadanie 5
(2011)3 = (134)6
(134)5 < (134)6
(2222)3 < (1111)6
'''

if __name__ == '__main__':
    print()