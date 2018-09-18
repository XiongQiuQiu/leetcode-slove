
def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """

    def generate(p, left, right, parenths=[]):
        if left: generate(p + '(', left - 1, right)
        if right > left: generate(p + ')', left, right - 1)
        if not right: parenths += p,
        return parenths

    return generate('', n, n)
generateParenthesis(3)
