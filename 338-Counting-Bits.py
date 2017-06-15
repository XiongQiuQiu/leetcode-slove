# -*- coding:utf-8 -*-
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        ans = [0]
        for i in range(1, num + 1):
            ans += ans[i >> 1] + (i & 1),
        return ans