'''
Zadanie 1.1

k=y/2
z=x*k
w=x*y
nastepne y=(poprzednie)k

-----------------------------
| n |  x |  y |  k |  z | w |
| 1 | 10 | 45 | 22 |220 |145|
| 2 | 10 | 22 | 11 |110 |220|
| 3 | 10 | 11 | 5  | 50 |110|
| 4 | 10 | 5  | 2  | 20 |50 |
| 5 | 10 | 2  | 1  | 10 |20 |
| 6 | 10 | 1  | -  | -  |10 |

Zadanie 1.2
-------------
| x | y | l |
| 9 |11 | 5 |
| 8 |32 | 5 |
| 2 |47 | 9 |
|112|112| 8 |
-------------

Zadanie 1.3

z=0
dopoki y<=1 wykonuj:
    jeżeli y mod 2 = 1
        z=z+x
    x=x+x
    y=ydiv2

Zadanie 2.1
s='aaaaaaab'
k1=1
k2=2


'''


def czy_minejszy(n, s, k1, k2):
    i = k1
    j = k2
    while (i<=n and j<=n):
        if s[i-1] == s[j-1]:
            i=i+1
            j=j+1
        else:
            if s[i-1]<s[j-1]:
                return 'PRAWDA'
            else:
                return 'FAŁSZ'
    if j<=n:
        return 'PRAWDA'
    else:
        return 'FAŁSZ'

def Zadanie22():
    slowa1 = open('slowa1.txt').readlines()
    slowa2 = open('slowa2.txt').readlines()
    slowa3 = open('slowa3.txt').readlines()
    print(czy_minejszy(int(slowa1[0]), slowa1[1], int(slowa1[2].split(' ')[0]), int(slowa1[2].split(' ')[1])))
    print(czy_minejszy(int(slowa2[0]), slowa2[1], int(slowa2[2].split(' ')[0]), int(slowa2[2].split(' ')[1])))
    print(czy_minejszy(int(slowa3[0]), slowa3[1], int(slowa3[2].split(' ')[0]), int(slowa3[2].split(' ')[1])))
    print('aaa')

def Zadanie23(n, s):
    sufiksy = []
    for i in range(n):
        a = (s[i:], i+1)
        sufiksy.append(a)
    sufiksy.sort()
    wynik = []
    for i in sufiksy:
        wynik.append(i[1])
    return wynik

def Zadanie24():
    slowa = open('slowa4.txt').readlines()
    for s in slowa:
        n = int(s.split()[0])
        s = s.split()[1]
        sufiksy = []
        for i in range(n):
            sufiksy.append(s[i:])
        sufiksy.sort()
        print(sufiksy[0])

def main():
    print(Zadanie24())

main()