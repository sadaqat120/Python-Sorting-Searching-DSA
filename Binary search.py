def bubble_sort(given_list):
    for i in range(1, len(given_list)):
        for j in range(0, len(given_list)-i):
            if given_list[j]>given_list[j+1]:
                given_list[j], given_list[j+1]=given_list[j+1], given_list[j]
    return given_list


def binary_search(given_list, number):
    sorted_list=bubble_sort(given_list)
    print("Sorted list: ", sorted_list)
    right=len(sorted_list)-1
    left=0
    while left<=right:
        mid=(left+right)//2
        if sorted_list[mid]==number:
            print(True)
            return "Index of number is", mid
        else:
            if number<sorted_list[mid]:
                right=mid-1
            else:
                left=mid+1
    return False

listy = [50, 70, 90, 110, 40, 20, 53, 72, 24, 73, 38, 21, 42, 164, 120]
print(binary_search(listy, 120))
