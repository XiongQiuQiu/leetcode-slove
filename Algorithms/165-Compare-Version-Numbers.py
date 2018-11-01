'''

Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the . character.
The . character does not represent a decimal point and is used to separate number sequences.
For instance, 2.5 is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Example 2:

Input: version1 = "1.0.1", version2 = "1"
Output: 1
Example 3:

Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
'''
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1_list,v2_list = version1.split('.'),version2.split('.')
        if len(v2_list) >len(v1_list):v1_list += ['0' for i in range(len(v2_list) -len(v1_list))]
        if len(v1_list) >len(v2_list):v2_list += ['0' for i in range(len(v1_list) -len(v2_list))]
        for v1,v2 in zip(v1_list,v2_list):
            if int(v1) > int(v2): return 1
            elif int(v1) < int(v2): return -1
            else: continue
        return 0