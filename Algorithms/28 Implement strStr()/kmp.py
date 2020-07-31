class Solution:
    def strStr(self, hayback: str, needle: str) -> int:
        if needle == "":
            return 0
        next = self.getNext(needle)
        i, n, j, m = 0, len(hayback), 0, len(needle)
        while i < n and j < m:
            while j > 0 and hayback[i] != needle[j]:
                j = next[j]
            if hayback[i] == needle[j]:
                j += 1
            i += 1
            if j == m:
                return i - j
        return -1

    def getNext(self, needle):
        i, j, l = 2, 0, len(needle)
        next = [0] * l
        while i < l:
            while j > 0 and needle[i-1] != needle[j]:
                j = next[j]
            if needle[i-1] == needle[j]:
                j += 1
            next[i] = j
            i += 1
        return next
