import timeit


def merge_sort(a_list):
    if len(a_list) > 1:
        middle = len(a_list) / 2
        left = a_list[:middle]
        right = a_list[middle:]

        merge_sort(left)
        merge_sort(right)

        left_idx, right_idx, a_list_idx = 0, 0, 0
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                a_list[a_list_idx] = left[left_idx]
                left_idx += 1
            else:
                a_list[a_list_idx] = right[right_idx]
                right_idx += 1
            a_list_idx += 1

        while left_idx < len(left):
            a_list[a_list_idx] = left[left_idx]
            left_idx += 1
            a_list_idx += 1

        while right_idx < len(right):
            a_list[a_list_idx] = right[right_idx]
            right_idx += 1
            a_list_idx += 1

    return a_list

# def merge(left, right):
#     result = []
#     while left and right:
#         if left[0] <= right[0]:
#             result.append(left[0])
#             left = left[1:]
#         else:
#             result.append(right[0])
#             right = right[1:]
#     while left:
#         result.append(left[0])
#         left = left[1:]
#     while right:
#         result.append(right[0])
#         right = right[1:]
#     return result


if __name__ == '__main__':
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

        # # list1 = [3, 7]
        # # list2 = [1, 13]
        # # print(merge(list1, list2))

        # # lists = [[1], [], [12], [3], [5]]
        # # while len(lists) > 1:
        # #     lists = mergeAll(lists)
        # # print(lists)

        # the_list = [5, 17, 4, 3, -1, 6, 37]
        # print(the_list)
        # print(merge_sort(the_list))