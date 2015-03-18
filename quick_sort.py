
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
    for i in xrange(lo, hi-1):
        if A[i] < pivotValue:
            A[storeIndex], A[i] = A[i], A[storeIndex]
            storeIndex += 1
    A[storeIndex], A[hi] = A[hi], A[storeIndex]
    return storeIndex


def select_pivot(a_list):

    if a_list[0] <= a_list[len(a_list)/2] <= a_list[-1] or a_list[-1] <= a_list[len(a_list)/2] <= a_list[0]:
        return a_list[len(a_list)/2]
    elif a_list[len(a_list)/2] <= a_list[0] <= a_list[-1] or a_list[-1] <= a_list[0] <= a_list[len(a_list)/2]:
        return a_list[0]
    else:
        return a_list[-1]
