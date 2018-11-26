def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    ans = list(s)
    i, j = 0, len(s) - 1
    while i <= j:
        if ans[i] not in vowel:
            i += 1
        if ans[j] not in vowel:
            j -= 1
        if ans[i] in vowel and ans[j] in vowel:
            ans[i], ans[j] = ans[j], ans[i]
    return ''.join(ans)

reverseVowels(1,"hello")