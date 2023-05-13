mode = 'add'
num = '2'
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
eq_ans = 0
while True:
    num1 = input()
    if num1 == 'add' or num1 == 'sub' or num1 == 'mul' or num1 == 'div':
        mode = num1 
    if num1 == 'num2':
        num = '2'
    elif num1 == 'num3':
        num = '3'
    elif num1 == 'num4':
        num = '4'
    elif num1 == 'num5':
        num = '5'
    elif num1 == 'info':
        print('No UI Calculator Version 1.0 Made by Ethan Liu')
    if num1 != 'add' and num1 != 'sub' and num1 != 'mul' and num1 != 'div' and num1 != 'num2' and num1 != 'num3' and num1 != 'num4' and num1 != 'num5' and num1 != 'info':
        if num == '2':
            num1 = int(num1)
            num2 = input()
            num2 = int(num2)
        elif num == '3':
            num1 = int(num1)
            num2 = input()  
            num2 = int(num2)
            num3 = input()
            num3 = int(num3)
        elif num == '4':
            num1 = int(num1)
            num2 = input()
            num2 = int(num2)
            num3 = input()
            num3 = int(num3)
            num4 = input()
            num4 = int(num4)
        elif num == '5':
            num1 = int(num1)
            num2 = input()
            num2 = int(num2)
            num3 = input()
            num3 = int(num3)
            num4 = input()
            num4 = int(num4)
            num5 = input()
            num5 = int(num5)
        if mode == 'add':
            eq_ans = num1 + num2 + num3 + num4 + num5
        elif mode == 'sub':
            eq_ans = num1 - num2 - num3 - num4 - num5
        if num == '2':
            if mode == 'mul':
                eq_ans = num1 * num2
            elif mode == 'div':
                eq_ans = num1 / num2 
        if num == '3':
            if mode == 'mul':
                eq_ans = num1 * num2 * num3
            elif mode == 'div':
                eq_ans = num1 / num2 / num3
        if num == '4':
            if mode == 'mul':
                eq_ans = num1 * num2 * num3 * num4
            elif mode == 'div':
                eq_ans = num1 / num2 / num3 / num4
        if num == '4':
            if mode == 'mul':
                eq_ans = num1 * num2 * num3 * num4
            elif mode == 'div':
                eq_ans = num1 / num2 / num3 / num4             
        eq_ans = str(eq_ans)
        print(eq_ans)