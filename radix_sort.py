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
    _radix_sort(a_list, max_digits, queue_list)


def _radix_sort(a_list, max_digits, queue_list):
    for i in xrange(1, max_digits):
        for item in a_list:
            queue_list[(item // 10**i) % 10].put(item)
        a_list_pointer = 0
        for each_queue in queue_list:
            while not each_queue.empty():
                a_list[a_list_pointer] = each_queue.get()
                a_list_pointer += 1


def string_radix_sort(string_list):
    queue_list = [Queue() for i in range(57)]
    maximum = 0
    for string in string_list:
        if len(string) > max:
            maximum = len(string)
        char = string[-1]
        queue_list[ord(char)-65].put(string)
        string_list_pointer = 0
        for each_queue in queue_list:
            while not each_queue.empty():
                string_list[string_list_pointer] = each_queue.get()
                string_list_pointer += 1

    _string_radix_sort(string_list, maximum, queue_list)


def _string_radix_sort(string_list, maximum, queue_list):
    for i in xrange(1, maximum):
        for string in string_list:
            try:
                queue_list[ord(string[-1-i])-65].put(string)
            except IndexError:
                queue_list[0].put(string)
        string_list_pointer = 0
        for each_queue in queue_list:
            while not each_queue.empty():
                string_list[string_list_pointer] = each_queue.get()
                string_list_pointer += 1






if __name__ == '__main__':

        nums = [random.sample(range(10**i), 10**i) for i in xrange(7)]

        time = []

        for num in nums:
            def test(num):
                radix_sort(nums)

            setup = "from __main__ import test\nnum = {}"

            time_one = timeit.Timer(
                "test(nums)",
                setup=setup.format(num)).timeit(number=10000)
            
            print(time_one)
            time.append(time_one)

        print(time)
