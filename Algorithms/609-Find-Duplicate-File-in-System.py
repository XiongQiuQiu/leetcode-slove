class Solution(object):
    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for x in paths:
            path = x.split()
            for s in path[1:]:
                content = s.split('(')[1]
                key = path[0] + '/' + s.split('(')[0]
                if d.get(content):
                    d[content].append(key)
                else:
                    d[content] = [key]
        return [d[x] for x in d]
