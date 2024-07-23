#%%
import glob
import os
from pathlib import Path
import time 

path = r'C:\Users\marco\.vscode\python\projects\columbia\assingments\sorted'

lookup = {
    'PDFs': ['pdf'],
    'MS': ['docx','doc','pptx','ppt','xls','xlsx'],
    'Audio': ['wav','mp3','flac','aiff'],
    'PDFs': ['png','jpeg','tiff','gif'],
    'JSON': ['json'],
    'PY': ['py']
}

frequency = 60 #seconds

os.chdir(path)

lookup_flip = {}
for k in lookup.keys():
    for v in lookup[k]:
        lookup_flip[v]=k
print (lookup_flip)

print(f'__init__ for time in {frequency}')
#%%
while True:
    files = glob.glob(r'*')
    for f in files:
        file = Path(f)
        if file.is_dir():
            continue
        ext = file.suffix.replace(".", "")

        if ext in lookup_flip:
            new_folder = lookup_flip[ext]

            if not os.path.exists(new_folder):
                os.mkdir(new_folder)
            
            os.rename(f, f'{new_folder}/{f}')
    curr = time.time()
    print(f'Sorted at {curr}')
    time.sleep(frequency)
        

        
