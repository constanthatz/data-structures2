import timeit


def merge_sort(the_list):
    for i in xrange(0, len(the_list), 2):
        if the_list[i] < len(the_list):
            if the_list[i+1] > the_list[i]:
                the_list[i], the_list[i+1] = the_list[i+1], the_list[i] 
            else:
                pass

if __name__ == '__main__':
        nums_best = [range(0, 10**i) for i in xrange(6)]
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
