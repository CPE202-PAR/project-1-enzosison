# Node list is
# None or
#Node(value, rest), where rest is the rest of the list
class Node:
    def __init__(self, value, rest):
        self.value = value
        self.rest = rest

    def __eq__(self, other):
        return ((type(other) == Node)
                and self.value == other.value
                and self.rest == other.rest
                )

    def __repr__(self):
        return ("Node({!r}, {!r})".format(self.value, self.rest))

# a StrList is one of
# - None, or
# - Node(string, StrList)

# StrList -> string
# Returns first (as determined by Python compare) string in StrList
# If StrList is empty (None), return None
# Must be implemented recursively
def first_string(strlist):
    if strlist is None:
        return None
    if strlist.rest is None:
        return strlist.value
    smallest = strlist.value
    if smallest < first_string(strlist.rest):
        return smallest
    else:
        return first_string(strlist.rest)

# StrList -> (StrList, StrList, StrList)
# Returns a tuple with 3 new StrLists,
# the first one with strings from the input list that start with a vowel,
# the second with strings from the input list that start with a consonant,
# the third with strings that don't start with an alpha character
# Must be implemented recursively

# def split_list(strlist):
#     if strlist is None:
#         return None
#     if strlist.rest is None:
#         return strlist.value
#     vowel_list = []
#     for i in strlist:
#         if strlist[i[0]] == a or strlist[i[0]] == e or strlist[i[0]] == i or strlist[i[0]] == o or strlist[
#             i[0]] == u:
#             vowel_list.append(strlist[i])
#     consonants = [B, C, D, F, G, H, J, K, L, M, N, P, Q, R, S, T, V, X, Z, W, Y]
#     consonant_list = []
#     for i in strlist:
#         if strlist[i[0]] in consonants:
#             consonant_list.append(strlist[i])
#     number_list = []
#     for i in strlist:
#         if i[0].isdigit:
#             number_list.append(strlist[i])
#     final_list = [vowel_list, consonant_list, number_list]
#     return final_list

def split_list(strlist):
    if strlist is None:
        return (None, None, None)
    # if strlist.rest is None:
    #     return strlist
    lists = split_list(strlist.rest)
    if strlist.value != "" and strlist.value[0] in 'aeiouAEIOU':
        return (Node(strlist.value, lists[0]), lists[1], lists[2])
    if strlist.value != "" and strlist.value[0] in 'bcdfghjklmnpqrstvxzwyBCDFGHJKLMNPQRSTVXZWY':
        return (lists[0], Node(strlist.value, lists[1]), lists[2])
    else:
        return (lists[0], lists[1], Node(strlist.value, lists[2]))

    return (lists[0], lists[1], lists[2])

    # else:
    # if strlist.value[0] in 'aeiouAEIOU':
    #     strlist.rest = split_list(strlist.rest)
    #     tup1 = (strlist)
    # else:
    #     return split_list(strlist.rest)
    # if strlist.value[0] in 'bcdfghjklmnpqrstvxzwyBCDFGHJKLMNPQRSTVXZWY':
    #     strlist.rest = split_list(strlist.rest)
    #     tup2 = (strlist)
    #     print(tup2)
    # else:
    #     return split_list(strlist.rest)

#    if strlist.value in 'bcdfghjklmnpqrstvxzwyBCDFGHJKLMNPQRSTVXZWY':
#       strlist.rest = split_list(strlist.rest)

# print(split_list(Node('abc', Node("Yellow", Node('42', Node("lime", Node('Ethan', Node('$7.25', None))))))))



