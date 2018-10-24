Binary_Input_String = "00110101 1011010100110101 00110101 10110101001101010 01101010 01101011011010100110101101101010011010100110101"
Binary_Input_String = "00110101101101010011010100110101101101010011010100110101001101011011010100110101101101010011010100110101"


print (Binary_Input_String)


def NthNumberIndex(Binary_Input_String, j):
    j = j - 1
    Message_Starting_Point = 0
    hops = 0
    Message_Count = 0

    print ("****", Message_Count, hops, j)

    while hops < len(Binary_Input_String) and Message_Count <= j:
        if Binary_Input_String[hops] == str(0):
            Message_Starting_Point = hops
            hops = hops + 8
            Message_Count = Message_Count + 1
            print ("Hopping 8", hops, "Message_Count", Message_Count)

        elif Binary_Input_String[hops] == str(1):
            Message_Starting_Point = hops
            hops = hops + 16
            Message_Count = Message_Count + 1
            print ("Hopping 16", hops, "Message_Count", Message_Count)
        else:
            print ("Unreadable Binary")


    return [Message_Starting_Point, hops]


print NthNumberIndex(Binary_Input_String, 3)
