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
import math


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

def ONP(n, X):
    symbole = "+-*"
    k = 1
    T = [0] * n
    for i in range(1, n + 1):
        if X[i - 1].isdigit():
            T[k - 1] = int(X[i - 1])
        if X[i - 1] in symbole:
            b = int(T[k - 2])
            a = int(T[k - 3])
            k = k - 2
            if X[i - 1] == '+':
                T[k - 1] = int(a + b)
            if X[i - 1] == '-':
                T[k - 1] = int(a - b)
            if X[i - 1] == '*':
                T[k - 1] = int(a * b)
        k = k + 1
    return T[1-1]

def poprawneONP(n, X):
    licznik = 0
    for i in range(1, n + 1):
        if X[i - 1].isdigit():
            licznik = licznik + 1
        if X[i - 1] in "+-*":
            if licznik < 2:
                return "NIE", licznik
            else:
                licznik = licznik - 1
    if licznik != 1:
        return "NIE", licznik
    else:
        return "TAK", licznik

'''
Zadanie 11.1
----------------------------------------------------------------------------
|       W=W1xW2       |     W1    |     W2    | op |         ONP(W)        |
|---------------------+-----------+-----------+----+-----------------------|
|        4 + 3        |     4     |     3     | +  |          4 3 +        |
|---------------------+-----------+-----------+----+-----------------------|
|       (4+3)*2       |    4+3    |     2     | *  |       4 3 + 2 *       |
|---------------------+-----------+-----------+----+-----------------------|
|       5*(7-6)       |     5     |   (7-6)   | *  |       5 7 6 - *       |
|---------------------+-----------+-----------+----+-----------------------|
| ((4+3)*2)-(5*(7-6)) | ((4+3)*2) | (5*(7-6)) | -  | 4 3 + 2 * 5 7 6 - * - |
----------------------------------------------------------------------------

Algorytm:
k ← 1
dla i=1,2,…,n wykonuj
    jeżeli X[i] jest liczbą
        T[k] ← X[i]
    jeżeli X[i]∈{+, –, ∗}
        b ← T[k – 1]
        a ← T[k – 2]
        k ← k – 2
        jeżeli X[i] = `+`
            T[k] ← a + b
        jeżeli X[i] = `–`
            T[k] ← a – b
        jeżeli X[i] = `∗`
            T[k] ← a ∗ b
    k ← k + 1
zwróć T[1]

Zadanie 11.2
-------------------------
|  i  | k po i | T po i |
|-----+--------+--------|
|  1  |   2    |   9    |
|-----+--------+--------|
|  2  |   3    |  9, 7  |
|-----+--------+--------|
|  3  |   2    | 16, 7  |
|-----+--------+--------|
|  4  |   3    | 16, 3  |
|-----+--------+--------|
|  5  |   2    |   48   |
|-----+--------+--------|
|  6  |   3    | 48, 5  |
|-----+--------+--------|
| 10  |   3    | 48, 2  |
|-----+--------+--------|
| 11  |   2    |   46   |
-------------------------

Zadanie 11.3
Algorytm:
    licznik ← 0
        dla i=1,2,…,n wykonuj
            jeżeli X[i] jest liczbą
                licznik ← licznik + 1
            jeżeli X[i]∈{+, –, ∗}
                jeżeli licznik < 2
                    zwróć „Nie” i zakończ działanie
                w przeciwnym razie
                    licznik ← licznik – 1
    jeżeli licznik ≠ 1
        zwróć „Nie”
    w przeciwnym razie
        zwróć „Tak”

----------------------------------------------------------
|               Napis               | licznik | poprawne |
|-----------------------------------+---------+----------|
|              1 2 + *              |    1    |   NIE    |
|-----------------------------------+---------+----------|
|      1 2 + 3 4 - 5 * 7 8 + 9      |    4    |   NIE    |
|-----------------------------------+---------+----------|
|         1 2 3 4 5 + + + +         |    1    |   TAK    |
|-----------------------------------+---------+----------|
|       1 2 3 4 5 + + + + + +       |    1    |   NIE    |
|-----------------------------------+---------+----------|
|        1 2 3 4 5 + + + + +        |    1    |   NIE    |
|-----------------------------------+---------+----------|
|  1 2 + 2 3 - 3 4 * 4 5 + - - - -  |    1    |   TAK    |
|-----------------------------------+---------+----------|
| 1 2 + 2 3 - 3 4 * 4 5 + - - - - - |    1    |   NIE    |
|-----------------------------------+---------+----------|
|   1 2 + 3 4 - 5 * 7 8 + 9 + + +   |    1    |   TAK    |
----------------------------------------------------------

Zadanie 11.4
X: 1 2 3 4 5 6 7 8 9 10 op1 op2 op3 op4 op5 op6 op7 op8 op9
Y: 10 9 8 7 6 5 4 3 2 1 op9 op8 op7 op6 op5 op4 op3 op2 op1

'''


