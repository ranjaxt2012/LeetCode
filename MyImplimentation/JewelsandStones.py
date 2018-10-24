J = "aA"
S = "aAAbbbb"


def numJewelsInStones(J, S):
    Stone_dict = {}
    for s in S:
        if Stone_dict.has_key(s):
            Existing_Stone_Count = Stone_dict[s]
            Stone_dict[s] = int(Existing_Stone_Count) + 1
        else:
            Stone_dict[s] = 1

    Jewel_Count = 0
    for j in J:
        if Stone_dict.has_key(j):
            Jewel_Count = Jewel_Count + Stone_dict[j]

    return Jewel_Count


numJewelsInStones(J, S)
