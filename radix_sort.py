from queue import Queue


def radix_sort(a_list):
    queue_list = [Queue() for i in range(10)]
    maximum = 0
    for item in a_list:
        if item > maximum:
            maximum = item
        queue_list[item % 10**i].put(item)
    a_list_pointer = 0
    for each_queue in queue_list:
        while not each_queue.empty():
            a_list[a_list_pointer] = each_queue.get()
            a_list_pointer += 1

    max_digits = len(str(maximum))
    _radix_sort(a_list, max_digits)


def _radix_sort(a_list, max_digits):
    queue_list = [Queue() for i in range(10)]
    for i in xrange(max_digits):
        for item in a_list:
            queue_list[(item // 10**i) % 10].put(item)
        a_list_pointer = 0
        for each_queue in queue_list:
            while not each_queue.empty():
                a_list[a_list_pointer] = each_queue.get()
                a_list_pointer += 1
