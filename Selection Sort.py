def selection_sort(given_list):
    for j in range(len(given_list)-1):
        smallest=j
        for i in range(j+1, len(given_list)):
            if given_list[i]<given_list[smallest]:
                smallest=i
        given_list[j], given_list[smallest]=given_list[smallest], given_list[j]
    return given_list
list1=[50, 70, 90, 110, 40, 20, 53, 72, 24, 73, 38, 21, 42, 164, 120]
print(selection_sort(list1))
