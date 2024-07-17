import random

Names = ['marco', 'zoe', 'raffa', 'laurin',] #name list
Nums = [13, 5, 9, 21,]

def print_list(list):
    for i in range(len(list)):
        print(list[i])
for i in range(1, 11, 1):
    print(i)
print(f'sum = {sum(Nums)}')
for i in range(len(Names)):
    print(f'Hello, {Names[i]}')

#%%
word = 'banana'
word2 = ""
for i in range(len(word) - 1, -1, -1):
    word2 += word[i]
print (word2)



letters = {}
for i in range(len(word)):
    if word[i] not in letters:
        letters[word[i]] = None
x = (list(letters))
#%%
for i in range(len(letters)):
    t = 0
    for k in range(len(word)):
        if x[i] == word[k]:
            t += 1
    letters[x[i]]=t
print(letters)

students = {'jack': 88, 'grace': 93, 'kevin': 54, 'mina': 67}
x = (list(students))
for i in range(len(students)):
    if students[x[i]] >= 60:
        pass
    else:
        students.pop(x[i], students[x[i]])
print(f'\npassed list:\n{students}')

for i in range(1, 11):
    q = 5*i
    print(f'5 x {i} = {q}')
#%%
t = 0
while t < 10:
    t += 1
    print(t)
# %%
inp = input('name: ')
while inp != 'quit':
    print(f'hello, {inp}')
    inp = input('name: ')
# %%

inp = int(input('enter an int 1-10:'))
if inp%2 == 0:
    if inp == 0:
        print('neither')
    else:
        print('even')
else:
    print('odd')
#%%
#import random
nums = []
for i in range(10):
    nums.append(random.randint(1,101))
nums.sort()
print(nums[0], nums[-1])
# %%
fruit_stand = {
    'lychee': 4.99,
    'guava': 11.99,
    'papaya': 4.48,
    'mango': 3.00,
    'persimmon': 8.99,
    'kiwi': 8.98,
}
opt = list(fruit_stand)

pick = input('what would u like? ').lower()
if pick in opt:
    print(f'that will be ${fruit_stand[pick]}.')
else:
    print(f'sorry, we do not have {pick}.')
# %%