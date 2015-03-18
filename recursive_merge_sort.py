import timeit


def merge_sort(a_list):
    if len(a_list) <= 1:
        return a_list
    else:
        return merge(merge_sort(a_list[:len(a_list) / 2]),
                     merge_sort(a_list[len(a_list) / 2:]))


def merge(left, right):
    new_list = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            new_list.append(left[left_idx])
            left_idx += 1
        else:
            new_list.append(right[right_idx])
            right_idx += 1

    while left_idx < len(left):
        new_list.append(left[left_idx])
        left_idx += 1

    while right_idx < len(right):
        new_list.append(right[right_idx])
        right_idx += 1
    return new_list

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
