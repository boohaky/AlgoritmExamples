def maxElement(list_to_search):
    if not isinstance(list_to_search, list):
        return -1
    len_list = len(list_to_search)
    if len_list == 1:
        return list_to_search[0]
    max_val = list_to_search[0]
    for pos in range(0, len_list):
        if list_to_search[pos] > max_val:
            max_val = list_to_search[pos]
    return 'Max element ' + str(max_val)


def binarySearch(list_to_search, element):
    low = 0
    high = len(list_to_search) - 1
    while low <= high:
        mid = (low + high) // 2
        if element < list_to_search[mid]:
            high = mid - 1
        elif element > list_to_search[mid]:
            low = mid + 1
        else:
            return "Binary Search index " + str(mid);
    else:
        return "Binary Search " + "no number";


if __name__ == '__main__':
    print(maxElement([45, 20, 5, 9, 6]))
    print(binarySearch([5, 6, 9, 45, 150, 180], 5))
