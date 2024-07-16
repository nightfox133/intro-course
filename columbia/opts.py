opts = list(range(1, 11, 1))
print(opts)
high=[]
low=[]
x = 5

hint = input(f'more or less than {x}? ').lower()
if hint == 'more':
    low.append(x)
if hint == 'less':
    high.append(x)

def find(list, index):
    list.sort()
    return list[index]
find(low, 0)
find(high, -1)
opts = opts[a:b]
print(opts)
