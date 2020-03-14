def bubblesort(v):
    n = len(v)
    for i in range (n):
        for j in range (n-1):
            if v[j] > v[j+1] :
                v[j], v[j+1] = v[j+1], v[j]
    return v

def countsort(v):
    n = len(v)
    ok = 1
    if len(v) == 0:
        return []
    m = []
    maxim = max(v)

    fr = [0] * (maxim + 1)
    for i in v:
        fr[i] += 1
    for i in range (maxim + 1):
        for j in range (1, fr[i] + 1):
            m.append(i)
    return m

def interclasare(lst, ldr):
    i=j=0
    rez = []
    while i < len(lst) and j < len(ldr):
        if lst[i] <= ldr[j]:
            rez.append(lst[i])
            i += 1
        else:
            rez.append(ldr[j])
            j += 1
    rez.extend(lst[i:])
    rez.extend(ldr[j:])
    return rez

def mergesort(lista):
    if len(lista) <= 1:
        return lista
    else:
        mijloc = len(lista)//2
        lst = mergesort (lista[:mijloc])
        ldr = mergesort (lista[mijloc:])
        return interclasare (lst, ldr)

def pivot_mediana(A):
    if len(A) <=1 :
        return sorted(A)[len (A)//2]
    subliste = [sorted(A[i:i+5]) for i in range (0, len (A), 5)]
    mediane = [sl[len(sl)//2] for sl in subliste]
    return pivot_mediana(mediane)

def quicksort(v):
    if len(v) <= 1:
        return v
    else:
        pivot = pivot_mediana(v)
        L = [x for x in v if x < pivot]
        E = [x for x in v if x == pivot]
        G = [x for x in v if x > pivot]
        return quicksort(L) + E + quicksort(G)

def radixsort(v, p):
    n = len(v)
    m = max(v)
    if p > m*10:
        return v
    bucket = [[] for i in range(10)]
    for i in range (n):
        c = (v[i] % p) // (p // 10)
        bucket[c].append(v[i])
    s = []
    for i in range(10):
        s.extend(bucket[i])
    return (radixsort(s, p*10))

def test(v):
    ok = 1
    n = len (v)
    for i in range(n-1):
        if v[i] > v[i+1]:
            return 0
    return 1

import time
from random import randrange as rand

for i in range(3, 7):
    f = open("sortari.inout", "w")
    for j in range(10**i):
        f.write(str(rand(10**i)) + " ")
    f.close()

    f = open("sortari.inout", "r")
    v = [int(x) for x in f.read().split()]
    f.close()

    ### bubble sort
    start = time.time()
    if len(v) > 9000:
        print ("Sunt prea multe numere pt un bubblesort.")
    else:
        s = bubblesort(v)
        final = time.time()
        if test(s):
            print( "Pentru " + str(10**i) + " numere, metoda bubblesort se executa in "+ str(final-start) + " secunde.")

    ### count sort
    start = time.time()
    s = countsort(v)
    final = time.time()
    if test(s):
        if final - start > 5 :
            print ("countsort: Dureaza prea mult.")
        else:
            print("Pentru " + str(10 ** i) + " numere, metoda countsort se executa in " + str(final - start) +" secunde.")

    ### merge sort
    start = time.time()
    s = mergesort(v)
    final = time.time()
    if test(s):
        if final - start > 5 :
            print ("mergesort: Dureaza prea mult.")
        else:
            print("Pentru " + str(10 ** i) + " numere, metoda mergesort se executa in " + str(final - start) + " secunde.")

    ### quick sort
    start = time.time()
    s = quicksort(v)
    final = time.time()
    if test(s):
        if final - start > 5:
            print ("quicksort: Dureaza prea mult.")
        else:
            print("Pentru " + str(10 ** i) + " numere, metoda quicksort se executa in " + str(final - start) + " secunde.")

    ### radix sort
    start = time.time()
    p = 10
    s = radixsort(v, p)
    final = time.time()
    if test(s):
        print("Pentru " + str(10 ** i) + " numere, metoda radixsort se executa in " + str(final - start) + " secunde.")

    ### sort
    start = time.time()
    s = sorted(v)
    final = time.time()
    if test(s):
        print("Pentru " + str(10 ** i) + " numere, metoda sorted se executa in " + str(final - start) + " secunde.")

    print()