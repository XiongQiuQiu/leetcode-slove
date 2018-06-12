class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        nows = ans = 0
        for i in timeSeries:
            ans += min(duration, i + duration - nows)
            nows = i + duration
        return ans
