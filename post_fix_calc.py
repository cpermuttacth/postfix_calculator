from ArrayStack import ArrayStack

def postfix_calc():
    exp = input('-->')
    dct = {}
    s = ArrayStack()
    while exp != 'done()':
        exp = input('-->')
    
        if '=' not in exp:
            for char in exp:
                if char.isdigit() == True:
                    s.push(char)

                elif char in '*-/+':
                    operand1 = int(s.pop())
                    operand2 = int(s.pop())

                    if char == '+':
                        s.push(operand1 + operand2)
                    elif char == '-':
                        s.push(operand1 + operand2)
                    elif char =='*':
                        s.push(operand1 * operand2)
                    elif char == '/':
                        s.push(operand1 * operand2)
            print(s.top())


        else:
            for char in exp:
                if char.isalpha() == True:
                    dct[char] = stack.top()
                    
            print(char)
                        
                

