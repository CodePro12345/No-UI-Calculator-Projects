mode = 'add123'
eq_ans = 0
while True:
    num1 = input()
    if num1 == 'add123' or num1 == 'mul123':
        mode = num1
    elif num1 == 'info':
        print('No UI Calculator add123 mul123 Standalone Version 1.0 Made by Ethan Liu')
    elif num1 == 'help' or num1 == '?':
        print('Entering add123 into the termainal will enable the termainal to do problems like 1 + 2 + 3 + 4 + 5 faster. Entering mul123 into the termainal will enable the termainal to do problems like 1 * 2 * 3 * 4 * 5 f0aster.')
    elif mode == 'add123' or mode == 'mul123':
        num1 = int(num1)
        if mode == 'add123':
            for i in range(num1 + 1):
                eq_ans += i
        elif mode == 'mul123':
            eq_ans = 1
            for i in range(num1):
                eq_ans *= i + 1
        print(eq_ans)