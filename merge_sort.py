def merge_sort(the_list):
    for i in xrange(0, len(the_list), 2):
        if the_list[i] < len(the_list):
            if the_list[i+1] > the_list[i]:
                the_list[i], the_list[i+1] = the_list[i+1], the_list[i] 
            else: