'''
No dobra, no to w tym pliku jest rozwiazanie wszystkich (mam nadzieje) zadan z tego pdf

na samym koncu jest funkcja main, w ktorej mozna wywolac kazda funkcje ktora jest rozwiazaniem zadania
oczywiscie najpierw wypada ja tam wywolac ale mam nadzieje ze bedziesz na tyle inteligentny by to zrobic

Template tabelki:

-------------------------
|   a   |   b   |   c   |
|-------+-------+-------|
|       |       |       |
|-------+-------+-------|
|       |       |       |
|-------+-------+-------|
|       |       |       |
-------------------------
'''

#Rozdzial 1

# Zadanie 1

def wyniki(i):
    if i < 3:
        return 1
    else:
        if i % 2 == 0:
            return wyniki(i - 3) + wyniki(i - 1) + 1
        else:
            return wyniki(i - 1) % 7

'''
Zadanie 1.1

----------------
| i | wynik(i) |
|---+----------|
| 1 |     1    |
|---+----------|
| 2 |     1    |
|---+----------|
| 3 |     1    |
|---+----------|
| 4 |     3    |
|---+----------|
| 5 |     3    |
|---+----------|
| 6 |     5    |
|---+----------|
| 7 |     5    |
|---+----------|
| 8 |     9    |
----------------
'''

'''
Zadanie 1.2

----------------
| i |   E(i)   |
|---+----------|
| 0 |     1    |
|---+----------|
| 3 |     1    |
|---+----------|
| 5 |     2    |
|---+----------|
| 7 |     3    |
|---+----------|
| 9 |     5    |
|---+----------|
|10 |     8    |
----------------

E(0) = E(1) = E(2) = 1
E(i) = E(i - 1) + E(i - 3) dla i > 2 && i mod 2 = 0
E(i) = E(i - 1) dla i > 2 && i mod 2 = 1
'''

'''
Zadanie 1.3

W[0] ← 1
W[1] ← 1
W[2] ← 1
max_wart ← 1
    dla i = 3, 4, …, 1 000 wykonuj
        jeżeli i mod 2 = 0
            W[i] ← W[i-3] + W[i-1] + 1
        w przeciwnym razie
            W[i] ← W[i-1] mod 7
        jeżeli W[i] > max_wart
            w[i] ← max_wart

zwróć max_wart
'''

#Zadanie 2

def binarny(x, k):
    print('0.', end="")
    y = x
    for i in range(1, k):
        print(y)
        if y >= 0.5:
            print('1', end="")
        else:
            print('0',  end="")
        y = y * 2
        if y >= 1:
            y = y - 1

'''
Zadanie 2.1

-------------------------------------------
| kolejne wykonianie | wartosc zmiennej y |
|--------------------+--------------------|
|          1         |         0.6        |
|--------------------+--------------------|
|          2         |         0.2        |
|--------------------+--------------------|
|          3         |         0.4        |
|--------------------+--------------------|
|          4         |         0.8        |
|--------------------+--------------------|
|          5         |         0.6        |
-------------------------------------------

liczba wypisana przez algorytm: 0.1001
'''

'''
Zadanie 2.3

funkcja trójkowy(x, k)
    wypisz „0,”
    y ← x
    dla i = 1, 2, ..., k wykonuj
        jeżeli y ≥ 2/3
            wypisz „2”
        jeżeli y >= 1/3 and y < 2/3
            wypisz „1”
        jeżeli y < 1/3
            wypisz „0”
        y = y * 3
        jeżeli y≥2
            y = y - 1
        jeżeli y≥1
            y = y - 1
'''

# Zadanie 3

