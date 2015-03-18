def quick_sort(a_list):
    # select pivot
    # sort around pivot
    # join

    pivot = select_pivot(a_list)




def select_pivot(a_list):

    if a_list[0] <= a_list[len(a_list)/2] <= a_list[-1] or a_list[-1] <= a_list[len(a_list)/2] <= a_list[0]:
        return a_list[len(a_list)/2]
    elif a_list[len(a_list)/2] <= a_list[0] <= a_list[-1] or a_list[-1] <= a_list[0] <= a_list[len(a_list)/2]:
        return a_list[0]
    else:
        return a_list[-1]
