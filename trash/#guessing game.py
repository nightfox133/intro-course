#guessing game

def p1_intro():
    print('welcome to guess a number')
    print('think of an intiger 0 to 100')
    print

def check(input1, input2):
    global run
    if input1 == 'quit' or input2== 'quit':
        run = False
opts = list(range(0, 101, 1))
guess = 50
run = True
while run:
    print(f'is your number {guess}: ')
    ans = input('y or n: ').lower()
    if ans == 'y':
        break
    hint = input('more or less? ').lower()
    if hint == 'more':

    
    
    check(ans, hint)




print(f'correct, it was {guess}!')
print('end')