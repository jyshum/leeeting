class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # what to keep track of?
        stack = []

        for char in tokens:
            if char == "+":
                # add
                number1 = stack.pop()
                number2 = stack.pop() # pops off the last two numbers
                value = number2 + number1
                stack.append(int(value)) # push result back
            elif char == "-":
                # subtract
                number1 = stack.pop()
                number2 = stack.pop()
                value = number2 - number1
                stack.append(int(value))
            elif char == "*":
                # multiply
                number1 = stack.pop()
                number2 = stack.pop()
                value = number2 * number1
                stack.append(int(value))
            elif char == "/":
                # divide
                number1 = stack.pop()
                number2 = stack.pop()
                value = number2 / number1
                stack.append(int(value))
            else:
                # number
                stack.append(int(char))

        return stack[0]
        # end of the loop, the stack will only have one number left as every new number taken from tokens was squashed into one by being operated with another number in the stack
    

