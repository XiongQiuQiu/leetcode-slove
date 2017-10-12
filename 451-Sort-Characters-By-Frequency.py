class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(k * i for k, i in collections.Counter(s).most_common())
