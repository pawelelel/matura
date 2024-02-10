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
    p = 0
    x1 = x / 2
    dalej = True
    while dalej:
        x1 = (x1 + x/x1) / 2
        #p = math.floor(x1)
        if p*p <= x and (p+1)*(p+1)>x:
            dalej = False
        if (p-1)*(p-1) <= x and p*p > x:
            p=p-1
            dalej=False
    return p


# Zadanie 24

def szukacz(p, k, e, T):
    if k == p:
        if T[p - 1] > e:
            return p
        else:
            return p + 1
    else:
        s = (p + k) // 2
        if T[s - 1] > e:
            return szukacz(p, s, e, T)
        else:
            return szukacz(s+1, k, e, T)

'''
funkcja F (p, k, e)
    jeżeli (k = p)
        jeżeli (T [p] > e)
                zwróć p i zakończ
            w przeciwnym razie
                zwróć p + 1 i zakończ
        w przeciwnym razie
            s ← (p+k) div 2
            jeżeli T [s] > e
                zwróć F (p, s, e)
            w przeciwnym razie
                zwróć F (s+1, k, e)

Zadanie 24.1
-----------------------------------
|           T          | F(p,k,e) |
|----------------------+----------|
|   [3, 4, 6, 8, 9]    |    6     |
|----------------------+----------|
| [15, 16, 18, 22, 24] |    1     |
|----------------------+----------|
|  [2, 10, 16, 24, 26] |    3     |
|----------------------+----------|
|  [1, 3, 10, 10, 18]  |    5     |
-----------------------------------

Zadanie 24.2
-----------------
|Pytanie|  P/F  |
|-------+-------|
|   1   |       |
|-------+-------|
|   2   |   x   |
|-------+-------|
|   3   |       |
-----------------

Zadanie 24.3
-----------------
|Pytanie|  P/F  |
|-------+-------|
|n div 2|       |
|-------+-------|
|  √n   |       |
|-------+-------|
|log2 n |   X   |
-----------------
'''
# Zadanie 24.4
def sprawdzPrzedzial(n, T, a, b):
    p = szukacz(1, n, b, T)
    l = szukacz(1, n, a, T)
    return p - l


# Zadanie 25

def czyPalindrom(S):
    d = len(S)
    i = d // 2
    while (i > 0) and (S[i] == S[d - i]):
        i -= 1
    if i == 0:
        return "TAK"
    else:
        return "NIE"

'''
    Algorytm:
        d ← długość(S)
        i ← d div 2
(*)     dopóki (i > 0) i (S[i] = S[d – i+1]) wykonuj
            i ← i – 1
        jeżeli i = 0
            zwróć TAK i zakończ,
        w przeciwnym razie
            zwróć NIE i zakończ

Zadanie 25.1
"AAAAAAAAB"
'''

# Zadanie 25.2 ignorujemy spacje
def czyZdaniePalindrom(S):
    S = str(S)
    S.replace(' ', '')
    return czyPalindrom(S)


# Zadanie 26

