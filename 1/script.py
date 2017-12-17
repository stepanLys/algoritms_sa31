# -*- coding: utf-8 -*-
import toRPN
import math

operators = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
    '^': lambda a, b: a** b,
}

def polish_eval(expression):
    elements = expression.split()
    stack = []
    while elements:
        e = elements.pop(0)
        if e in operators:
            b = stack.pop()
            a = stack.pop()
            stack.append(operators[e](a, b))
        else:
            stack.append(float(e))
    return stack[0]

def main():
    # print(polish_eval('5 4 ^'))
    '''
    input = "11 + 2".split(" ")
    output = infixToRPN(input)
    print(output)
    print(' '.join(output))
    '''

    infix = input('Введіть вираз:\t').split(' ')
    print(toRPN.infixToRPN(infix))
    RPN = ' '.join(toRPN.infixToRPN(infix))


    print('RPN:\t' + RPN)

    print('Результат:\t' + str(polish_eval(RPN)))

if __name__ == '__main__':
    main()