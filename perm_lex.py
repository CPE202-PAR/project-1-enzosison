# string -> List of strings
# Returns list of permutations for input string
# e.g. 'ab' -> ['ab', 'ba']; 'a' -> ['a']; '' -> []
def perm_gen_lex(str_in):
    list = []
    if not str_in:
        return []
    if len(str_in) == 1:
        return [str_in]
    for i in range(len(str_in)):
        new_string = str_in.replace(str_in[i], '')
        permutation = perm_gen_lex(new_string)
        for letter in permutation:
            list.append(str_in[i] + letter)
    return list