'''
Zadanie 26.1
----------------------------------------------
|        X         |     Y     | Podrzednosc |
|------------------+-----------+-------------|
| HHGGFFEEDDCCBBAA |  ABCDEFGH |     TAK     |
|------------------+-----------+-------------|
|     DCBADCBA     |  FGHABCJD |    4 TAK    |
|------------------+-----------+-------------|
|      ABCDE       |  ABCCBAE  |     NIE     |
|------------------+-----------+-------------|
|      AAAAA       |     AA    |    0 TAK    |
|------------------+-----------+-------------|
|       ABA        |    ACA    |     NIE     |
|------------------+-----------+-------------|
|      ACEGJ       | ABCDEFGHJ |    4 TAK    |
----------------------------------------------

Dany jest następujący algorytm A:
    dla i=1,2,…,10 wykonuj
        Czyjest[i] ← fałsz
    d ← dlugosc(Y)
    dla i=1,2,…,d wykonuj
        lit ← Y[i]
        Czyjest[kod(lit)] ← prawda
    d ← dlugosc(X)
    czyp ← prawda
    dla i=1,2,…,d wykonuj
        lit ← X[i]
        czyp ← czyp i Czyjest[kod(lit)]
    jeżeli czyp=prawda
        zwróć 1
    w przeciwnym razie
        zwróć 0

Zadanie 26.2
----------------------------------------------------
|        X         |     Y     | wynik algorytmu A |
|------------------+-----------+-------------------|
| HHGGFFEEDDCCBBAA |  ABCDEFGH |         1         |
|------------------+-----------+-------------------|
|     DCBADCBA     |  FGHABCJD |         1         |
|------------------+-----------+-------------------|
|      ABCDE       |  ABCCBAE  |         0         |
|------------------+-----------+-------------------|
|      AAAAA       |    AA     |         1         |
|------------------+-----------+-------------------|
|        AA        |  AAAAA    |         1         |
|------------------+-----------+-------------------|
|      ACEGJ       | ABCDEFGHJ |         0         |
----------------------------------------------------
Specyfikacja
Wynik: 1 -> slowa sa podobne; 0 -> slowa nie sa podobne

Zadanie 26.3
Algorytm B:
    dla i=1,2,…,10 wykonuj
        Czy_x[i] ← fałsz
        Czy_y[i] ← fałsz
    dx ← dlugosc(X)
    dla i=1,2,…,dx wykonuj
        lit ← X[i]
        Czy_x[kod(lit)] ← prawda
    dy ← dlugosc(Y)
    dla i=1,2,…,dy wykonuj
        lit ← Y[i]
        Czy_y[kod(lit)] ← prawda
    k ← 0
    dla i=1,2,…,10 wykonuj
        jeżeli Czy_y[i]=prawda oraz Czy_x[i]= prawda
            k← k + 1
        jeżeli Czy_y[i]= falsz oraz Czy_x[i]=prawda
            zwróć −1 i zakończ
    zwróć k
'''
# Zadanie 26.4
def czyRownowazne(A: str, B: str):
    litery = []
    for a in A:
        if a not in litery:
            litery.append(a)
    for b in B:
        if b not in litery:
            return 0
    return 1


# Zadanie 27

'''
Zadanie 27.1
-----------------------------------
| Wzorzec |   Tekst    |  Sposob   |
|---------+------------+-----------|
|  para   |   opera    | z błędem  |
|---------+------------+-----------|
|  para   |   aparat   | dokładnie |
|---------+------------+-----------|
|  kran   |  karawana  | z błędem  |
|---------+------------+-----------|
|  sport  | bezspornie | z błędem  |
|---------+------------+-----------|
|   ryt   |  zakryty   | dokładnie |
|---------+------------+-----------|
|  sofa   |  solanka   | z błędem  |
------------------------------------

Zadanie 27.2
AAAAAAAA
AAAA
'''
# Zadanie 27.3
def dopasowanieZBledem(wzorzec, tekst):
    match = 0
    for i in range(0, len(tekst) - len(wzorzec) + 1):
        for j in range(0, len(wzorzec)):
            if tekst[i + j] == wzorzec[j]:
                match += 1
        if match == len(wzorzec) or match == len(wzorzec) - 1:
            return "TAK"
    return "NIE"


# Zadanie 28

'''
Zadanie 28.1
-------------------------------------------
|   Slowo    | 2a  | 2b  | Czy a p |  Bo  |
|------------+-----+-----+---------+------|
|  AABAABAA  | tak | tak |   tak   | AABA |
|------------+-----+-----+---------+------|
|  AAABBAAA  | tak | nie |   nie   |      |
|------------+-----+-----+---------+------|
|  AAABBAAB  | nie | nie |   nie   |      |
|------------+-----+-----+---------+------|
|  AAAABBBB  |     |     |         |      |
|------------+-----+-----+---------+------|
|  ABBBABAA  |     |     |         |      |
|------------+-----+-----+---------+------|
|  ABAAAABA  |     |     |         |      |
|------------+-----+-----+---------+------|
| AAAAAAAAAA |     |     |         |      |
-------------------------------------------


'''


# Zadanie 29

'''
Zadanie 29.1
MATURA

Zadanie 29.2
Algorytm(wiadomosc):
    litera = pusty()
    kolor_poprzedniej = bialy
    while kolor_poprzedniej != czarny and wiadomosc[0] != czarny:
        kulka = pobierz(wiadomosc)
        kolor_poprzedniej = kulka
        dolacz(litera, kulka)
    return litera, wiadomosc
    
Zadanie 29.3
Algorytm(ciag):
    wiadomosc = pusty()
    while czy_sa_kulki(ciag):
        litera = pobierz_litere(ciag)
        dopisz(wiadomosc, litera)
    return wiadomosc
'''


# Zadanie 30

'''
Zadanie 30.1
szyfruj(zn,k)
    return (znak(zn) + k - 65) mod 26 + 65
    
Zadanie 30.2
INFORMATYKA => JPISWSHBHUL
KOMPUTER => LQPTZZLZ
'''
def szyfrCezaraZPrzesunieciem(slowo):
    st = ""
    k = 1
    for s in slowo:
        st += chr((ord(s) + k - 65) % 26 + 65)
        k += 1
    return st

