class Stack:
    def __init__(self) -> None:

        self._data = []

    def push(self, item):

        self._data.push(item)

    def pop(self):

        return self._data.pop()

    def top(self):

        return self._data.top()

    def is_empty(self):

        return len(self._data) == 0


def readInFix():

    operands = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    operators = ['*', '+', '-', '/', '(', ')']
    arit_input = str(input("Skriv in infix: "))
    arit_list = arit_input.split(', ')

    return arit_list


def infixToPostfix(i_array):
    operators = ['*', '+', '-', '/', '(', ')']

    stack = Stack()
    output = []

    for i in range(len(i_array)):
        current_symbol = i_array[i]

        if current_symbol.isdigit(): 
            output.append(current_symbol)
        elif current_symbol == '(':
            stack.push(current_symbol)
        elif current_symbol == ')':
            while not stack.is_empty() and stack.top() != '(':
                output.append(stack.top())
                stack.pop()
            stack.pop() 
        elif current_symbol in operators: 
            while (
                not stack.is_empty()
                and (p(stack.top()) > p(current_symbol) or (p(stack.top()) == p(current_symbol) and stack.top() != '('))
            ):
                output.append(stack.top())
                stack.pop()
            stack.push(current_symbol)

    while not stack.is_empty():
        output.append(stack.top())
        stack.pop()
    print("Output: ",output)

    return output


def p(operator):
    if operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return 0

def evalPostfix(p_array):

    epStack = Stack()
    results = []

    operands = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    operators = ['*', '+', '-', '/', '(', ')']

    i = 1
    for i in range(len(p_array)): #kanske +1?
        if i in operands:
            epStack.push(i)
        elif i in valid_operators:
            operand2 = epStack.pop()
            operand1 = epStack.pop()

            result = performOperation(operand1, operand2, i)
            epStack.push(result)

    if not epStack.is_empty():
        results.append(epStack.pop())

    return results


def performOperation(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        if operand2 == 0:
            print("Knasigt! Division med noll ej tillåtet.")
            return 0
        else:
            return operand1 / operand2

def main():
    infix_list = readInFix()
    postfix_notation = infixToPostfix(infix_list)
    result = evalPostfix(postfix_notation)
    print("Postfixnotation:", postfix_notation)
    print("Resultat:", result)


if __name__ == "__main__":
    main()
