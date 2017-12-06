class Solution(object):
    def flipLights(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if m *n ==0: return 1
        if n == 1 : return 2
        if n == 2: return (3 - m)
        if m == 1 : return 1
        if m == 2: return 7
        return 8
