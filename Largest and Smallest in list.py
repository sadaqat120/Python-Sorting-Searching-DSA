def largest(given_list):
    if len(given_list)!=0:
        large_number=given_list[0]
        for i in range(1, len(given_list)):
            if large_number<given_list[i]:
                large_number=given_list[i]
        return "The largest number is", large_number
    return "List have no length"


def smallest(given_list):
    if len(given_list)!=0:
        small_number=given_list[0]
        for i in range(1, len(given_list)):
            if small_number>given_list[i]:
                small_number=given_list[i]
        return "The smallest number is", small_number
    return "List have no length"

listy = [50, 70, 90, 110, 40, 20, 53, 72, 24, 73, 38, 21, 42, 164, 120]
print(largest(listy))
print(smallest(listy))
