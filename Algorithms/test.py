def permuteUnique(nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            for i in xrange(len(l)+1):
                new_ans.append(l[:i]+[n]+l[i:])
                if i<len(l) and l[i]==n:
                    break              #handles duplication
        ans = new_ans
    return ans
permuteUnique([2,1,1,3,4,5,6])