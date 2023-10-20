w, h = 6, 6;
arr = [[0 for x in range(w)] for y in range(h)]

arr[0][0] = 1
arr[0][1] = 1
arr[0][2] = 1

arr[1][1] = 1

arr[2][0] = 1
arr[2][1] = 1
arr[2][2] = 1

arr[3][2] = 2
arr[3][3] = 4
arr[3][4] = 4

arr[4][3] = 2

arr[5][2] = 1
arr[5][3] = 2
arr[5][4] = 4

for i in arr:
    print (i)


def hourglassSum(arr):
    result = 0
    to_string = ""
    # for i in range(4):
    #     result = result + arr[i][i]
    #     to_string = to_string + str(arr[i][i])
    #
    #     result = result + arr[i][i + 1]
    #     to_string = to_string + str(arr[i][i + 1])
    #
    #     result = result + arr[i][i + 2]
    #     to_string = to_string + str(arr[i][i + 2])
    #
    #     result = result + arr[i + 1][i + 1]
    #     to_string = to_string + str(arr[i + 1][i + 1])
    #
    #     result = result + arr[i + 2][i]
    #     to_string = to_string + str(arr[i + 2][i])
    #
    #     result = result + arr[i + 2][i + 1]
    #     to_string = to_string + str(arr[i + 2][i + 1])
    #
    #     result = result + arr[i + 2][i + 2]
    #     to_string = to_string + str(arr[i + 2][i + 2])
    #     print (to_string)
    #     to_string = ""
    #     print (result)
    #     result = 0

    for x in range(4):
        for y in range(4):
            result = arr[x][y]
            to_string = str(arr[x][y]) + ", "

            result = result + arr[x][y + 1]
            to_string = to_string + str(arr[x][y + 1]) + ", "

            result = result + arr[x][y + 2]
            to_string = to_string + str(arr[x][y + 2]) + ", "

            result = result + arr[x + 1][y + 1]
            to_string = to_string + str(arr[x + 1][y + 1]) + ", "

            result = result + arr[x][y + 2]
            to_string = to_string + str(arr[x][y + 2]) + ", "

            result = result + arr[x + 2][y + 1]
            to_string = to_string + str(arr[x + 2][y + 1]) + ", "

            result = result + arr[x + 2][y + 2]
            to_string = to_string + str(arr[x + 2][y + 2])
        print (to_string)
        print (result)


hourglassSum(arr)

# 00, 01, 02, 11, 20, 21, 22
#
# 11, 12, 13, 22, 31, 32, 33
#
# 22, 23, 24, 33, 42, 43, 44
test-push
