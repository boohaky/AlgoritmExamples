from src.sort.BaseSort import BaseSort


class SelectionSort(BaseSort):

    def sort(self, list_to_sort):
        current_pos = 0
        while current_pos < len(list_to_sort) - 1:
            min_element_index = current_pos
            i = current_pos + 1
            # finding min value
            while i < len(list_to_sort):
                if list_to_sort[i] < list_to_sort[min_element_index]:
                    min_element_index = i
                i += 1
            # swap
            temp = list_to_sort[current_pos]
            list_to_sort[current_pos] = list_to_sort[min_element_index]
            list_to_sort[current_pos] = temp
            current_pos += 1
        print("SelectionSort " + str(list_to_sort))


class BubbleSort(BaseSort):

    def sort(self, list_to_sort):
        for i in range(len(list_to_sort) - 1):
            for j in range(len(list_to_sort) - 1 - i):
                # check and swap next to each other elements
                if list_to_sort[j + 1] < list_to_sort[j]:
                    list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
        print("BubbleSort " + str(list_to_sort))


class MergeSort(BaseSort):

    def sort(self, list_to_sort):
        final_list = self.mergeOneSort(list_to_sort)
        print("MergeSort " + str(final_list))

    def mergeOneSort(self, list_to_sort):
        list_length = len(list_to_sort)
        if list_length < 2:
            return list_to_sort
        center_index = list_length // 2
        # divide list into two separate
        return self.mergeTwoSort(self.mergeOneSort(newList(list_to_sort[:center_index])),
                                 self.mergeOneSort(newList(list_to_sort[center_index:])))

    def mergeTwoSort(self, list1, list2):
        result_list = []
        # init of all secondary data
        len_list_1 = len(list1)
        len_list_2 = len(list2)
        result_len = len_list_1 + len_list_2
        count1 = 0
        count2 = 0

        # check every element in two arrays and set for correct position
        for pos in range(0, result_len):
            if count1 < len_list_1 and count2 < len_list_2:
                if list1[count1] < list2[count2]:
                    result_list.append(list1[count1])
                    count1 += 1
                else:
                    result_list.append(list2[count2])
                    count2 += 1
            elif count1 < len(list1):
                result_list.append(list1[count1])
                count1 += 1
            else:
                result_list.append(list2[count2])
                count2 += 1
        return result_list


class QuickSort(BaseSort):

    def sort(self, list_to_sort):
        final_list = self.quickSort(list_to_sort)
        print("QuickSort " + str(final_list))

    def quickSort(self, list_to_sort):
        len_list = len(list_to_sort)
        if len(list_to_sort) < 2:
            return list_to_sort
        # choose pivot element
        pivot = list_to_sort[int(len_list / 2)]
        below = []
        above = []
        same = []
        # sort every element below, same and above
        for pos in range(0, len_list):
            list_value = list_to_sort[pos]
            if list_value < pivot:
                below.append(list_value)
            elif list_value > pivot:
                above.append(list_value)
            else:
                same.append(list_value)
        return self.quickSort(below) + same + self.quickSort(above)


class InsertionSort(BaseSort):

    def sort(self, list_to_sort):
        for pos in range(1, len(list_to_sort)):
            i = pos - 1
            while (i > -1) and list_to_sort[i + 1] < list_to_sort[i]:
                list_to_sort[i + 1], list_to_sort[i] = list_to_sort[i], list_to_sort[i + 1]
                i -= 1
        print("InsertionSort " + str(list_to_sort))


def newList(current_list):
    new_list = []
    for pos in current_list:
        new_list.append(pos)
    return new_list


if __name__ == '__main__':
    list_to_sort = [45, 20, 5, 9, 6]
    print(list_to_sort)
    SelectionSort().sort(newList(list_to_sort))
    BubbleSort().sort(newList(list_to_sort))
    MergeSort().sort(newList(list_to_sort))
    QuickSort().sort(newList(list_to_sort))

    InsertionSort().sort(newList(list_to_sort))
