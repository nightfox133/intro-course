

#covert 10 - 2
#not working yet

#%%
num = int(input('#: '))
digit = int(input('digit #:'))

binary = []

for i in range(digit, 1, -1):
    if num - (2^i) >= 0:
        num = num - (2^i)
        binary.append(1)
    else:
        if len(binary) > 0:
            binary.append(0)
print(binary)
# %%

