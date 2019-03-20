def permutation(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in permutation(elements[1:]):
            # print 'perm:'+ str(perm)
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def perm(s=''):
    if len(s) <= 1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in perm(s[0:i] + s[i + 1:]):
            sl.append(s[i] + j)
    return sl

if __name__ == "__main__":

    s='Diei'
    for item in list(permutation(list(s))):
        pass
        # print ''.join(item)
    print(perm(s))