# Zadanie 30.3
def deSzyfrCezaraZPrzesunieciem(slowo):
    st = ""
    stt = []
    k = 1
    for s in slowo:
        st += chr((ord(s) - k + 65) % 26 + 65)
        k += 1
    return st


# Zadanie 31

'''
Algorytm:
    n ← dlugosc(W)
    m ← n div k
    jeżeli n mod k≠0
        m←m+1
    dla i=1,2,…,m wykonuj
        j←i
        dopóki j ≤ n wykonuj
            wypisz W[j]
            j ← j+m
'''
def szyfrSkokowy(k ,W):
    n = len(W)
    m = n // k
    if n % k != 0:
        m += 1
    for i in range(1, m+1):
        j = i
        while j <= n:
            print(W[j-1], end="")
            j = j+m

'''
Zadanie 31.1
ZEŁA1ADJTAEWNSEIT
ZEPA1RDJOAESNSTITE

Zadanie 31.2
UMIEMDEKODOWAĆ
DOBRZEJEST
'''

# Zadanie 31.3
def deSzyfrSkokowy(k ,W):
    n = len(W)
    wynik = [' '] * n
    m = n // k
    if n % k != 0:
        m += 1
    index = 1
    for i in range(1, m+1):
        j = i
        while j <= n:
            wynik[j-1] = W[index-1]
            index += 1
            #print(W[j-1], end="")
            j = j+m

    print("".join(wynik))

# Zadanie 32.4
def szyfrMieszany(k, W):
    tab = [[] for i in range(k)]
    n = len(W)
    m = n // k
    if n % k != 0:
        m += 1
    index = 1
    for i in range(1, n + 1):
        x = (i-1) // 4
        tab[x].append(W[index-1])
        index += 1
    for x in range(k):
        for y in range(m):
            l = len(tab[x])
            try:
                print(tab[x][y], end="")
            except:
                return


# Zadanie 32

'''
Zadanie 32.1
a(cd)a         => acdcda
(pur)owy       => purpurowy
(z)(zz)        => zzzzzz
(ab)a(abcd)    => ababaabcdabcd
'''
# Zadanie 32.2
def czykompresja(n, napis):
    if n % 2 == 1:
        return
    polowa = n // 2
    if napis[:polowa] == napis[polowa:]:
        return napis[polowa:]
    return
# Zadanie 32.3
def dekomprsja(n, napis):
    i = 0
    while i < n:
        if napis[i] != '(':
            print(napis[i], end="")
            i += 1
            continue
        powtorka = ""
        for j in range(i+1, n):
            if napis[j] == ')':
                i = j
                for p in powtorka:
                    print(p, end="")
                for p in powtorka:
                    print(p, end="")
            else:
                powtorka += napis[j]
        i += 1


# Zadanie 33

'''
Algorytm:
    dla i=1,2,…,n wykonuj
        jeżeli A[i,1]>0
            B[i,1] ← 1
        w przeciwnym razie
            B[i,1] ← 0
    dla j=2,3,…,n wykonuj
        B[0,j] ← 0
        B[n+1,j] ← 0
        dla i=1,2,…,n wykonuj
            jeżeli A[i,j] ≤0
                B[i,j] ← 0
            w przeciwnym razie
                jeżeli B[i – 1, j – 1]=1 lub B[i, j – 1]=1 lub B[i + 1, j – 1]=1
                    B[i,j] ← 1
                w przeciwnym razie
                    B[i,j] ← 0
    d ← 0
    dla i=1,2,…,n wykonuj
        jeżeli B[i,n]=1
            d ← 1
    zwróć d

Zadanie 33.1
        -----------------------------------------
        |   1   |   2   |   3   |   4   |   5   |
|-------+-------+-------+-------+-------+-------|
|   0   |       |   0   |   0   |   0   |   0   |
|-------+-------+-------+-------+-------+-------|
|   1   |   0   |   0   |   1   |   1   |   1   |
|-------+-------+-------+-------+-------+-------|
|   2   |   0   |   1   |   1   |   0   |   0   |
|-------+-------+-------+-------+-------+-------|
|   3   |   1   |   0   |   0   |   1   |   0   |
|-------+-------+-------+-------+-------+-------|
|   4   |   0   |   0   |   0   |   0   |   1   |
|-------+-------+-------+-------+-------+-------|
|   5   |   0   |   0   |   0   |   0   |   0   |
|-------+-------+-------+-------+-------+-------|
|   6   |       |   0   |   0   |   0   |   0   |
-------------------------------------------------
Wartosc: 1

Zadanie 33.2
typu chodzay
wartosciach ujemnych


Zadanie 33.3
x = 0
for koumna
    znajdz najwieksza liczbe
    x += najwieksza liczba
return x 

Zadanie 33.4
Algorytm:
    dla i=1,2,…,n wykonuj
        jeżeli A[i,1]>0
            B[i,1] ← 1
        w przeciwnym razie
            B[i,1] ← 0
    dla j=2,3,…,n wykonuj
        B[0,j] ← 0
        B[n+1,j] ← 0
        dla i=1,2,…,n wykonuj
            jeżeli A[i,j] ≤0
                B[i,j] ← 0
            w przeciwnym razie
                jeżeli B[i, j – 1]=1 lub B[i + 1, j – 1]=1
                    B[i,j] ← 1
                w przeciwnym razie
                    B[i,j] ← 0
    d ← 0
    dla i=1,2,…,n wykonuj
        jeżeli B[i,n]=1
            d ← 1
    zwróć d
'''


