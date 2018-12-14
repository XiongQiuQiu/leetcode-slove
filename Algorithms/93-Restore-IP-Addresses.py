'''Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]'''


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.helper(ans, s, 0, '')
        return ans

    def helper(self, ans, s, index, path):
        if index == 4:
            if not s:
                ans.append(path[:-1])
            return
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:
                    self.helper(ans, s[i:], index + 1, path + s[:i] + '.')
                elif i == 2 and s[0] != '0':
                    self.helper(ans, s[i:], index + 1, path + s[:i] + '.')
                elif i == 3 and s[0] != '0' and int(s[:i]) <= 255:
                    self.helper(ans, s[i:], index + 1, path + s[:i] + '.')
