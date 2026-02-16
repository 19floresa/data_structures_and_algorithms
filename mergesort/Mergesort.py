
def merge(bot, top):
    new_data = []
    i = 0
    j = 0
    max_i = len(bot)
    max_j = len(top)
    max_ij = max_i + max_j
    for _ in range(max_ij):
        if i == max_i:
            new_data.append(top[j])
            j += 1
            continue
        elif j == max_j:
            new_data.append(bot[i])
            i += 1
            continue
        else:
            val1 = bot[i]
            val2 = top[j]
            if val1 < val2:
                new_data.append(val1)
                i += 1
            else:
                new_data.append(val2)
                j += 1
    return new_data
    

def mergesort_helper(data):
    length = len(data)
    if length <= 1:
        return data
    mid = length // 2
    new_bot = mergesort_helper(data[0 : mid])
    new_top = mergesort_helper(data[mid : length])
    print("start")
    print(data)
    print(data[0 : mid])
    print(data[mid : length])
    print(new_bot)
    print(new_top)
    print("end")
    new_data = merge(new_bot, new_top)
    return new_data

def mergesort(data):
    return mergesort_helper(data)



test1  = [ 70, 30, 50, 10 ]
print(mergesort(test1))
