'''Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''


class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        def fun(res, c):
            if c != '#':
                res.append(c)
            elif res:
                res.pop()
            return res

        return reduce(fun, S, []) == reduce(fun, T, [])


class Solution:
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        si, ti = len(S) - 1, len(T) - 1
        count_s = count_t = 0

        while si >= 0 or ti >= 0:
            # si stops at non-deleted character in S or -1
            while si >= 0:
                if S[si] == '#':
                    count_s += 1
                    si -= 1
                elif S[si] != '#' and count_s > 0:
                    count_s -= 1
                    si -= 1
                else:
                    break

            # ti stops at non-deleted character in T or -1
            while ti >= 0:
                if T[ti] == '#':
                    count_t += 1
                    ti -= 1
                elif T[ti] != '#' and count_t > 0:
                    count_t -= 1
                    ti -= 1
                else:
                    break

            if (ti < 0 and si >= 0) or (si < 0 and ti >= 0):
                # eg. S = "a#", T = "a"
                return False
            if (ti >= 0 and si >= 0) and S[si] != T[ti]:
                return False

            si -= 1
            ti -= 1
        return True