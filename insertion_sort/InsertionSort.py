def insertion_sort(data):
    length = len(data)
    if (length <= 1):
        return data
    j = 0
    for i in range(length):
        val = data[i]
        current = i
        prev = i - 1
        while prev >= 0:
            val = data[current]
            val2 = data[prev]
            if val < val2:
                data[current] = val2
                data[prev] = val
            else:
                break
            prev -= 1
            current -= 1
    return data




test = [1, 2, 3, 4, 5, 6]
test2 = [7, 4, 1, 5, 3]
test3 = [5, 2, 4, 6, 1, 3]
test4 = [5, 4, 4, 1, 1]
test5 = [-1, 5, 3, 4, 0]
test6 = [ 7, 6, 5, 4, 3]
#print(insertion_sort(test))
#print(insertion_sort(test2))
#print(insertion_sort(test3))
#print(insertion_sort(test4))
#print(insertion_sort(test5))
#print(insertion_sort(test6))