def F(x, n):
    if n == 1:
        return x
    else:
        if n % 3 == 0:
            k = F(x, n // 3)
            return k*k*k # *
        else:
            return x * F(x, n - 1) # **

'''
Zadanie 3.1

--------------------
| wywoanie | wynik |
|----------+-------|
| F(2, 10) | 1024  |
|----------+-------|
| F(2, 9)  |  512  |
|----------+-------|
| F(2, 3)  |   8   |
|----------+-------|
| F(2, 1)  |   2   |
|----------+-------|
|          |       |
|----------+-------|
|          |       |
--------------------
'''

'''
Zadanie 3.2

-------------------------
| x | n | wynik F(x, n) |
|---+---+---------------|
| 2 | 2 |       4       |
|---+---+---------------|
| 2 | 3 |       8       |
|---+---+---------------|
| 3 | 4 |      81       |
|---+---+---------------|
| 2 | 5 |      32       |
|---+---+---------------|
| 2 | 8 |     256       |
|---+---+---------------|
| 2 |10 |     1024      |
-------------------------
'''

'''
Zadanie 3.3

------------------------------------
| x | n | Liczba operacji mnozenia |
|-------+--------------------------|
| 2 | 2 |            1             |
|---+---+--------------------------|
| 2 | 3 |            2             |
|---+---+--------------------------|
| 3 | 4 |            3             |
|---+---+--------------------------|
| 4 | 7 |            4             |
|---+---+--------------------------|
| 4 | 8 |            5             |
|---+---+--------------------------|
| 4 | 9 |            4             |
------------------------------------
'''

'''
Zadanie 3.4

2 * log3 n
'''

# Zadanie 4

'''
Zadanie 4.1

-----------------------------------------------------------------------
|   Liczba w systemie silniowym   |   Liczba w systemie dziesietnym   |
|---------------------------------+-----------------------------------|
|              (310)!             |         3*3!+1+2!+0*1!=20         |
|---------------------------------+-----------------------------------|
|              (2011)!            |      2*4!+0*3!+1*2!+1*1!=51       |
|---------------------------------+-----------------------------------|
|             (54211)!            |   5*5!+4*4!+2*3!+1*2!+1*1!=711    |
-----------------------------------------------------------------------
'''

'''
Zadanie 4.2

(54321)!
'''

'''
Zadanie 4.3

-----------------------------------
|   x   | k | x div k! | x mod k! |
|-------+---+----------+----------|
|  5489 | 7 |     1    |   449    |
|-------+---+----------+----------|
|  449  | 6 |     0    |   449    |
|-------+---+----------+----------|
|  449  | 5 |     3    |   89     |
|-------+---+----------+----------|
|  89   | 4 |     3    |    17    |
|-------+---+----------+----------|
|  17   | 3 |     2    |    5     |
|-------+---+----------+----------|
|   5   | 2 |     2    |    1     |
|-------+---+----------+----------|
|   1   | 1 |     1    |    0     |
-----------------------------------

5489 = (1033221)!`
'''

# 4.4
def ZapisSilniowy(x):
    silnia = 1
    k = 1
    while silnia < x:
        k = k + 1
        silnia = silnia * k
    if silnia > x:
        silnia = silnia // k
        k = k - 1
    s = ""
    while k > 0:
        cyfra = x // silnia
        s = s + str(cyfra)
        x = x % silnia
        silnia = silnia // k
        k = k - 1
    return s


# Zadanie 5

# Jak latwo zauwazyc w pythonie odejmuje jeden przy operacji na tablicy
# poniewaz w pseudokodzie uznali ze tablice zaczynaja sie od 1
def sortowaniePrzezWstawianie1(n, A):
    for j in range(n - 1, 0, -1):
        x = A[j-1]
        p = j
        k = n + 1
        while k - p > 1:
            i = (p + k) // 2
            if x <= A[i-1]:
                k = i
            else:
                p = i
        for i in range(j, p):
            A[i-1] = A[i]
        A[p-1] = x
    return A

'''
Algorytm
    dla j = n – 1, n – 2, … , 1 wykonuj
        x ← A[j]
        p ← j
        k ← n + 1
        dopóki k – p > 1 wykonuj
            i ← (p + k) div 2
            jeżeli x ≤ A[i]
                k ← i // *
            w przeciwnym razie
                p ← i // *
        dla i = j, j + 1, … , p – 1 wykonuj
            A[i] ← A[i + 1]
        A[p] ← x
'''

'''
Zadanie 5.1
12, 4, 3, 10, 5, 11

------------------------------
|           | Liczba wykonan |
| Wartosc j |----------------|
|           | k = i  | p = i |
|-----------|--------|-------|
|     5     |   1    |   0   |
|-----------|--------|-------|
|     4     |   1    |   1   |
|-----------|--------|-------|
|     3     |   2    |   0   |
|-----------|--------|-------|
|     2     |   1    |   1   |
|-----------|--------|-------|
|     1     |   0    |   3   |  
------------------------------
'''

'''
Zadanie 5.2

Algorytm:
    dla j = n – 1, n – 2, … , 1 wykonuj
        x ← A[j]
        i ← j + 1
        dopóki (i ≤ n) i (x > A[i]) wykonuj
            A[i – 1] ← A[i]
            i ← i + 1
        A[i - 1] ← x
'''
# ten sam problem jak w sortowaniu powyzej
def sortowaniePrzezWstawianie2(n, A):
    for j in range(n - 1, 0, -1):
        x = A[j - 1]
        i = j + 1
        while i <= n and x > A[i - 1]:
            A[i - 2] = A[i - 1]
            i = i + 1
        A[i - 2] = x
    return A

'''
Zadanie 5.3

-----------------
|   P   |   F   |
|-------+-------|
|       |   x   |
|-------+-------|
|   x   |       |
|-------+-------|
|   x   |       |
|-------+-------|
|   x   |       |
-----------------

'''


# Zadanie 6


'''
Algorytm 1:
    n ← 1
    dla i=1,2,…,k wykonuj
        n ← 2⋅n
    s ← 1
    dopóki s<n wykonuj
        j ← 1
        dopóki j<n wykonuj
(*)         jeżeli A[j]>A[j+s]
(**)            zamień(A[j],A[j+s])
            j ← j+2⋅s
        s ← 2⋅s
    zwróć A[1]

'''

def dziwnymergesort1(k, A):
    n = 1
    for i in range(k):
        n = 2 * n
    s = 1
    while s < n:
        j = 1
        while j < n:
            if A[j - 1] > A[j + s - 1]: # *
                A[j - 1], A[j + s - 1] = A[j + s - 1], A[j - 1] # **
            j = j + 2 * s
        s = 2 * s
    return A

'''
Zadanie 6.1

-----------------------------------------------------------
| k |         Zaw pocz         |         Zaw konc         |
|---+--------------------------+--------------------------|
| 2 | [4, 3, 1, 2]             | [1, 4, 3, 2]             |
|---+--------------------------+--------------------------|
| 2 | [2, 3, 4, 1]             | [1, 3, 2, 4]             |
|---+--------------------------+--------------------------|
| 3 | [1, 2, 3, 4, 5, 6, 7, 8] | [1, 2, 3, 4, 5, 6, 7, 8] |
|---+--------------------------+--------------------------|
| 3 | [8, 7, 6, 5, 4, 3, 2, 1] | [1, 8, 7, 6, 5, 4, 3, 2] |
|---+--------------------------+--------------------------|
| 3 | [4, 5, 6, 1, 8, 3, 2, 4] | [1, 5, 4, 6, 2, 8, 3, 4] |
-----------------------------------------------------------

Zadanie 6.2
-----------------
|   P   |   F   |
|-------+-------|
|       |   x   |
|-------+-------|
|       |   x   |
|-------+-------|
|   x   |       |
-----------------

Zadanie 6.3
-----------------
|   P   |   F   |
|-------+-------|
|   x   |       |
|-------+-------|
|       |   x   |
|-------+-------|
|   x   |       |
|-------+-------|
|       |   x   |
-----------------

Zadanie 6.4

Algorytm 2:
    n ← 1
    dla i=1,2,…,k wykonuj
        n ← 2⋅n
    s ← 1
    dopóki s<n wykonuj
        j ← 1
        dopóki j<n wykonuj
(*)         jeżeli A[j]>A[j+1]
                zamień(A[j],A[j+1])
            j ← j+1
        s ← s+1
    zwróć A[1], A[2],…,A[n]
    
    

Po zakończeniu działania algorytmu 2 element A[i] jest mniejszy lub rowny
niż element A[i+1] dla każdego i większego od 0
oraz mniejszego od n

Wiersz (*) algorytmu 2 wykonywany będzie w przebiegu algorytmu
wiecej niż n razy,
mniej niż n2 razy.

'''

def dziwnymergesort2(k, A):
    temp = 0
    n = 1
    for i in range(k):
        n = 2 * n
    s = 1
    while s < n:
        j = 1
        while j < n:
            temp += 1
            if A[j - 1] > A[j]: # *
                A[j - 1], A[j] = A[j], A[j - 1]
            j = j + 1
        s = s + 1
    print(temp)
    return A


# Zadanie 7

def uporzadkuj(T, kosztowneOperacje):
    n = len(T)
    if n == 1:
        return T
    k = int(n / 2)
    A = uporzadkuj(T[:k], kosztowneOperacje)
    B = uporzadkuj(T[-k:], kosztowneOperacje)
    return scal(A, B, kosztowneOperacje)

def scal(A, B, kosztowneOperacje):
    kosztowneOperacje[0] += (2 * len(A) - 1)
    C = A + B
    C.sort()
    return C

'''
Zadanie 7.1

T = [ 15, 11 ] => [11, 15] 
T = [ 1, 3, 8 ] => Bledna specyfikacja
T = [ 8, 4, 2, 1] => [1, 2, 4, 8]
T = [ 10, 15, 1 , 6, 9, 2, 5, 90 ] => [1, 2, 5, 6, 9, 10, 15, 90]

Zadanie 7.2

            8, 80, 90, 14, 3, 5, 20, 10, 5, 6, 90, 34, 11, 13, 56, 9
        8, 80, 90, 14, 3, 5, 20, 10    |    5, 6, 90, 34, 11, 13, 56, 9
      8, 80, 90, 14 | 3, 5, 20, 10           5, 6, 90, 34 | 11, 13, 56, 9
    8, 80 | 90, 14    3, 5 | 20, 10           5, 6 | 90, 34    11, 13 | 56, 9
   8 | 80 | 90 | 14 | 3 | 5 | 20 | 10 | 5 | 6 | 90 | 34 | 11 | 13 | 56 | 9
   
Zadanie 7.3
49
kosztowneOperacje = [0]
print(uporzadkuj([ 8, 80, 90, 14, 3, 5, 20, 10, 5, 6, 90, 34, 11, 13, 56, 9 ], kosztowneOperacje))
'''


# Zadanie 8

def DwaCiagi(A, B, x, n):
    i = 1
    j = n
    while i <= n and j > 0:
        while i <= n and j > 0:
            if A[i - 1] + B[j - 1] == x: # *
                return True
            else:
                if A[i - 1] + B[j - 1] < x:
                    i = i + 1
                else:
                    j = j - 1
    return False

'''
Algorytm ten sprawdza czy istnieje taka para liczb z tablic A i B ktora jest rowna x

    i←1
    j←n
    dopóki (i ≤ n oraz j > 0) wykonuj
        dopóki (i ≤ n oraz j > 0)wykonuj
(*)         jeżeli A[i] + B[j] = x
                podaj wynik PRAWDA i zakończ algorytm
            w przeciwnym razie
                jeżeli A[i] + B[j] < x
                    i← i + 1
                w przeciwnym razie
                    j← j – 1
    podaj wynik FAŁSZ
    
Zadanie 8.1
-------------------------
| wynik | liczba krokow |
|-------+---------------|
| Falsz |      7        |
|-------+---------------|
|Prawda |      2        |
-------------------------

Zadanie 8.2
prawda gdy A[cos] + B[cos] == x
falsz gdy A[kazdy] + B[kazdy] != x

Zadanie 8.3
DwaCiagi([1, 1, 1, 1, 15], [1, 1, 1, 5, 10], 20, 5)
'''

# Zadanie 9

'''
Zadanie 9.1
---------------------------------
|   n   |   x   |   y   |   z   |
|-------+-------+-------+-------|
|   3   |   A   |   B   |   C   |
|-------+-------+-------+-------|
|   2   |   A   |   C   |   B   |
|-------+-------+-------+-------|
|   1   |   A   |   B   |   C   |
|-------+-------+-------+-------|
|   1   |   B   |   C   |   A   |
|-------+-------+-------+-------|
|   2   |   C   |   B   |   A   |
|-------+-------+-------+-------|
|   1   |   C   |   A   |   B   |
|-------+-------+-------+-------|
|   1   |   A   |   B   |   C   |
--------------------------------|

Zadanie 9.2
A => B; A => C; B => C; A => B; C => A; C => B; A => B

Zadanie 9.3
-----------------
|   n   | H(n)  |
|-------+-------|
|   1   |   1   |
|-------+-------|
|   2   |   3   |
|-------+-------|
|   3   |   7   |
|-------+-------|
|   4   |  15   |
|-------+-------|
|   5   |  31   |
|-------+-------|
|   7   |  127  |
|-------+-------|
|  10   | 1023  |
-----------------
H(n) = 2^n - 1

Zadanie 9.3
A => C; A => B C => B; A => C; B => A; B => C; A => C; A => B; C => B; C => A; B => A; C => B; A => C; A => B; C => B
'''


# Zadanie 10

def obliczaniePoooootegi(n, x):
    Z = []
    Z.append(x)
    m = 1
    w = 2
    while w < n:
        Z.append(Z[m - 1] * Z[m - 1])
        m = m + 1
        w = 2 * w
    return Z

'''
Z[0] ← x
m ← 1
w ← 2
dopóki w < n wykonuj
    Z[m] ← Z[m − 1] ⋅ Z[m − 1]
    m ← m + 1
    w ← 2 ⋅ w

Zadanie 10.1
[2, 4, 16, 256]

Zadanie 10.2
-------------------
|   n  | operacje |
|------+----------|
|   1  |    0     |
|------+----------|
|   2  |    1     |
|------+----------|
|   4  |    3     |
|------+----------|
|   8  |    7     |
|------+----------|
|  16  |    15    |
|------+----------|
| 1024 |   1023   |
-------------------
f(n) = 2 * f(n / 2) + 1

Zadanie 10.3

9, 1, 0, -6, 0, 10, 0, 2, 0, 4, -1, 0, 0, 0, -3, 5
    9, 1, 0, -6, 0, 10, 0, 2
        9, 1, 0, -6
            9, 1
                9
                1
            0, -6
                0
                -6
        0, 10, 0, 2
            0, 10
                0
                10
            0, 2
                0
                2
    0, 4, -1, 0, 0, 0, -3, 5
        0, 4, -1, 0
            0, 4
                0
                4
            -1, 0
                -1
                0
        0, 0, -3, 5
            0, 0
                0
                0
            -3, 5
                -3
                5
g(n) = 2 * n - 1

Zadanie 10.4
-------------------
|   n  | operacje |
|------+----------|
|   3  |    2     |
|------+----------|
|   9  |    8     |
|------+----------|
|  27  |    26    |
|------+----------|
|  81  |    80    |
|------+----------|
|  243 |   242    |
-------------------
'''


# Zadanie 11

'''
-------------------------
|   a   |   b   |   c   |
|-------+-------+-------|
|       |       |       |
|-------+-------+-------|
|       |       |       |
|-------+-------+-------|
|       |       |       |
-------------------------


'''

# funkcja main
if __name__ == '__main__':
    #tutaj wywoluj swoje funkcje i inne takie






































