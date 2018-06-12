class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, b = eval(a.replace('i', 'j')), eval(b.replace('i', 'j'))
        ans = a * b
        return ''.join([str(int(ans.real)), '+', str(int(ans.imag)), 'i'])