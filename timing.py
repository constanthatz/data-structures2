import random
import timeit
from insertion_sort import insertion_sort
from recursive_merge_sort_other import merge_sort
from quick_sort import quicksort
from radix_sort import radix_sort


if __name__ == '__main__':
    nums = [random.sample(range(10**i), 10**i) for i in xrange(4)]

    sorts = ['Insertion Sort', 'Merge Sort', 'Quick Sort', 'Radix Sort']
    times = [[] for i in xrange(len(sorts))]

    for num in nums:
        def test_ins(num):
            insertion_sort(num)

        def test_merge(num):
            merge_sort(num)

        def test_quick(num):
            quicksort(num)

        def test_radix(num):
            radix_sort(num)

        time_ins = timeit.timeit(
            "test_ins(num)",
            setup="from __main__ import test_ins\nnum = {}"
                  .format(num), number=10)/10.0

        time_merge = timeit.timeit(
            "test_merge(num)",
            setup="from __main__ import test_merge\nnum = {}"
                  .format(num), number=10)/10.0

        time_quick = timeit.timeit(
            "test_quick(num)",
            setup="from __main__ import test_quick\nnum = {}"
                  .format(num), number=10)/10.0

        time_radix = timeit.timeit(
            "test_radix(num)",
            setup="from __main__ import test_radix\nnum = {}"
                  .format(num), number=10)/10.0

        print('{} numbers'.format(len(num)))
        print('{}s: {}'.format(time_ins, sorts[0]))
        print('{}s: {}'.format(time_merge, sorts[1]))
        print('{}s: {}'.format(time_quick, sorts[2]))
        print('{}s: {}'.format(time_radix, sorts[3]))
        print('\n')

        times.append(time_ins)
        times.append(time_merge)
        times.append(time_quick)
        times.append(time_radix)
