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

def pivot_med3(x, y, z):
    if x >= y and x <= z or x >= z and x <= y:
        return x
    if y >= x and y <= z or y >= z and y <= x:
        return y
    return z

def quicksort_m3(v):
    if len(v) <= 1:
        return v
    else:
        if len(v) >= 3:
            pivot = pivot_med3(v[0], v[len(v) // 2], v[len(v) - 1])
        else:
            pivot = v[0] if v[0] >= v[1] else v[1]
        L = [x for x in v if x < pivot]
        E = [x for x in v if x == pivot]
        G = [x for x in v if x > pivot]
        return quicksort_m3(L) + E + quicksort_m3(G)

def quicksort_mm(v):
    if len(v) <= 1:
        return v
    else:
        pivot = pivot_mediana(v)
        L = [x for x in v if x < pivot]
        E = [x for x in v if x == pivot]
        G = [x for x in v if x > pivot]
        return quicksort_mm(L) + E + quicksort_mm(G)

def radixsort_10(v, p):
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
    return (radixsort_10(s, p*10))

def radixsort_2(v, k):
    n = len(v)
    m = max(v)
    if 2**k > m:
        return v
    bucket = [[], []]
    for i in range(n):
        c = (v[i] >> k) & 1
        if c == 0:
            bucket[0].append(v[i])
        else:
            bucket[1].append(v[i])
    s = []
    s.extend(bucket[0])
    s.extend(bucket[1])
    return radixsort_2(s, k+1)

def test(v):
    ok = 1
    n = len (v)
    for i in range(n-1):
        if v[i] > v[i+1]:
            return 0
    return 1

import time
from random import randrange as rand

t = open ("sortari2.in", "r")
nr = int(t.readline())
i = 1
for linie in t:

    n = int (linie.split()[0])
    m = int (linie.split()[1])

    f = open("sortari1.in", "w")
    for j in range(n):
        f.write(str(rand(m)) + " ")
    f.close()

    f = open("sortari1.in", "r")
    v = [int(x) for x in f.read().split()]
    f.close()

    print ("testul " + str(i))
    i += 1

    ### bubble sort
    start = time.time()
    if len(v) > 9999:
        print ("bubble sort pentru {} numere mai mici decat {}: sunt prea multe numere".format(n, m))
    else:
        s = bubblesort(v)
        final = time.time()
        if test(s):
            print ("bubble sort pentru {} numere mai mici decat {}: {} secunde".format(n, m, final - start))
            #print( "Pentru " + str(10**i) + " numere, metoda bubblesort se executa in "+ str(final-start) + " secunde.")

    ### count sort
    start = time.time()
    s = countsort(v)
    final = time.time()
    if test(s):
        print("count sort pentru {} numere mai mici decat {}:".format(n, m), end=" ")
        if final - start > 5 :
            print ("dureaza prea mult.")
        else:
            print(str(final - start) + " secunde")

    ### merge sort
    start = time.time()
    s = mergesort(v)
    final = time.time()
    if test(s):
        print("merge sort pentru {} numere mai mici decat {}:".format(n, m), end=" ")
        if final - start > 5 :
            print ("dureaza prea mult.")
        else:
            print(str(final - start) + " secunde")

    ### quick sort mm
    start = time.time()
    s = quicksort_mm(v)
    final = time.time()
    if test(s):
        print("quick sort in pivot mediana medianelor pentru {} numere mai mici decat {}:".format(n, m), end=" ")
        if final - start > 5:
            print ("dureaza prea mult.")
        else:
            print(str(final - start) + " secunde")

    ### quick sort mm
    start = time.time()
    s = quicksort_m3(v)
    final = time.time()
    if test(s):
        print("quick sort in pivot mediana din 3 pentru {} numere mai mici decat {}:".format(n, m), end=" ")
        if final - start > 5:
            print("dureaza prea mult.")
        else:
            print(str(final - start) + " secunde")

    ### radix sort in baza 10
    start = time.time()
    s = radixsort_10(v, 10)
    final = time.time()
    if test(s):
        print("radix sort in baza 10 pentru {} numere mai mici decat {}: {} secunde".format(n, m, final - start))
        #print("Pentru " + str(10 ** i) + " numere, metoda radixsort se executa in " + str(final - start) + " secunde.")

    ### radix sort in baza 2
    start = time.time()
    s = radixsort_2(v, 0)
    final = time.time()
    if test(s):
        print("radix sort in baza 2 pentru {} numere mai mici decat {}:".format(n, m), end = " ")
        if final - start > 5:
            print("dureaza prea mult.")
        else:
            print(str(final - start) + " secunde")

    ### sort
    start = time.time()
    s = sorted(v)
    final = time.time()
    if test(s):
        print("sort pentru {} numere mai mici decat {}: {} secunde".format(n, m, final - start))
        #print("Pentru " + str(10 ** i) + " numere, metoda sorted se executa in " + str(final - start) + " secunde.")

    print()
t.close()
