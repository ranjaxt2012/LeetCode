def fact(n):
    # Base Case
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def addition(n):
    # Base Case
    if n == 0:
        return 0
    else:
        return n + addition(n - 1)


def splitAddition(n):
    # Base Case
    if len(str(n)) == 1:
        return n
    else:
        return n % 10 + splitAddition(n / 10)


def reverseString(s):
    if len(s) <= 1:
        return s

    return reverseString(s[1:]) + s[0]

print reverseString("ABC")

# DID NOT GET IT
# Pick one letter of of each element, a, b, c
# Base case would be when we have gone thought a, b and c
def stringPermutation(s):
    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for i, let in enumerate(s):

            # For every permutation resulting from Step 2 and 3 described above
            for perm in stringPermutation(s[:i] + s[i + 1:]):
                # Add it to output
                out += [let + perm]
    return out


def fibnatch(number, ret_num):
    ret_num = ret_num + number
    if number == 1:
        return ret_num

    return fibnatch(number - 1, ret_num)


if __name__ == "__main__":
    print ("Enter Number of the foctorial: ")
    # num = int(input())
    # print (fact(num))
    # print (addition(num))
    # print (splitAddition('1234'))
    print reverseString('abc')
    print stringPermutation("abc")
    print fibnatch(10, 0)
