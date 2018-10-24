'''
https://leetcode.com/problems/container-with-most-water/description
Input: [1,8,6,2,5,4,8,3,7]
Output: 49
'''
from collections import deque

Input = [1, 8, 6, 2, 5, 4, 8, 3, 7]

Input_Queue = deque()
for i in Input:
    Input_Queue.append(i)


def Wall_Distance_Zero(Input):
    Input_With_Distance = {}
    Count = 1
    for I in Input:
        Input_With_Distance[Count] = I
        Count += 1
    return Input_With_Distance


def Bucket_Max_Area_Bruit_Force(Input_With_Distance):
    Areas = []
    for I in Input_With_Distance:
        for J in Input_With_Distance:
            W = (max(I, J) - min(I, J))
            H = min(Input_With_Distance[I], Input_With_Distance[J])
            A = W * H
            Areas.append(A)
    return max(Areas)


def SideBySideArea(Input_Queue):
    max_area = 0

    left_distance = 1
    right_distnace = len(Input_Queue)

    right_node = Input_Queue.pop()
    left_node = Input_Queue.popleft()

    while len(Input_Queue) >= 2:

        print (right_distnace, left_distance, right_node, left_node)
        width = (right_distnace - left_distance)
        height = min(left_node, right_node)

        if (width * height) > max_area:
            max_area = width * height

        if left_node > right_node:
            right_node = Input_Queue.pop()
            right_distnace -= 1
        else:
            left_node = Input_Queue.popleft()
            left_distance += 1

    return max_area


Input_With_Distance = Wall_Distance_Zero(Input)
Areas = Bucket_Max_Area_Bruit_Force(Input_With_Distance)
print Areas

Input_Queue_Results = SideBySideArea(Input_Queue)
print Input_Queue_Results
