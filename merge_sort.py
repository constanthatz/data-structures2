import timeit


def merge_sort(the_list):
    lists = [the_list]
    while len(lists[0]) > 1:
        lists = split(lists)
    while len(lists) > 1:
        lists = sort(lists)


def split(lists):
    new_list = []
    for item in lists:
        new_list.append(item[:len(item)/2])
        new_list.append(a_list[len(item)/2:])
    return new_list


def sort(lists):
    new_list = []
    for i in xrange(len(lists)-1):
        merge(lists[i], lists[i+1])


def merge(list1, list2):
    new_list = []
    while list1:
        try:
            if list1[0] < list2[0]:
                new_list.append(list1.pop(0))
            else:
                new_list.append(list2.pop(0))
        except IndexError:
            new_list.append(list1.pop(0))
    new_list.extend(list2)

    return new_list

if __name__ == '__main__':
        nums_best = [range(0, 10**i) for i in xrange(6)]
        # nums_worst = [item[::-1] for item in nums_best]

        # time_best = []
        # time_worst = []

        # for i in xrange(len(nums_best)):
        #     def test(nums):
        #         merge_sort(nums)

        #     setup = "from __main__ import test\nnums = {}"

        #     time_best.append(timeit.Timer(
        #         "test(nums)",
        #         setup=setup.format(nums_best[i])).timeit(number=10000))
        #     time_worst.append(timeit.Timer(
        #         "test(nums)",
        #         setup=setup.format(nums_worst[i])).timeit(number=10000))

        # print(time_best)
        # print(time_worst)

        list1 = [3, 7]
        list2 = [1, 13]
        print(merge(list1, list2))
