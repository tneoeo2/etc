#%%
import json
from FileLoader import Loader
#%%
##! 중복된파일 이름 찾기
from iteration_utilities import duplicates
from iteration_utilities import unique_everseen



def listDups(listNums):
  return list(unique_everseen(duplicates(listNums)))
#%%

PATH = "S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\after\\"
file_name = "textinthewild_data_info.json"
#%%

ld = Loader(PATH)

"""
dict_keys(['info', 'images', 'annotations', 'licenses'])    
"""

wild_data = ld.read_json(PATH+file_name)

w_image = wild_data['images']  
w_anno = wild_data['annotations']

# %%
"""
json 삭제 기능    
파일이름 입력 => images에서 해당 파일이름의 이미지 id 찾기 (1)
=>anno에서 찾은 id와 일치하는 image_id 파일 찾기 (2)

(1)과 (2) 삭제처리

"""
