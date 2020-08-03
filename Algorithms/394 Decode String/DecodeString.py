class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        tmpStr = ""
        tmpNum = ""
        for i in s:
            if i == "]":
                c = stack.pop()
                while c != "[":
                    tmpStr= c + tmpStr
                    c = stack.pop()
                while len(stack) > 0 and "0" <= stack[-1] <= "9":
                    tmpNum = stack.pop() + tmpNum
                tmpStr = tmpStr * int(tmpNum)
                stack.append(tmpStr)
                tmpStr = ""
                tmpNum = ""
            else:
                stack.append(i)
        ans = ""
        for i in stack:
            ans += i
        return ans


inStr = "abc10[cd]xyz"
sol = Solution()
print(sol.decodeString(inStr))
