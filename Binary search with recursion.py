def binary_search(given_list, number):
    print(given_list)
    right=len(given_list)-1
    left=0
    if left>right:
        return False
    mid=(left+right)//2
    if given_list[mid]==number:
        return True
    else:
        if number<given_list[mid]:
            return binary_search(given_list[left:mid], number)
        else:
            return binary_search(given_list[mid+1:right+1], number)
listy = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,23,45,45,454,789,788,799,812]
print(binary_search(listy, 1233))
