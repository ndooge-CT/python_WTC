
def find_min(L):
    """TODO: complete for Step 1"""
    for i in L:
        if not isinstance(i, int):
            return -1
    if len(L) == 0:
        return -1
    if len(L) == 1:
        return L[0]
    else:
        min = find_min(L[1:])
        x = L[0]
        if (min < x):
            x = min
        return x
    
def sum_all(n):
    """TODO: complete for Step 2"""
    for i in n:
        if not isinstance(i, int):
            return -1
    if len(n) == 0:
        return -1
    if len(n) == 1:
        return n[0]
    else:
        return n[0] + sum_all(n[1:]) 

def find_possible_strings(character_set,n):
    """TODO: complete for Step 3"""
    for i in character_set:
        if type(i) != str:
            return []
    
    if n == 1:
        return character_set

    else:
        prefix = []
        for i in character_set:
            for  suffix in find_possible_strings(character_set, n-1):
                prefix += [i + suffix]
        return prefix

if __name__ == "__main__":
    lst = [10,156,2,999, 5,0]
    #set[] = {'x', 'y'}, k = 3
    print(find_min(lst))
    n = [5]
    print (sum_all(n))
    char_set = ['a','b','c']
    num = 1
    #possible_strings = permutations(char_set,3)
    print(find_possible_strings(char_set, num))