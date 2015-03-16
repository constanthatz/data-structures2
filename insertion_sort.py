import timeit


def insertion_sort(the_list):
    for index, item in enumerate(the_list):
        while item < the_list[index-1] and index > 0:
            the_list[index], the_list[index-1] = the_list[index-1], item
            index -= 1

if __name__ == '__main__':
        nums_best = [range(0, 1*(10**i)) for i in xrange(5)]
        nums_worst = [item[::-1] for item in nums_best]

        time_easy = []
        time_hard = []

        for i in xrange(len(nums_best)):
            def test_best(nums):
                insertion_sort(nums)

            def test_worst(nums):
                insertion_sort(nums)

            setup_best = """from __main__ import test_best\nnums = {}"""
            setup_worst = """from __main__ import test_worst\nnums = {}"""

            time_easy.append(timeit.Timer(
                "test_best(nums)",
                setup=setup_best.format(nums_best[i])).timeit(number=10000))
            time_hard.append(timeit.Timer(
                "test_worst(nums)",
                setup=setup_worst.format(nums_worst[i])).timeit(number=10000))

        print(time_easy)
        print(time_hard)
