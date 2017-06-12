def permutation(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in permutation(elements[1:]):
            # print 'perm:'+ str(perm)
            for i in range(len(elements)):
                print perm[:i] + elements[0:1] + perm[i:]
                yield perm[:i] + elements[0:1] + perm[i:]

if __name__ == "__main__":
    s='Diei'
    for item in list(permutation(list(s))):
        pass
        # print ''.join(item)