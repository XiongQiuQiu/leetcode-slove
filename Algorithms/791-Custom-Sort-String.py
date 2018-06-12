class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        num_t = collections.Counter(T)
        ans = ''
        for i in S:
            ans += i * num_t[i]
            del num_t[i]
        return ans + ''.join(k*v for k,v in num_t.items())
        