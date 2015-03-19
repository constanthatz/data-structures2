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
    if a_list[lo] <= a_list[(hi - lo)//2] <= a_list[hi] or a_list[hi] <= a_list[(hi - lo)//2] <= a_list[lo]:
        return (hi - lo)//2
    elif a_list[(hi - lo)//2] <= a_list[lo] <= a_list[hi] or a_list[hi] <= a_list[lo] <= a_list[(hi - lo)//2]:
        return lo
    else:
        return hi

if __name__ == '__main__':
    n = 3
    nums_best = [range(0, 10**i) for i in xrange(n)]
    nums_worst = [[0]*10**i for i in xrange(n)]

    time_best = []
    time_worst = []

    for i in xrange(len(nums_best)):
            def test(nums):
                quicksort(nums)

            setup = "from __main__ import test\nnums = {}"

            time_one = timeit.Timer(
                "test(nums)",
                setup=setup.format(nums_best[i])).timeit(number=10)/10

            time_two = timeit.Timer(
                "test(nums)",
                setup=setup.format(nums_worst[i])).timeit(number=10)/10
            time_best.append(time_one)
            time_worst.append(time_two)
            print('{}s: {} numbers, best'.format(time_one, len(nums_best[i])))
            print('{}s: {} numbers, worst'.format(time_one, len(nums_worst[i])))
