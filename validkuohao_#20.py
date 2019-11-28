# -*- coding: utf-8 -*-
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
有效字符串需满足：
	左括号必须用相同类型的右括号闭合。
	左括号必须以正确的顺序闭合。"([)]" --> False; "{[]}"--> True
注意空字符串可被认为是有效字符串。
可以首先排除的情况： 字符串为奇数、字符串开头是 ')', '}', ']'
"""
class Solution:

    def isValid(self, s):
        # 执行用时 48ms，内存消耗 13.7MB
        d = {'(':')', '{':'}', '[':']'}
        l = [None]
        if len(s) % 2 == 1:
            return False
        if len(s) == 0:
            return True
        for i in s:
            if i in d:
                l.append(i)
            elif l[-1] in d and i == d[l[-1]]:
                l.pop()
        return len(l) == 1

if __name__ == '__main__':
    s = Solution()
    print(s.isValid(']['))