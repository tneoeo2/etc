#%%
import json
import os
from FileLoader import Loader




PATH = "S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\"
folderlist = ['after', 'before', 'code', 'wild']
#%%
##* json test
ld = Loader(PATH)

json_file = ld.load_file_type('.json')
print("list 확인---", json_file)
t_json = PATH +json_file[0]

json_data = ld.read_json(t_json, ecd="utf-8")
print("json 읽기 완료.....")
#%%
keys = list(json_data.keys())

json_info = json_data[keys[0]]    
json_imgs = json_data[keys[1]]      #id, width, height, file_name, type   #?list  [ {}, {}, {}] <- 형태 리스트데이터
json_anno = json_data[keys[2]]
json_lics = json_data[keys[3]]




# %%

###? 500개 단위로 데이터 split
def split_data(t_json):   
    s_json = []
    for i in range(len(t_json)//500 +1):
        if (i+1)*500 <len(t_json):
            print(f"split---- {i*500} : {(i+1)*500} ")
            s_json.append(t_json[i*500 : (i+1)*500] )
        else:
            cnt = len(t_json)-(i*500)
            print(f"split---- {i*500} : {i*500+cnt}")
            s_json.append(t_json[i*500 :] )
            
    return s_json
        
#%%
s_json_imgs = split_data(json_imgs)
        
        
#%% 
##? 500개 단위로 파일명 리스트만 뽑아오기;
def get_target_values(t_list:list, key):
    cnt = len(t_list)
    valuelist = []
    
    for i in range(cnt):
        valuelist.append(t_list[i][key])
        
    return valuelist

keyword = "file_name"
list_cnt = len(s_json_imgs)
file_name_list = []          ####! json파일 이름 리스트

for i in range(list_cnt):
    s_file_name_list = get_target_values(s_json_imgs[i], key=keyword)    #파일이름이 담겨있는 리스트(500개씩)
    file_name_list.append(s_file_name_list)
    


#%%
##각 폴더 별 리스트 생성
BOOK_PATH = "S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\01_textinthewild_book_images_new\\book\\"
GOODS_PATH = "S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\01_textinthewild_goods_images_new\\Goods\\"
SIGN_PATH = "S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\01_textinthewild_signboard_images_new\\Singboard\\"
TSIGN_PATH = "S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\01_textinthewild_traffic_sign_images_new\\Traffic_Sign\\" 




booklist = os.listdir(BOOK_PATH)
goodslist = os.listdir(GOODS_PATH)
signlist = os.listdir(SIGN_PATH)
tsignlist = os.listdir(TSIGN_PATH)

#%%
all_image_list = []

all_image_list.extend(booklist)
all_image_list.extend(goodslist)
all_image_list.extend(signlist)
all_image_list.extend(tsignlist)

#%%
print("--------------------파일 개수 확인--------------------")
print(f"books : {len(booklist)}, goods: {len(goodslist)}, sign: {len(signlist)}, tsign: {len(tsignlist)}")


#%% 
##? json <==> folder 파일 비교
"""
    json(500단위)로 각 폴더의 파일 name 비교
    1. json에만 파일이름 존재하고 이미지 파일이 없는 경우
    2. 이미지 파일만 존재하고 json에 데이터 없는경우
    
"""
def compare_AB(list1:list, list2:list):     #list2의 값이 list1에 있는지 비교 (list1이 메인)
    result_list = list1.copy()
    in_cnt = 0
    n_in_cnt = 0
    in_list = []
    n_in_list = []
    for el in list2:
        try:
            # print("존재하는 파일 : ", el)
            result_list.remove(el)
            in_cnt += 1
            # in_list.append(el)
        except:
            n_in_cnt += 1
            # n_in_list.append(el)
            # print("존재하지않는 파일 : ", el)
    print('존재하는 파일 수량 : {}, 존재 X 파일: {}'.format(in_cnt, n_in_cnt))
    
    return result_list, in_list, n_in_list

#%%
####! json에만 존재하는 파일명 구하기
only_json_list = []

cnt = len(file_name_list)

for i in range(cnt):     ####? json에만 존재하는 파일명 추출
    print("-------------{}-------------".format(i))
    rm_book_list, _, _ = compare_AB(file_name_list[i], booklist)
    rm_goods_list, _, _ = compare_AB(rm_book_list, goodslist)
    rm_sign_list, _, _ = compare_AB(rm_goods_list, signlist)
    rm_tsign_list, _, _ = compare_AB(rm_sign_list, tsignlist)
    print(rm_tsign_list)    
    only_json_list.extend(rm_tsign_list)


#%%
##? 리스트 합치기
nm_cnt = len(file_name_list)

all_file_name_list = []
for i in range(nm_cnt):
    all_file_name_list.extend(file_name_list[i])

#%%

##! image만 존재하는 파일명 구하기  : image이름 리스트에서 json이름 리스트 제거해보기 (0개)
s_booklist = split_data(booklist)
s_goodslist = split_data(goodslist)
s_signlist = split_data(signlist)
s_tsignlist = split_data(tsignlist)

print("--------------------파일 개수 확인--------------------")
print(f"books : {len(s_booklist)}, goods: {len(s_goodslist)}, sign: {len(s_signlist)}, tsign: {len(s_tsignlist)}")
#%%

only_book_img_list = []

tcnt = len(s_booklist)
fcnt = len(file_name_list)
ori_cnt = len(json_imgs)

# for i in range(tcnt):     ####? json에만 존재하는 파일명 추출
for j in range(tcnt):     ####! book 모두 있음
    print("=============={}==============".format(j))
    rm_result_list,_, _ = compare_AB(s_booklist[j], all_file_name_list)
    # print(rm_result_list)    
    only_book_img_list.extend(rm_result_list)

#%%    

only_goods_img_list = []

tcnt = len(s_goodslist)
fcnt = len(file_name_list)
ori_cnt = len(json_imgs)
for j in range(tcnt):     ####! book 모두 있음
    print("=============={}==============".format(j))
    rm_result_list,_, _ = compare_AB(s_goodslist[j], all_file_name_list)
    # print(rm_result_list)    
    only_goods_img_list.extend(rm_result_list)

#%%    

only_sign_img_list = []

tcnt = len(s_signlist)
fcnt = len(file_name_list)
ori_cnt = len(json_imgs)
for j in range(tcnt):     ####! book 모두 있음
    print("=============={}==============".format(j))
    rm_result_list,_, _ = compare_AB(s_signlist[j], all_file_name_list)
    # print(rm_result_list)    
    only_sign_img_list.extend(rm_result_list)

#%%        

only_tsign_img_list = []

tcnt = len(s_tsignlist)
fcnt = len(file_name_list)
ori_cnt = len(json_imgs)
for j in range(tcnt):     ####! book 모두 있음
    print("=============={}==============".format(j))
    rm_result_list,_, _ = compare_AB(s_tsignlist[j], all_file_name_list)
    # print(rm_result_list)    
    only_tsign_img_list.extend(rm_result_list)
    

    

#%%
print("--------------------파일 개수 확인--------------------")
print(f"books : {len(only_book_img_list)}, goods: {len(only_goods_img_list)}, sign: {len(only_sign_img_list)}, tsign: {len(only_tsign_img_list)}")
    

    

# %%
###! json 에 중복된 이름이 있나..?
print(f"전체 json_name 수: {len(all_file_name_list)}, set(json_name리스트) : {len(set(all_file_name_list))} ")

##! image에 중복된 이름이 있나?
print(f"전체 image_name 수: {len(all_image_list)}, set(image_name리스트) : {len(set(all_image_list))} ")
# %%
##! 중복된파일 이름 찾기
from iteration_utilities import duplicates
from iteration_utilities import unique_everseen


# listNums = [1,1,2,3,3,4,5,5,5,5,6,8,8]

def listDups(listNums):
  return list(unique_everseen(duplicates(listNums)))

print(listDups(all_file_name_list))
print(listDups(all_image_list))
# %%
