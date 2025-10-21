# 20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        item = []
        for i in s:
            if i in '({[':
                item.append(i)
            else:
                if not item:
                    return False

                top = item.pop()

                if i == ')' and top != "(":
                    return False
                if i == '}' and top != "{":
                    return False
                if i == ']' and top != "[":
                    return False

        return len(item) == 0 

        