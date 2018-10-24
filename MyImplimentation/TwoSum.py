def TwoSum(lst, s):
    for n in range(len(lst)):

        firstnumber = lst[n]
        secondnumber = 9 - lst[n]
        if secondnumber in lst:
            return firstnumber, secondnumber


print TwoSum([2, 7, 9, 8], 9)


def longestSubstringWithoutRepeting(s):
    sub_string = ""

    # BaseCase
    if len(s) <= 1:
        return s
    else:
        temp_string = ""
        for i in s:
            if i not in temp_string:
                temp_string = temp_string + str(i)
            elif len(sub_string) < len(temp_string):
                sub_string = temp_string
    return sub_string


print longestSubstringWithoutRepeting('abcabcfpcbb')
