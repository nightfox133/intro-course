import math

Names = ['marco', 'zoe', 'raffa', 'laurin',] #name list
Nums = [13, 5, 9, 21,]

def print_list(list):
    for i in range(len(list)):
        print(list[i])

for i in range(1, 11, 1):
    print(i)

for i in range(len(Names)):
    print(f'Hello, {Names[i]}')

print(f'sum = {sum(Nums)}')

word = 'python'
