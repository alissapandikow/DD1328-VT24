class Stack:
    def __init__(self) -> None:
        self._data = []

    def push(self, item):
        self._data.push(item)

    def pop(self):
        if not self.is_empty():
            return self._data.pop()
        else:
            print("Error: pop")
            return None

    def top(self):
        if not self.is_empty():
            return self._data[-1]
        else:
            print("Error: top")
            return None

    def is_empty(self):
        return len(self._data) == 0


def readInFix():
    valid_operands = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    valid_operators = ['*', '+', '-', '/', '(', ')']

    arit_input = input("Skriv infixuttryck: ")

    for char in arit_input:
        if char not in valid_operands and char not in valid_operators:
            print("Du måste ange ett uttryck med godkända operander och operatorer.")
            return readInFix()

    arit_list = arit_input.split()
    return arit_list


def infixToPostfix(i_array):
    valid_operands = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    valid_operators = ['*', '+', '-', '/', '(', ')']

    postfix_output = []
    stack = Stack()

    for char in i_array:
        if char in valid_operands:
            print("H")
            postfix_output.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while stack.top() != '(':
                postfix_output.append(stack.top())
                stack.pop()
            stack.pop()
        elif char in valid_operators:
            t = stack.top()
            while t != '('or p(t) < p(char) or stack.top() == '(':
                postfix_output.append(stack.top())
                stack.pop()
            stack.push(char)

    while stack.top() is not None:
        postfix_output.append(stack.top())
        stack.pop()

    return postfix_output



def evalPostfix(p_array):
    valid_operands = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    valid_operators = ['*', '+', '-', '/', '(', ')']

    epStack = Stack()
    results = []

    for V_i in p_array:
        if V_i in valid_operands:
            results.append(V_i)
        elif V_i in valid_operators:
            operand2 = epStack.pop()
            operand1 = epStack.pop()

            result = performOperation(operand1, operand2, V_i)
            epStack.push(result)

    return results


def p(operator):
    if operator == '*' or operator == '/':
        return 2
    elif operator == '+' or operator == '-':
        return 1
    else:
        return 0


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
    print()
    main()


if __name__ == "__main__":
    main()
