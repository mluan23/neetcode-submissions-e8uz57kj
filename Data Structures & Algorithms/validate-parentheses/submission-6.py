class Solution:
    def isValid(self, s: str) -> bool:
        lst = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                lst.append(c)
            else:
                if len(lst) == 0:
                    return False
                elem = lst.pop(len(lst)-1) 
                if c == ')' and elem != '(':
                    return False
                if c == '}' and elem != '{':
                    return False
                if c == ']' and elem != '[':
                    return False
        return len(lst) == 0