# Zadnie 34

'''
Bajtek = 7
Bitus = 128
'''

# Zadanie 35

'''
Zadanie 35 a
-------------------------
| nr pyt|   P   |   F   |
|-------+-------+-------|
|   A   |       |   X   |
|-------+-------+-------|
|   B   |   X   |       |
|-------+-------+-------|
|   C   |       |   X   |
|-------+-------+-------|
|   D   |   X   |       |
-------------------------

Zadanie 35 b
C = 111
M = 1111
x = 15.5

Zadanie 35 c
C = 000
M = 0000
x = 0.0625
'''

# Zadanie 36

'''
Zadanie 36
Wieczorek
Iwanicka
'''

# Zadanie 37

'''
Zadanie 37
winogrona
maliny
orzechy
'''


# Zadanie 38

'''
Zadanie 38
Katowice 3
Kraków 2
Warszawa 2
'''


# Zadanie 39

'''
Zadanie 39.1
aquapark2 bo ma mniejszy rozmiar

Zadanie 39.2
TIFF

Zadanie 39.3
6120
'''

# Zadanie 40

'''
Zadanie 40
LICZ.JEŻELI(A1:A200;"=5")
'''

# Zadanie 41

'''
Zadanie 41
tekstowy
'''

# Zadanie 42

'''
Algorytm:
    x ← T[1]
    i ← 0
    j ← n+1
    wykonuj
        wykonuj
            j ← j-1
(*)     dopóki T[j] > x wykonuj
            i ← i+1
(**)    dopóki T[i] < x
        jeżeli i < j
(***)       zamień(T[i] T[j])
        w przeciwnym razie
            zakończ

Algorytm            
    x ← T[1]
    i ← 0
    j ← n+1
    wykonuj
(*)     wykonuj T[j] > x
            j ← j - 1
(**)    wykonuj  T[i] < x
            i ← i + 1
        jeżeli i < j
(***)       zamień(T[i], T[j])
        w przeciwnym razie
            return

'''

def ciekawyAlgorytm(T):
    n = len(T)
    x = T[1-1]
    i = 0
    j = n + 1
    while True:
        while T[j-1] > x:
            j = j - 1
        while T[i-1] < x:
            i = i + 1
        if i < j:
            T[i-1], T[j-1] = T[j-1], T[i-1]
        else:
            return


'''    
Zadanie 42.1
-------------------------------------------------
|               T               |   *   |  **   |
|-------------------------------+-------+-------|
|   4, 2, 5, 8, 1, 9, 7, 6, 3   |       |       |
|-------------------------------+-------+-------|
| 5, 4, 3, 2, 1, 6, 7, 8, 9, 10 |       |       |
|-------------------------------+-------+-------|
|      1, 2, 3, ... , 100       |       |       |
|-------------------------------+-------+-------|
|     100, 99, 98, ... , 1      |       |       |
-------------------------------------------------
'''


# Zadanie 43

'''
Zadanie 43.1
wyszukiwanie optymalnej trasy samochodowej => musze wiedziec gdzie jestem jezeli chce gdzies pojechac
serwis pogodowy => fajnie jest znac pogode w swojej okolicy

Zadanie 43.2
kompilator języka programowania => niepotrzebne
system komputerowego składu tekstu => niepotrzebne

Zadanie 43.3
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |       |   X   |
|---------+-------+-------|
|    2    |   X   |       |
|---------+-------+-------|
|    3    |       |   X   |
|---------+-------+-------|
|    4    |   X   |       |
---------------------------

Zadanie 43.4
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |       |   X   |
|---------+-------+-------|
|    2    |   X   |       |
|---------+-------+-------|
|    3    |   X   |       |
|---------+-------+-------|
|    4    |       |   X   |
|---------+-------+-------|
|    5    |   X   |       |
---------------------------

'''


