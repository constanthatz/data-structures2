import timeit
import random


def merge_sort(a_list):
    if a_list:
        return _merge_sort(a_list, 0, len(a_list)-1)
    else:
        return a_list


def _merge_sort(a_list, left, right):
    if left < right:
        center = (left + right) / 2
        _merge_sort(a_list, left, center)
        _merge_sort(a_list, center+1, right)
        merge(a_list, left, center+1, right)


def merge(a_list, A, B, C):
    new_list = []

    start = A
    middle = B
    end = C

    while A < middle and B <= end:
        if a_list[A] <= a_list[B]:
            new_list.append(a_list[A])
            A += 1
        else:
            new_list.append(a_list[B])
            B += 1
    while A < middle:
        new_list.append(a_list[A])
        A += 1
    while B <= end:
        new_list.append(a_list[B])
        B += 1

    a_list[start:end+1] = new_list

if __name__ == '__main__':
    # the_list = [-3, -2, -1, 0, 1, 2, 3, 4]
    # print(the_list)
    # merge_sort(the_list)
    # print(the_list)
    # print('\n')

    # the_list = the_list[::-1]
    # print(the_list)
    # merge_sort(the_list)
    # print(the_list)
    # print('\n')

    # the_list = random.sample(the_list, len(the_list))
    # print(the_list)
    # merge_sort(the_list)
    # print(the_list)
    # print('\n')

    nums_best = [range(0, 10**i) for i in xrange(3)]
    nums_worst = [item[::-1] for item in nums_best]

    time_best = []
    time_worst = []

    for i in xrange(len(nums_best)):
        def test(nums):
            merge_sort(nums)

        setup = "from __main__ import test\nnums = {}"

        time_best.append(timeit.Timer(
            "test(nums)",
            setup=setup.format(nums_best[i])).timeit(number=10000))
        time_worst.append(timeit.Timer(
            "test(nums)",
            setup=setup.format(nums_worst[i])).timeit(number=10000))

    print(time_best)
    print(time_worst)
