'''
Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
'''
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if len(flowerbed) == 1 :return 1 >= n if flowerbed[0] ==0 else 0>=n
        cnt=0
        pre=0
        for i in range(len(flowerbed)-1):
            if pre == 0 and flowerbed[i] ==0 and flowerbed[i+1] == 0:
                cnt += 1
                flowerbed[i] = 1
            pre = flowerbed[i]
        if flowerbed[-1] == 0 and flowerbed[-2] ==0:
            cnt += 1
        return cnt >= n

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        ans = 0
        for i, v in enumerate(flowerbed):
            if v: continue
            if i > 0 and flowerbed[i - 1]: continue
            if i < len(flowerbed) - 1 and flowerbed[i + 1]: continue
            ans += 1
            flowerbed[i] = 1
        return ans >= n