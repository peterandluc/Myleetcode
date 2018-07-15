class Solution:
    """
    O(n)
    """
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start, rm = 0, 0
        l = len(s)
        for i in range(l):
            if s[i] in s[start:i]:
                rm = max(rm, i - start)
                tmp = s[start:i].find(s[i])
                start = start + tmp + 1
        return max(rm, l-start)
