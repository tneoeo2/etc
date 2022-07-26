#%%
import os
import sys
import json
import numpy as np

class Loader:
    
    def __init__(self, file_path):  
        self.file_path = file_path 
        
    def __str__(self):

        return f"PATH----- {self.file_path}"
    
    def load_file(self):   #하위 파일리스트 가져오기
        
        filelist = os.listdir(self.file_path)
        
        return filelist        
      
    
    def load_file_type(self, type):   #하위 파일리스트 가져오기
        
        filelist = os.listdir(self.file_path)
        filelist = [file for file in filelist if file.endswith(type)]
        
        return filelist        
    
    def read_json(self, t_path, ecd='utf-8'):   #ecd:인코딩 설정
        json_data = ''
        with open(t_path, 'r', encoding=ecd) as f:
            # print(type(f), f)
            json_data = json.load(f)
            
        return json_data
            
            
            
            

#%%%
"""##?Test
PATH = "S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\01_textinthewild_book_images_new\\book\\"
JSON_PATH = "S:\\nexin\\AEye\\AI-HUB\\before\\printed_data_info___.json"


#%%
##* file test
ld = Loader(PATH)
# ld = Loader(PATH, ".jpg")
filelist = ld.load_file(".jpg")

# print(filelist)
len(filelist)

#%%
##* json test
jld = Loader(JSON_PATH)
json_file = jld.read_json(ecd="utf-8")

print(json_file['info'])

"""

##% 
# %%
