"""
1.json 파일 읽어오기
2. type 별로 데이터 나누기 
    ex: {'book' : ['파일 이름', '파일이름'...]}     형식
    
3. type이름에 맞춰서 폴더 생성 (book, sign....)
4. dict에서 폴더이름을 key 로 갖는 value값의 파일들을 해당 폴더로 이동(용량크니까 이동...)
    
"""
#%%
import shutil
import os
import sys
from FileLoader import Loader


JSON_PATH = "S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\after\\textinthewild_data_info.json"
DIR_PATH = "S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\after\\"
dir_names = ['book', 'sign', 'product', 'traffic sign']


#*한번만 실행
# for i in dir_names:
#     os.makedirs(DIR_PATH + i, exist_ok=True)
#%%
##* json test
ld = Loader(JSON_PATH)

wild_data = ld.read_json(JSON_PATH)

w_info = wild_data['info']
w_image = wild_data['images']  
w_anno = wild_data['annotations']
w_licenses = wild_data['licenses']

#%%
w_cnt = len(w_image)

type_dict = {
    'book' : [],
    'sign' : [],
    'product' : [],
    'traffic sign' : []
}

for i in range(w_cnt):
    if w_image[i]['type'] == 'book':
        type_dict['book'].append(w_image[i]['file_name'])
    elif w_image[i]['type'] == 'sign':
        type_dict['sign'].append(w_image[i]['file_name'])
    elif w_image[i]['type'] == 'product':
        type_dict['product'].append(w_image[i]['file_name'])
    elif w_image[i]['type'] == 'traffic sign':
        type_dict['traffic sign'].append(w_image[i]['file_name'])
# %%
#* 파일 이동
product_src = 'S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\01_textinthewild_goods_images_new\\Goods\\'
book_src = 'S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\01_textinthewild_book_images_new\\book\\'
sign_src = 'S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\01_textinthewild_signboard_images_new\\Singboard\\'
tsign_src = 'S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\01_textinthewild_traffic_sign_images_new\\Traffic_Sign\\'

dst_dir = "S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\all\\"
#파일 한 곳에 몰아넣기

books = os.listdir(book_src)
signs = os.listdir(sign_src)
products = os.listdir(product_src)
tsigns = os.listdir(tsign_src)


#%%
src_path_list = [book_src, sign_src, product_src, tsign_src]
src_list = [books, signs, products, tsigns]

for idx, src in enumerate(src_list):
    print(src_path_list[idx])
    # print(src)
    for s in src:
        try:
            shutil.move(src_path_list[idx] + s, dst_dir)
        except Exception as e:
            print(e)
# %%
book_dst = 'S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\after\\book\\'
sign_dst = 'S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\after\\sign\\'
product_dst = 'S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\after\\product\\'
tsign_dst = 'S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\after\\traffic sign\\'

for i in type_dict['book']:
    try:
        shutil.move(dst_dir + i, book_dst)
    except Exception as e:
        pass
print('book END')
    
for i in type_dict['sign']:
    try:
        shutil.move(dst_dir + i, sign_dst)
    except Exception as e:
        pass
print('sign END')
    
for i in type_dict['product']:
    try:
        shutil.move(dst_dir + i, product_dst)
    except Exception as e:
        pass
print('product END')
    
for i in type_dict['traffic sign']:
    try:
        shutil.move(dst_dir + i, tsign_dst)
    except Exception as e:
        pass
print('traffic sign END')

# %%
