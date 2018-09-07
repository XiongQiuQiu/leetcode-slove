def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    sd = {'(': ')', '[': ']', '{': '}'}
    stack = []
    for symbol in s:
        if symbol in sd:
            stack.append(symbol)
        elif sd[stack.pop()] != symbol:
            return False
    return True

isValid('(]')