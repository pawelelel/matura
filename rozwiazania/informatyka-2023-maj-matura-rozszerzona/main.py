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

def Zadanie25():
    lines = open('bin.txt').readlines()
    odp = open('wyniki2_5.txt', 'w')
    for l in lines:
        a = int(l, 2) // 2
        wynik = int(l, 2)^a
        odp.write(str(bin(wynik)[2::]) + '\n')
    odp.close()

def Zadanie31():
    lines = open('pi.txt').readlines()
    ile = 0
    for l in range(1, len(lines)):
        jeden = int(lines[l-1])
        dwa = int(lines[l])
        if (10*jeden+dwa > 90):
            ile = ile + 1
    return ile

def Zadanie32():
    lines = open('pi.txt').readlines()
    dict = {}
    for i in range(10):
        dict['0' + str(i)] = 0
    for i in range(10, 100):
        dict[str(i)] = 0

    for l in range(1, len(lines)):
        jeden = int(lines[l-1])
        dwa = int(lines[l])
        dict[str(jeden) + str(dwa)] = dict[str(jeden) + str(dwa)] + 1

    max = -1
    maxPoz = '-1'
    min = 10000000
    minPoz = '-1'
    for i in dict:
        if dict[i] < min:
            min = dict[i]
            minPoz = i
        if dict[i] > max:
            max = dict[i]
            maxPoz = i
    print( minPoz  + ' ' + str(min))
    print( maxPoz  + ' ' + str(max))


def Zadanie33():
    ile = 0
    lines = open('pi.txt').readlines()
    for i in range(5, len(lines) - 1):
        jeden = int(lines[i - 5])
        dwa = int(lines[i - 4])
        trzy = int(lines[i - 3])
        cztery = int(lines[i - 2])
        piec = int(lines[i - 1])
        szesc = int(lines[i])
        if (jeden <= dwa and dwa <= trzy and trzy >= cztery and cztery >= piec and piec >= szesc):
            ile = ile + 1
    return ile

def CzyRosnacomalejacy(ciag):
    for i in range(1, len(ciag) // 2):
        jeden = ciag[i-1]
        dwa = ciag[i]
        if dwa < jeden:
            return False
    for i in range(len(ciag) // 2 + 1, len(ciag)):
        jeden = ciag[i - 1]
        dwa = ciag[i]
        if dwa > jeden:
            return False
    return True

def Zadanie34():
    lines = open('pi.txt').readlines()
    miejsce = -1
    ciag = ''
    najdluzszyCiag = ''
    for i in range(len(lines)):
        ciag = ''
        for j in range(i, len(lines)):
            ciag = ciag + lines[j][:1]
            if CzyRosnacomalejacy(ciag):
                if len(ciag) > len(najdluzszyCiag):
                    najdluzszyCiag = ciag
                    miejsce = i + 1
    print(miejsce)
    print(najdluzszyCiag)
    '''
    758
    113499999983
    '''
        
'''
Zadanie 4
PF

Zadanie 5
(2011)3 = (134)6
(134)5 < (134)6
(2222)3 < (1111)6
'''

def Zadanie63():
    lines = open('owoce.txt').readlines()
    lines.pop(0)

    # ilosc owocow w chlodni
    owoce = {'maliny': 0, 'truskawki': 0, 'porzeczki': 0}

    # zrobione konfiturki
    konfitury = {'malinowo-truskawkowa': 0, 'malinowo-porzeczkowa': 0, 'truskawkowo-porzeczkowa': 0}

    for l in lines:
        l = l.split('\t')
        owoce['maliny'] = owoce['maliny'] + int(l[1])
        owoce['truskawki'] = owoce['truskawki'] + int(l[2])
        owoce['porzeczki'] = owoce['porzeczki'] + int(l[3][::1])









        print(owoce)

    return -1

def Zadanie64():
    return -1

if __name__ == '__main__':
    print(Zadanie63())