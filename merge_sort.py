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
    while i < len(lists)-2:
        new_sublist = []
        while lists[i]:
            
            for j in range(len(lists[i])):
                for k in range(len(lists[i+1])):
                    if lists[i][j] < lists[i][k]:
                        new_sublist.append(lists[i][j])


                 new_sublist.append(lists[i][j], lists[i+1][j])





                new_sublistappend








    list_len = len(lists[0])

    while list_len / 2 > 1:

        list_len = list_len / 2
        for a_list in lists:





        lists = [[the_list[0:list_len]], [[the_list]]




    for i in xrange(0, len(the_list), 2):
        if the_list[i] < len(the_list):
            if the_list[i+1] > the_list[i]:
                the_list[i], the_list[i+1] = the_list[i+1], the_list[i]
    for 