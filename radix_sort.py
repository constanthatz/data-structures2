from queue import Queue

def radix_sort(a_list):
    queue_list = [Queue() for i in range(10)]
    for item in a_list:
        queue_list[item % 10].put(item)
    a_list_pointer = 0
    for each_queue in queue_list:
        while not each_queue.empty():
            a_list[a_list_pointer] = each_queue.get()
