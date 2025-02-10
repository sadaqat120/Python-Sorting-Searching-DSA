def bubble_sort(given_list):
    for i in range(1, len(given_list)):
        for j in range(0, len(given_list)-i):
            if given_list[j]>given_list[j+1]:
                given_list[j], given_list[j+1]=given_list[j+1], given_list[j]
    return given_list

listy = [50, 70, 90, 110, 40, 20, 53, 72, 24, 73, 38, 21, 42, 164, 120]
print(bubble_sort(listy))
