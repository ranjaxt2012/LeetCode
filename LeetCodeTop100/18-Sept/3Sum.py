import collections

SumArray = [-1, 0, 1, 2, -1, -4]
SumArray.sort()


# [-4, -1, -1, 0, 1, 2]

def GetNegativeNumberSet(SumArray):
    SortedSet = set()
    i = 1

    while i > 0:
        i = SumArray.pop()

    for S in SumArray:
        SortedSet.add(S)

    return SortedSet


def ThreeSum(SumArray):
    for s in range(len(SumArray) - 1):
        two_sum = SumArray[s] + SumArray[s + 1]
        if int(abs(two_sum)) in SumArray:
            print (SumArray[s], SumArray[s + 1], abs(two_sum))


# NegtiveSumSet = GetNegativeNumberSet(SumArray)
ThreeSum(SumArray)
