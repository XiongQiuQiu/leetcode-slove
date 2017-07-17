class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        ones = equation.split('=')[0]
        twos = equation.split('=')[1]
        lx, ln = self.parse(ones)
        rx, rn = self.parse(twos)
        lx -= rx
        rn -= ln
        if lx == 0 and rn == 0: return 'Infinite solutions'
        if lx == 0 and rn != 0: return 'No solution'
        return 'x=' + str(rn / lx)

    def parse(self, st):
        x, n = 0, 0
        sig = ['-', '+', '#']
        si = 0
        st = st + '#'
        for i in range(1, len(st)):
            if st[i] in sig:
                if st[i - 1] == 'x':
                    x += int((st[si:i - 1] if st[si:i - 1] not in sig else st[si:i - 1] + '1') or '1')
                else:
                    n += int(st[si:i] or '1')
                si = i
        return x, n
