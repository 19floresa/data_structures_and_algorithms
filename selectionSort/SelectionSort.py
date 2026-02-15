def selection_sort(data):
    length = len(data)
    if length <= 1:
        return data
    for i in range(length):
        index_least = i
        val = data[i]
        for j in range(i+1, length):
            val2 = data[j]
            if val2 < val:
                index_least = j
                val = val2
        if index_least != i:
            temp = data[index_least]
            data[index_least] = data[i]
            data[i] = temp
    return data

# test1 = [64, 25, 12, 22, 11]
# test2 = [7, 12, 9, 11, 3]
# test3 = [1, 3, 4, 7, 9]
# test4 = [9, 7, 4, 3, 1]
# test5 = [1, 4, 3, 9, 7]
# test6 = [4, 2, 4, 1, 2]
# print(selection_sort(test1))
# print(selection_sort(test2))
# print(selection_sort(test3))
# print(selection_sort(test4))
# print(selection_sort(test5))
# print(selection_sort(test6))