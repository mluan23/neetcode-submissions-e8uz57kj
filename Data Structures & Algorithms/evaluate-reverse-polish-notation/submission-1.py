class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # ok so you gotta iterate thru everything
        # it always will be 2 things to start, unless 1
        # if size 1 just return the thing
        # else you will use a stack
        # ok just pop until stack is empty essentially
        # or use a queue?
        # so i think depends on sub and div
        # do you really even need a stack?
        # hmm O(n) space? why tho
        # cant we just use a first and second num variable?
        # hmm lets try it
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        res = -math.inf
        # there should always be >=2 things to remove
        for i in range(len(tokens)):
            if tokens[i] in "+-/*":
                first = int(stack.pop())
                second = int(stack.pop())
                if res != -math.inf:
                    first, second = second, first
                res = self.evaluate(second, first, tokens[i])
                stack.append(res)
            else:
                stack.append(tokens[i])
        return res
        # first = int(tokens[0])
        # second = int(tokens[1])
        # op = tokens[2]

        # res = self.evaluate(first, second, op)

        # for i in range(3, len(tokens)):
        #     # its a number
        #     first = res
        #     if tokens[i] not in "+-/*":
        #         second = int(tokens[i])
        #     else:
        #         res = self.evaluate(first, second, tokens[i])
        # return res

    def evaluate(self, first, second,op):
        if op == "+":
            return first + second
        if op == "-":
            return first - second
        if op == "*":
            return first * second
        if op == "/":
            return first // second