# Zadanie 12

def szyfrBeauforta(n, Tekst, k):
    Szyfrogram = [0] * n
    i = 0
    while i < n:
        Szyfrogram[i] = chr((90 - ord(Tekst[i]) + k) % 26 + 65)
        i = i + 1
        k = k + 1
    return "".join(Szyfrogram)

'''
i ← 0
dopóki (i<n) wykonuj
(*) Szyfrogram[i] ← (90-Tekst[i]+k) mod 26 + 65
    i ← i+1
    k ← k+i

Zadanie 12.1
-----------------------
| Lp. |   i   |   k   |
|-----+-------+-------|
|  1  |   0   |  20   |
|-----+-------+-------|
|  2  |   1   |  21   |
|-----+-------+-------|
|  3  |   2   |  22   |
|-----+-------+-------|
|  4  |   3   |  23   |
|-----+-------+-------|
|  5  |   4   |  24   |
|-----+-------+-------|
|  6  |   5   |  25   |
|-----+-------+-------|
|  7  |   6   |  26   |
-----------------------

Zadanie 12.2
26 bo modulo 26 i tak wszystkie liczby >= 26 zmniejsza

Zadanie 12.3
---------------------------
|  k  | Teskt[] | Szyfr[] |
|-----+---------+---------|
|  1  |  MAPA   |  OBND   |
|-----+---------+---------|
|  2  |  KOC    |   DAN   |
---------------------------
'''
# Zadanie 12.4
def deSzyfrBeauforta(n, Szyfrogram, k):
    Tekst = [0] * n
    i = 0
    while i < n:
        x = ord(Szyfrogram[i]) - 65 - k
        if x < 0:
            x = x + 26
        x = 90 - x
        Tekst[i] = chr(x)
        i = i + 1
        k = k + 1
    return "".join(Tekst)


# Zadanie 13

def sprawdzPunkty(PX, PY, ax, ay):
    n = len(PX)
    for i in range(1, n + 1):
        roznicax = PX[i-1] - ax
        roznicay = PY[i-1] - ay
        drugix = ax - roznicax
        drugiy = ay - roznicay
        znalezione = False
        for k in range(1, n + 1):
            if drugix == PX[k-1] and drugiy == PY[k-1]:
                znalezione = True
        if znalezione == False:
            return "NIE"
    return "TAK"

'''
funkcja sprawdz(PX[1..n], PY[1..n],ax,ay)
    dla i = 1, 2, ..., n wykonuj
        roznicax ← PX[i] – ax
        roznicay ← PY[i] – ay
        drugix ← ax – roznicax
        drugiy ← ay – roznicay
        znalezione ← fałsz
        dla k = 1, 2, ..., n wykonuj
            jeżeli drugix = PX[k] oraz drugiy = PY[k]
                znalezione ← prawda
        jeżeli znalezione = fałsz
            wypisz NIE i zakończ wykonywanie algorytmu
    wypisz TAK

Zadanie 13.1
1.TAK
2.NIE
3.TAK

Zadanie 13.2
P6=(3; -2)
A=(2; 1)
'''


# Zadanie 14

