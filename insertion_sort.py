def insertion_sort(the_list):
    for index, item in enumerate(the_list):
        try:
            while item < the_list[index-1]:
                the_list[index], the_list[index-1] = the_list[index-1], item
                index -= 1
        except IndexError:
            pass
