name = 'Marco Roseberg'
age = 15
height_meters =1.8034 #5'4

def math(a, b):
    print(a+b)
    print(a*b)
    print(b/a)
math(age, height_meters)

intro = (f'{name} {age}'); print(intro)
print (intro.swapcase())

hobbies = ['piano', 'fencing', 'running']; print(hobbies)
hobbies.append('binary circuits'); hobbies.pop(0)
hobbies.sort(); print(hobbies)

# %%
my_dict = {
    'name': name,
    'age': age,
    'hobbys': hobbies,
    'height': height_meters,
}
# %%

#step 10
print(my_dict)
my_dict['color'] = 'purple'
my_dict.pop('height')
print(my_dict['hobbys'])
my_dict['age'] += 1

#final
print(f'\n{my_dict}')
