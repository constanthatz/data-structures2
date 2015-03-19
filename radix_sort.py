from Queue import Queue
import random
import timeit


def radix_sort(a_list):
    queue_list = [Queue() for i in range(10)]
    maximum = 0
    for item in a_list:
        if item > maximum:
            maximum = item
        queue_list[item % 10].put(item)
    a_list_pointer = 0
    for each_queue in queue_list:
        while not each_queue.empty():
            a_list[a_list_pointer] = each_queue.get()
            a_list_pointer += 1

    max_digits = len(str(maximum))
    _radix_sort(a_list, max_digits)


def _radix_sort(a_list, max_digits):
    queue_list = [Queue() for i in range(10)]
    for i in xrange(1, max_digits):
        for item in a_list:
            queue_list[(item // 10**i) % 10].put(item)
        a_list_pointer = 0
        for each_queue in queue_list:
            while not each_queue.empty():
                a_list[a_list_pointer] = each_queue.get()
                a_list_pointer += 1

if __name__ == '__main__':

        nums = [random.sample(range(10**i), 10**i) for i in xrange(4)]

        time = []

        for num in nums:
            def test(num):
                radix_sort(num)

            setup = "from __main__ import test\nnum = {}"

            time_one = timeit.timeit(
                "test(num)",
                setup=setup.format(num), number=10)/10.0

            print('{}s: {} numbers'.format(time_one, len(num)))
            time.append(time_one)
