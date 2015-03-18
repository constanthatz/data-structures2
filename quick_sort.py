import random
import timeit


def quicksort(a_list):
    return _quicksort(a_list, 0, (len(a_list)-1))


def _quicksort(A, lo, hi):
    if lo < hi:
        p = partition(A, lo, hi)
        _quicksort(A, lo, p - 1)
        _quicksort(A, p + 1, hi)
    return A

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
    nums_best = [range(0, 10**i) for i in xrange(4)]
    nums_worst = [item[::-1] for item in nums_best]

    time_best = []
    time_worst = []

    for i in xrange(len(nums_best)):
        def test(nums, lo, hi):
            quicksort(nums)

        setup = "from __main__ import test\nnums = {}"

        time_best.append(timeit.Timer(
            "test(nums, 0, len(nums)-1)",
            setup=setup.format(nums_best[i])).timeit(number=10000))
        time_worst.append(timeit.Timer(
            "test(nums, 0, len(nums)-1)",
            setup=setup.format(nums_worst[i])).timeit(number=10000))

    print(time_best)
    print(time_worst)
