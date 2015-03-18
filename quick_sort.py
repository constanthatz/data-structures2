import random


def quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        quicksort(A, lo, p - 1)
        quicksort(A, p + 1, hi)


def partition(A, lo, hi):
    pivotIndex = select_pivot(A, lo, hi)
    pivotValue = A[pivotIndex]

    A[pivotIndex], A[hi] = A[hi], A[pivotIndex]
    storeIndex = lo
    for i in xrange(lo, hi):
        if A[i] < pivotValue:
            A[storeIndex], A[i] = A[i], A[storeIndex]
            storeIndex += 1
    A[storeIndex], A[hi] = A[hi], A[storeIndex]
    return storeIndex


def select_pivot(a_list, lo, hi):
    if a_list[lo] <= a_list[(hi - lo)/2] <= a_list[hi] or a_list[hi] <= a_list[(hi - lo)/2] <= a_list[lo]:
        return a_list[(hi - lo)/2]
    elif a_list[(hi - lo)/2] <= a_list[lo] <= a_list[hi] or a_list[hi] <= a_list[lo] <= a_list[(hi - lo)/2]:
        return a_list[lo]
    else:
        return a_list[hi]

if __name__ == '__main__':
    a_list = random.sample(range(10), 10)
    print(a_list)
    quicksort(a_list, 0, len(a_list)-1)
    print(a_list)
