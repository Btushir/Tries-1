"""
Todo: Solve using Trie
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # if string empty
        if not strs:
            return ""

        # the first string is the prefix
        prefix = strs[0]

        # start from second string and
        for idx in range(1, len(strs)):  # O(n)
            curr = strs[idx]
            i, j = 0, 0

            # compare the prefix and curr string
            while i < len(prefix) and j < len(curr):  # O(number of char in string)
                if prefix[i] == curr[j]:
                    i += 1
                    j += 1
                else:
                    break

            # the prefix can not updated in the else part because what if
            # lenght of string is less than prefix the while loop
            prefix = prefix[:i]

        return prefix



