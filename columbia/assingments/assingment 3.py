#%%
def is_palindrone(string): #3.1
    if string == string[::-1]:
        return True
    else:
        return False
#%%
class Rect: #3.2
    def __init__(self, l ,w ):
        calc = {}
        self.area = l*w
        self.perimeter = 2*(l+w)
my_rect = Rect(
    l = 4,
    w = 5
)
#%%
phrase = ['the', 'fox', 'jumped', 'over', 'the', 'lazy', 'dog']

def count_words(list):  #3.3
    words = []
    for i in range(len(list)):
        if list[i] not in words:
            words.append(list[i])
    dict = {}
    for i in range(len(words)):
        t = list.count(words[i])
        dict[words[i]] = t
    return dict
print(count_words(phrase))
# %%
