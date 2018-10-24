def array_left_rotation(array, n):
    return_array = []
    # Base Case
    if n == 0:
        return array
    else:
        for i in range(n, len(array)):
            return_array.append(array[i])
        for i in range(0, n):
            return_array.append(array[i])
    return return_array


array = [1, 2, 3, 4, 5]
n = 2
print (array_left_rotation(array, n))

q1 = [2, 1, 5, 3, 4]
q2 = [2, 5, 1, 3, 4]


def New_Year_Chaos(q):
    hoplist = {}
    for i in range(len(q)):
        pass