# Zadanie 44

'''
Zadanie 44
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |   X   |       |
|---------+-------+-------|
|    2    |   X   |       |
|---------+-------+-------|
|    3    |       |   X   |
|---------+-------+-------|
|    4    |   X   |       |
---------------------------
'''


# Zadanie 45

'''
Zadanie 45
procesor
pamięć operacyjna
'''


# Zadanie 46

'''
Zadanie 46
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |   X   |       |
|---------+-------+-------|
|    2    |       |   X   |
|---------+-------+-------|
|    3    |       |   X   |
|---------+-------+-------|
|    4    |   X   |       |
---------------------------
'''


# Zadanie 47

'''
Zadanie 47
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |       |   X   |
|---------+-------+-------|
|    2    |   X   |       |
|---------+-------+-------|
|    3    |       |   X   |
|---------+-------+-------|
|    4    |   X   |       |
---------------------------
'''


# Zadanie 48

'''
Zadanie 48
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |       |       |
|---------+-------+-------|
|    2    |       |       |
|---------+-------+-------|
|    3    |       |       |
|---------+-------+-------|
|    4    |       |       |
---------------------------
'''


# Zadanie 49

'''
Zadanie 49
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |   X   |       |
|---------+-------+-------|
|    2    |   X   |       |
|---------+-------+-------|
|    3    |       |   X   |
|---------+-------+-------|
|    4    |   X   |       |
---------------------------
'''


# Zadanie 50

'''
Zadanie 50
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |       |   X   |
|---------+-------+-------|
|    2    |   X   |       |
|---------+-------+-------|
|    3    |       |   X   |
|---------+-------+-------|
|    4    |   X   |       |
---------------------------
'''


# Zadanie 51

'''
Zadanie 51
---------------------------
| pytanie | brute |  psy  |
|---------+-------+-------|
|    A    |   X   |   X   |
|---------+-------+-------|
|    B    |       |   X   |
|---------+-------+-------|
|    C    |   X   |       |
|---------+-------+-------|
|    D    |       |   X   |
---------------------------
'''


# Zadanie 52

'''
Zadanie 52
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |   X   |       |
|---------+-------+-------|
|    2    |   X   |       |
|---------+-------+-------|
|    3    |       |   X   |
|---------+-------+-------|
|    4    |       |   X   |
---------------------------
'''


# Zadanie 53

'''
Zadanie 53.1
1: 09:20:15
2: 23:10:36

Zadanie 53.2
     X
  XX  
XX  X 
 X X X
'''


# Zadanie 54

'''
Zadanie 54
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |   X   |       |
|---------+-------+-------|
|    2    |       |   X   |
|---------+-------+-------|
|    3    |       |   X   |
|---------+-------+-------|
|    4    |   X   |       |
---------------------------
'''


# Zadanie 55

def F(n):
    if n == 1:
        return 1
    else:
        return F(n//2)+1

'''
F(n)
    jeżeli n = 1, zwróć 1 i zakończ
    w przeciwnym razie zwróć F(n div 2) + 1

Zadanie 55.1
logarytmiczna

Zadanie 55.2
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |       |   X   |
|---------+-------+-------|
|    2    |   X   |       |
|---------+-------+-------|
|    3    |   X   |       |
|---------+-------+-------|
|    4    |       |   X   |
---------------------------
'''


# Zadanie 56

'''
Zadanie 56
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |   X   |       |
|---------+-------+-------|
|    2    |       |   X   |
|---------+-------+-------|
|    3    |   X   |       |
|---------+-------+-------|
|    4    |       |   X   |
---------------------------
'''


# Zadanie 57

'''
Zadanie 57
---------------------------
| pytanie |   P   |   F   |
|---------+-------+-------|
|    1    |   X   |       |
|---------+-------+-------|
|    2    |   X   |       |
|---------+-------+-------|
|    3    |       |   X   |
|---------+-------+-------|
|    4    |   X   |       |
---------------------------
'''







# funkcja main
if __name__ == '__main__':
    #tutaj wywoluj swoje funkcje i inne takie
    print(ciekawyAlgorytm([4, 2, 5, 8, 1, 9, 7, 6, 3]))


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