def merge(a: list, b: list):
    """merges two already sorted lists, needs extra memory"""
    c = [0] * (len(a) + len(b))
    i = k = n = 0

    while i < len(a) and k < len(b):
        if a[i] <= b[k]:
            c[n] = a[i]
            i += 1
            n += 1
        else:
            c[n] = b[k]
            k += 1
            n += 1

    while i < len(a):
        c[n] = a[i]
        i += 1
        n += 1

    while k < len(b):
        c[n] = b[k]
        k += 1
        n += 1

    return c


def merge_heap(a: list):
    q = []
    heapq.heapify(q)
    for i in range(len(a)):
        heapq.heappush(q, [a[i]])

    while len(q) > 1:
        l, r = heapq.heappop(q), heapq.heappop(q)
        heapq.heappush(q, merge(l, r))

    return heapq.heappop(q)


def merge_sort(a):
    """mother function sorting array A with usage of additional memory"""
    if len(a) > 1:
        middle = len(a) // 2
        l = a[:middle]
        r = a[middle:]

        l = merge_sort(l)
        r = merge_sort(r)
        c = merge(l, r)
        return c
    return a


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
                k += 1
            else:
                alist[k] = righthalf[j]
                j += 1
                k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def hoar_sort(A):
    if len(A) <= 1:
        return
    barrier = A[0]
    L, M, R = [], [], []
    for x in A:
        if x < barrier:
            L.append(x)
        elif x == barrier:
            M.append(x)
        else:
            R.append(x)
    hoar_sort(L)
    hoar_sort(R)
    k = 0
    for x in L + M + R:
        A[k] = x
        k += 1


print()
a = [1, 10, 6, 5, 8, 9, 2, 5, 3, 7, 4]
hoar_sort(a)
print('inplace hoar_sort a = ', a)


def check_sorted(A, ascending=True):
    """this part needs some improvement since
       I want use it like all(list(map(check_sorted, func(arr)))) for func in func_list"""
    flag = True
    if ascending:
        for i in range(len(A)):
            if A[i] > A[i + 1]:
                flag = False
                break
    else:
        for i in range(len(A)):
            if A[i] < A[i + 1]:
                flag = False
                break
    return flag
