def get_next(p):
    next_list = [-1 for i in range(len(p)+1)]
    i = 0
    j = -1
    while i < len(p):
        if j == -1 or p[i] == p[j]:
            i += 1
            j += 1
            next_list[i] = j;
        else:
            j = next_list[j]
    return next_list



def kmp(t, p):
    next_list = get_next(p)
    i = 0
    j = 0
    while i < len(t) and j < len(p):
        if j == -1 or t[i] == p[j]:
            i += 1
            j += 1
        else:
            j = next_list[j]
    if j == len(p):
        return i -j
    else:
        return -1

print kmp('abababca', 'ababca')