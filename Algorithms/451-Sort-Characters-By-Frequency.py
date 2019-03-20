class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ''.join(k * i for k, i in collections.Counter(s).most_common())

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        dmap = {}
        for i in s:
            dmap[i] = dmap.setdefault(i,0)+1
        return ''.join(i[0]*s.count(i[0]) for i in sorted(dmap.items(),key=lambda x: x[1])[::-1])