def insertion_sort(given_list):
    for i in range(0, len(given_list)-1):
        while i>-1 and given_list[i]>given_list[i+1]:
            given_list[i], given_list[i+1]=given_list[i+1], given_list[i]
            i-=1
    return given_list


def insertion_sort_by_teacher(given_list):
    for j in range(1, len(given_list)):
        key=given_list[j]
        i=j-1
        while i>0 and given_list[i]>key:
            given_list[i+1]=given_list[i]
            i-=1
        given_list[i+1]=key
    return given_list

list1 = [24, 2, 4, 2, 4, 23, 4, 235, 3, 6, 43, 3, 45, 3, 4, 634, 6, 4, 76, 45, 7, 45, 7, 568, 56, 8, 6, 9, 67, 96,
         79, 67, 6, 547, 65, 8, 6, 8, 56, 67, 4, 53, 4, 2, 4, 12, 3, 12, 423, 6, 34, 7, 45, 75, 67, 45, 6, 24, 5]
print(insertion_sort(list1))
print(insertion_sort_by_teacher(list1))
