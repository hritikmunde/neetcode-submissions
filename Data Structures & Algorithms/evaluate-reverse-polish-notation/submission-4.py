class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ("+", "-", "*", "/")
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in operators:
                para1 = stack.pop()
                para2 = stack.pop()
                if tokens[i] == "+":
                    expression = para2 + para1
                    stack.append(expression)
                if tokens[i] == "-":
                    expression = para2 - para1
                    stack.append(expression)
                if tokens[i] == "*":
                    expression = para2 * para1
                    stack.append(expression)
                if tokens[i] == "/":
                    expression = int(para2 / para1)
                    stack.append(expression)
            else:
                stack.append(int(tokens[i]))
        return stack[-1]