'''
Zadanie 14.1
----------
| n | l  |
|---+----|
| 0 | 1  |
|---+----|
| 1 | 2  |
|---+----|
| 2 | 4  |
|---+----|
| 3 | 8  |
|---+----|
| 5 | 32 |
|---+----|
| 6 | 64 |
|---+----|
| 9 |512 |
|---+----|
|10 |1024|
----------
C(n)=2^n

Zadanie 15.2
------------
| n |  l   |
|---+------|
| 0 |  1   |
|---+------|
| 1 | 1/3  |
|---+------|
| 2 | 1/9  |
|---+------|
| 3 |1/27  |
|---+------|
| 4 |1/81  |
|---+------|
| 5 |1/243 |
|---+------|
| 6 |1/729 |
|---+------|
| 7 |1/2187|
------------
D(n)=1(/3^n)

Zadanie 15.3
[0; 1/27], [2/27; 1/9], [2/9; 7/27], [8/27; 1/3], [2/3; 19/27], [20/27; 7/9], [8/9; 25/27], [26/27; 1]
[0; 0.001], [0.002; 0.01], [0.02; 0.021], [0.022; 0.1], [0.2; 0.201], [0.202; 0.21], [0.22; 0.221], [0.222; 1]
'''

def pole(n, punktyX, punktyY):
    pole = 0
    for i in range(0, n):
        index1 = i+1
        index2 = i-1
        if i+1 == n:
            index1 = 0
        if i-1 == -1:
            index2 = n-1
        x1 = punktyX[index1]
        x2 = punktyX[index2]
        pole = pole + (x1 - x2) * punktyY[i]
    return pole / 2

'''
Zadanie 14.1
----------------------------
| i | x | y | x+1-x-1 | *y |
|---+---+---+---------+----|
| 1 | 2 | 2 |   -7    |-14 |
|---+---+---+---------+----|
| 2 | 1 | 7 |    7    | 49 |
|---+---+---+---------+----|
| 3 | 9 | 8 |    9    | 72 |
|---+---+---+---------+----|
| 4 |10 | 4 |   -1    | -4 |
|---+---+---+---------+----|
| 5 | 8 | 2 |   -8    |-16 |
----------------------------
Pole: 43.5

Zadanie 14.2
P=1/2*((x2-x3)*y1+(x3-x1)*y2+(x1-x2)*y3)

Zadanie 14.3
+ i - => 2*n-1
* => n
'''

# Zadanie 16

'''
dla każdego niewyciętego pola (i,j)
    D[i, j] ← -1
D[1, 1] ← 0
k ← 0
powtarzaj:
    jeśli nie ma takich pól (x,y), że D[x, y] = k
        zakończ algorytmu
    dla każdego pola (x,y) takiego, że D[x, y] = k wykonaj
        dla każdego pola (a,b) sąsiadującego z (x,y) wykonaj
            jeśli (a,b) nie jest wycięte oraz D[a, b] = -1
                D[a, b] ← k+1
    k ← k+1

Zadanie 16.1
---------------------
| 0 | 1 | 2 | x | x |
|---+---+---+---+---|
| 1 | 2 | x | x | x |
|---+---+---+---+---|
| x | 3 | 4 | x | 8 |
|---+---+---+---+---|
| 5 | 4 | 5 | 6 | 7 |
---------------------

Zadanie 16.2
---------------------
| 0 | 1 | 2 | x |10 |
|---+---+---+---+---|
| 1 | 2 | 3 | x | 9 |
|---+---+---+---+---|
| 2 | 3 | 4 | x | 8 |
|---+---+---+---+---|
| 3 | 4 | 5 | 6 | 7 |
---------------------

Zadanie 16.3
---------
| 0 | x |
|---+---|
| x |-1 |
---------
'''


# Zadanie 17

