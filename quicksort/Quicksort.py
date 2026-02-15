def quicksort(data, index_start, index_end):
    if len(data) <= 1:
        return data
    if (index_start >= 0) and (index_start < index_end):
        (start, end) = partition(data, index_start, index_end)
        data = quicksort(data, index_start, start-1)
        data = quicksort(data, end+1, index_end)
    return data

def partition(data, index_start, index_end):
    pivot = data[(index_start + index_end) // 2]
    lt = index_start
    eq = index_start
    gt = index_end
    while (eq <= gt):
        val_lt = data[lt]
        val_eq = data[eq]
        val_gt = data[gt]
        if val_eq < pivot:
            data[lt] = val_eq
            data[eq] = val_lt
            lt += 1
            eq += 1
        elif val_eq > pivot:
            data[eq] = val_gt
            data[gt] = val_eq
            gt -= 1
        else:
            eq += 1

    return (lt, gt)

# test1 = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
# test2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1] 
# test3 = [42]
# test4 = [4, 2, 4, 1, 4, 3, 4, 5]
# test5 = [7, 7, 7, 7, 7]
# print(quicksort(test1, 0, len(test1)-1))
# print(quicksort(test2, 0, len(test2)-1))
# print(quicksort(test3, 0, len(test3)-1))
# print(quicksort(test4, 0, len(test4)-1))
# print(quicksort(test5, 0, len(test5)-1))