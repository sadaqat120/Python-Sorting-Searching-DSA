def sequential_search(given_list, number):
    for i in given_list:
        if i==number:
            return True
    return False

list1=[1, 2, 34, 352, 5, 32, 5, 43, 543, 6, 43, 67, 54, 7, 547, 45, 87, 56, 8, 65, 875, 6, 43, 6523, 5, 23, 5, 23, 5]
print(sequential_search(list1, 10))