'''
odczytaj prędkość samochodu;
odczytaj odległość od najbliższego pojazdu;
jeżeli prędkość samochodu < 30 lub odległość od najbliższego pojazdu < 15:
    dopóki prędkość samochodu = 100 wykonuj
        wyślij polecenie hamowania do układu hamulcowego;
        odczytaj prędkość samochodu

Zadanie 17.1
dopóki prędkość samochodu = 100 wykonuj                                    => dopóki prędkość samochodu > 0 wykonuj
jeżeli prędkość samochodu < 30 lub odległość od najbliższego pojazdu < 15: => jeżeli prędkość samochodu < 30 oraz odległość od najbliższego pojazdu < 15:

Zadanie 17.2
prędkość samochodu — 29 km/h, odległość między samochodami — 1 m      => brzegowe
prędkość samochodu — 400 km/h,odległość od najbliższego pojazdu — 0 m => niezgodne ze specyfikacją
prędkość samochodu — 13 km/h,odległość od najbliższego pojazdu — 8 m  => standardowe
prędkość samochodu — 45 km/h,odległość od najbliższego pojazdu — 17 m => standardowe
prędkość samochodu — 0 km/h,odległość od najbliższego pojazdu — 17 m  => brzegowe

Zadanie 17.3
---------------------------------------------------------------------------------------------------------------------------------
|                                                          Pytanie                                                          |P/F|
|---------------------------------------------------------------------------------------------------------------------------+---|
| upewnienie się, że system poradzi sobie z odczytem parametrów z czujników i tempo jego reakcji pozwoli uniknąć zderzenia. | P |
|---------------------------------------------------------------------------------------------------------------------------+---|
|                                   zwiększenie precyzji pomiarów prędkości i odległości.                                   | F |
|---------------------------------------------------------------------------------------------------------------------------+---|
|                                               zmniejszenie długości kodu programu.                                        | F |
|---------------------------------------------------------------------------------------------------------------------------+---|
|                               sprawdzenie, czy system działa zgodnie z podaną specyfikacją.                               | P |
---------------------------------------------------------------------------------------------------------------------------------

zadanie 17.4
--------------------
|  v  |  d  | stan |
|-----+-----+------|
| <30 | <15 |  wl  |
|-----+-----+------|
| <30 | =15 | nieu |
|-----+-----+------|
| =30 | <15 | wyl  |
|-----+-----+------|
| =30 | =15 | wyl  |
|-----+-----+------|
| >30 | --- | wyl  |
--------------------
'''


# Zadanie 18

def NWD(a, b):
    mod = 0
    while b != 0:
        r = a % b
        mod += 1
        a = b
        b = r
    return a

'''
funkcja NWD (a, b)
    dopóki b ≠ 0 wykonuj
(*)     r ← a mod b
        a ← b
        b ← r
    zwróć a i zakończ

Zadanie 18.1
-------------------
|  a  |  b  | mod |
|-----+-----+-----|
| 25  | 15  |  3  |
|-----+-----+-----|
| 116 | 324 |  6  |
|-----+-----+-----|
| 762 | 282 |  6  |
-------------------

Zadanie 18.2
----------------------------------
|          a1 A2 an        | NWD |
|--------------------------+-----|
|       36 24 72 150       |  6  |
|--------------------------+-----|
|    119 187 323 527 731   | 17  |
|--------------------------+-----|
| 121 330 990 1331 110 225 |  1  |
----------------------------------
'''
# Zadanie 18.3
def NWDCiag(a):
    nwd = NWD(a[0], a[1])
    for i in range(2, len(a)):
        nwd = NWD(nwd, a[i])
    return nwd


# Zadanie 19

