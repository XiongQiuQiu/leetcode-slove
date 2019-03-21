def dailyTemperatures(T):
    """
    :type T: List[int]
    :rtype: List[int]
    """
    stack = []
    res = [0] * len(T)

    for idx in range(len(T) - 1, -1, -1):
        while stack and T[idx] >= T[stack[-1]]:
            stack.pop()

        if stack:
            res[idx] = stack[-1] - idx

        stack.append(idx)

    return res
dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])