'''
Zadanie 19.1
---------------------------------------------------
|  Towar  |      2      |    4    |   8   |  10   |
|---------+-------------+---------+-------+-------|
| Kozaki  |   10111011  |  2323   |  273  |  187  |
|---------+-------------+---------+-------+-------|
| Plaszcz |  111010100  |  13110  |  724  |  3744 |
|---------+-------------+---------+-------+-------|
| Skuter  | 10110110010 | 112302  | 2662  |  1458 |
---------------------------------------------------

Zadanie 19.2
------------------------------
|      x      | R |     y    |
|-------------+---+----------|
| 110000100 2 | > |  556 8   |
|-------------+---+----------|
|   3123 4    | < |  1747 8  |
|-------------+---+----------|
|   110 10    | > | 11010 3  |
|-------------+---+----------|
|    266 9    | < | 110100 3 |
|-------------+---+----------|
| 110111101 2 | > |  674 8   |
------------------------------

Zadanie 19.3
suma2 = 1011 0010
suma4 = 2333
R = 13
'''
# Zadanie 19.4
def suma(A, B, p, n):
    i = 1
    R = [0]
    while i < n + 1:
        c = A[i-1] + B[i-1] + R[i-1]
        R.append(c // p)
        i += 1


# Zadanie 20

'''
Zadanie 20.1
371
407
54748

Zadanie 20.2
-----------------------
|   x   |   B   | P/F |
|-------+-------+-----|
| 3433  |   6   |  P  |
|-------+-------+-----|
| 4890  |   5   |  P  |
|-------+-------+-----|
| 8956  |   3   |  F  |
|-------+-------+-----|
| 15345 |   2   |  F  |
-----------------------
'''
# Zadanie 20.3
def czyBNarcystyczna(x, B):
    digits = []
    a = x
    while a != 0:
        digits.append(a % B)
        a //= B
    digits.reverse()
    sum = 0
    for d in digits:
       sum += pow(d, len(digits))
    if sum == x:
        return "TAK"
    return "NIE"


# Zadanie 21

'''
Zadanie 21.1
x^1, x^2, (x^2)^2, ((x^2)^2)^2x, (((x^2)^2)^2x)^2x, ((((x^2)^2)^2x)^2x)^2

Zadanie 21.2
------------------
| k  | bin k | * |
|----+-------+---|
| 4  |  100  | 2 |
|----+-------+---|
| 5  |  101  | 3 |
|----+-------+---|
| 6  |  110  | 3 |
|----+-------+---|
| 7  |  111  | 4 |
|----+-------+---|
| 8  | 1000  | 3 |
|----+-------+---|
| 15 | 1111  | 6 |
|----+-------+---|
| 16 | 10000 | 4 |
|----+-------+---|
| 22 | 10110 | 6 |
|----+-------+---|
| 32 |100000 | 5 |
------------------
'''
# Zadanie 21.3
def SzybkiePotegowanie(x, n):
    wynik = 1
    while n > 0:
        if n % 2 == 1:
            wynik *= x
        x *= x
        n //= 2
    return wynik


# Zadanie 22

def schematHornera(n, x, a):
    w = a[n-1]
    for k in range(n-2, -1, -1):
        w = x*w+a[k]
    return w

'''
Zadanie 22.1
--------------------------
| Dane |    Wartosci     |
|------+-----------------|
|  n=N |       6         |
|------+-----------------|
|  x=R |       6         |
|------+-----------------|
| a0a1 | 7,-8,2,1,-13,10 |
--------------------------

Algorytm (schemat Hornera):
    w ← a[n]
    dla k = n − 1, n − 2, ... , 0 wykonuj
(*)     w ← k * w + a[k]
    zwróć w i zakończ

Zadanie 22.2
-------------------------------
| Dzialanie | Liczba operacji |
|-----------+-----------------|
|     +     |       n         |
|-----------+-----------------|
|     *     |       n         |
-------------------------------

Zadanie 22.3
-------------
| k |   w   |
|---+-------|
| 5 |   5   |
|---+-------|
| 4 |  10   |
|---+-------|
| 3 |  22   |
|---+-------|
| 2 |  39   |
|---+-------|
| 1 |  85   |
|---+-------|
| 0 |  179  |
-------------
wynik = 179
'''
# Zadanie 22.4
def schematHornera2n(n, x, a):
    w = a[n-1]
    y = x*x
    for k in range(n-2, -1, -1):
        w = y*w+a[k]
    return w


# Zadanie 23

'''
Algorytm
    i ← 0
    a ← 0
    r ← 1
    dopóki a ≤ x wykonuj
        i ← i + 1
        a ← a + r
        r ← r + 2
    zwróć i – 1 i zakończ

Zadanie 23.1
-------------------------
|   i   |   a   |   r   |
|-------+-------+-------|
|   0   |   0   |   1   |
|-------+-------+-------|
|   1   |   1   |   3   |
|-------+-------+-------|
|   2   |   4   |   5   |
|-------+-------+-------|
|   3   |   9   |   7   |
|-------+-------+-------|
|   4   |  16   |   9   |
|-------+-------+-------|
|   5   |  25   |  11   |
-------------------------

Zadanie 23.2
-----------------
|nr pyt |  P/F  |
|-------+-------|
|   1   |   P   |
|-------+-------|
|   2   |   F   |
|-------+-------|
|   3   |   P   |
|-------+-------|
|   4   |   F   |
-----------------
'''
# Zadanie 23.3

def pierwiastek(x):
    x1 = x / 2
    dalej = True
    while dalej:
        x1 = (x1 + x/x1) / 2
        p = math.floor(x1)
        if p*p and (p+1)*(p+1)>x:
            dalej = False


# funkcja main
if __name__ == '__main__':
    #tutaj wywoluj swoje funkcje i inne takie
    print(schematHornera(7, 2, [9, 7, -5, 2, 0, -3, 4]))




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

-----------------
|   a   |   b   |
|-------+-------|
|       |       |
|-------+-------|
|       |       |
|-------+-------|
|       |       |
-----------------
'''










