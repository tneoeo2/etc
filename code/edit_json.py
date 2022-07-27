#%%
import json
from webbrowser import get
from FileLoader import Loader
#%%
##! 중복된파일 이름 찾기
from iteration_utilities import duplicates
from iteration_utilities import unique_everseen



def listDups(listNums):
  return list(unique_everseen(duplicates(listNums)))

# %%
"""
json 삭제 기능    
파일이름 입력 => images에서 해당 파일이름의 이미지 id 찾기 (1)
=>anno에서 찾은 id와 일치하는 image_id 파일 찾기 (2)

(1)과 (2) 삭제처리

"""
##? dict_keys(['id', 'width', 'height', 'file_name', 'type'])

##? key1: value 값을 가진 데이터를 찾고 해당 데이터의 key2의 value를 반환하는 함수
def get_values(data,  value, key1, key2, opt=False):     #data:json데이터 value : 검색할 대상, key1: 검색할 대상이 속한 Key값, key2: return받을 value의 key
  cnt = len(data)
  r_all = []
  r_value = []
  r_cnt = []
  for i in range(cnt):
    j_data = data[i]
    if j_data[key1] == value:
          r_value.append(j_data[key2])
          r_all.append(j_data)
          r_cnt.append(i)
          if opt:
                break
          
          
  print("찾은 value 값: ", r_value, end='\t')
  print("r_cnt : ", r_cnt)
          
    
  return r_value, r_cnt, r_all


def get_idx(idx:str): #str으로 반환된 인덱스 변환
    r_idx = int(idx)-1
    
    return r_idx

##get_values(w_image, 'FFF2F34A08347075F55E72B240EFE691.jpg', 'file_name', 'id')    ##?file_name으로 'id'값 찾기

#%%
PATH = "S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\"
file_name = "textinthewild_data_info.json"
#%%
ld = Loader(PATH)

"""
dict_keys(['info', 'images', 'annotations', 'licenses'])    
"""

wild_data = ld.read_json(PATH+file_name)

w_info = wild_data['info']
w_image = wild_data['images']  
w_anno = wild_data['annotations']
w_licenses = wild_data['licenses']


#%%
"""
1.images의 file_name으로 해당 이미지의 id값 찾기
2. anno에서 images["id"]와 일치하는 annotations["images_id"] 찾기  ==> data index는 images['id'] -1 이다!
3. (1)과 (2) 삭제
"""
 
double_images = ['417C79B4528607B795178AC2836E1EEF.jpg', 'EB862D328745738A1072A0E28F2E444E.jpg',
 'E33A9B660BDF41038F18A0E7C1BA3EB2.jpg', 'FDE78B0B9ACEBEFD9C27E24DE801735C.jpg', 
'AF857F4974FC03E909E7D46BF62FC3BF.jpg', '4FAC6E7274569FBD28EB3F490B8B424D.jpg', 
'BA9EEE2326B1B80DF796D33D8A7AF8C3.jpg', 'CC300D2C382F6C2B8182FC6A797BF376.jpg', 
'8EBD02D972108A457C158C8E97C1B00B.jpg', 'C3DB0CAB3968510DE5FFCDEF63287939.jpg',
 '48FC828EB17E3F30584AC8A2F3976B48.jpg']    

only_json = ['FFF2F34A08347075F55E72B240EFE691.jpg','FFF046F2AC18C145BF35BD919E817495.jpg',       ###json에만 존재하는 데이터 -- ##!삭제조치
'FFF22117C8512468492A7BBD7C2CA974.jpg', '00C6E318A22BA1BC698B28B9C6ADAB1E.jpg',
'FFFA896433BBB137E3F88FCEBE949743.jpg','FFF4A7F84FD8A161E159D75ABCDCBDF5.jpg',
'FFE30230D754CE6EA0BD27815D7C8998.jpg','FFA8992BF815BD1439B7E27372526D0E.jpg',
 '0DA4D79F6F81127FA387A246945309C3.jpg','FFF9F9C2D8265F04618C1ABC8CC02D19.jpg',
 'FFF604FD8DBF64630C2B56971A61378F.jpg','FFF3CF9F5CC7A94CD4C07D3EA80030A3.jpg',
 'FFF325D713B9A296248E6E9A4DBC575D.jpg','FFEE472370F6E6F6F541B74F04F4FA95.jpg', 
 'FFE2E6D3E2E12FE27F96058A11369889.jpg','FF98C673E6297DBB2EDBAF7C3C7CA347.jpg', 'FFF471B835BAB373967416776631355E.jpg',
 'FFFDF553CDCE3F6BD3C7DF3166F938EA.jpg','FFFB197061A332FBD6A4B33805F43229.jpg','00A28AF8F44D2F5C04056244C6CEDC93.jpg',
 'FFFD72239E6A987D21A16CA865B040F5.jpg','FFFD68F9E05DA8B0E003E358AD476F7D.jpg','FFFAB658D5CAE531A532EC4C18D36551.jpg',
 'FFFA1C446ADF8C79FAFDA527F538EE46.jpg','FFFBE2212C8AF93D7BC2CB8B64B97852.jpg','FFF44BF74B9C978BC294F4948210B483.jpg',
 'FFFF310024B02D1BBA4136CD74773CD6.jpg','FFB18DA5B141187EFDDB50E986A10F0B.jpg','FFF4BCD91663E874D27A50DA6EB9BEF0.jpg',
 'FFF1C466CE74C3B1B58CB0D3F4C5AEF0.jpg','FFEDB792695A930AE13700AA7694056E.jpg','FFE93EA0A2409FA53EC7E7E9E99F8B0C.jpg',
 'FFF9956F572FB8CAF847BA5CA742CEDC.jpg','FFF964E893793720594619431BAFB727.jpg','FFEEE474568A300C6CEAAE11D5D7FE6A.jpg',
 'FFF3C5BD1309A5FBF4602330E9C71573.jpg','FFBDF4AAA37B828E733E58C61A119AE1.jpg','FFAFD88FC17ED0FC3B2C1F10BF5DDF37.jpg',
 'FFB7BFF84BEAE337CB58C577A75E4DFC.jpg','FFFF54E232C4A11B8FEF4A7BF04CBE8B.jpg','FFEDF5CACDB9BEF0AA5FAC6C2D06AC77.jpg',
 'FFE5F597C7B294F8253E1C04558C33B1.jpg','FFE40FA14B3B3F5D940DF30DF6E91B61.jpg','FFF00BBB62A14535FB6237B305C8A95C.jpg']   


##images에서 탐색
nm_key = 'file_name'
id_key = 'id'

image_id_list = []   #원하는 file_name을 가진 데이터의 인덱스 리스트
image_idx_list = []
image_all_list = []

for i in range(len(only_json)):
  image_id, id_cnt, img_all = get_values(w_image, only_json[i], nm_key, id_key)
  image_id_list.extend(image_id)
  image_idx_list.extend(id_cnt)
  image_all_list.extend(img_all)

#%%
nm_key = 'file_name'
id_key = 'id'

double_id_list = []   #원하는 file_name을 가진 데이터의 인덱스 리스트
double_idx_list = []
double_all_list = []

for i in range(len(double_images)):
  double_id, id_cnt, double_all = get_values(w_image, double_images[i], nm_key, id_key, opt=True)
  double_id_list.extend(double_id)
  double_idx_list.extend(id_cnt)
  double_all_list.extend(double_all)
#%%
image_id_list.extend(double_id_list)
image_idx_list.extend(double_idx_list)
image_all_list.extend(double_all_list)

print("--------------------파일 개수 확인--------------------")
print(f"image_id_list : {len(image_id_list)}, image_idx_list: {len(image_idx_list)}, image_all_list: {len(image_all_list)}")

#%%
##anno에서 탐색
anno_key = 'image_id'
t_key = 'id'

r_anno_id_list = []
r_anno_idx_list = []
r_anno_all_list = []
for i in range(len(image_id_list)):
  anno_value = image_id_list[i]
  r_id, r_anno_cnt, anno_all = get_values(w_anno, anno_value, anno_key, t_key)
  r_anno_id_list.append(r_id)    
  r_anno_idx_list.append(r_anno_cnt)    
  r_anno_all_list.append(anno_all)    
#%%

print("--------------------파일 개수 확인--------------------")
print(f"r_anno_id_list : {len(r_anno_id_list)}, r_anno_idx_list: {len(r_anno_idx_list)}, r_anno_all_list: {len(r_anno_all_list)}")

#%%
def delete_idx(images_data, anno_data, image_all, anno_all):   #json데이터에서 해당 데이터 삭제
      r_image = images_data.copy()
      r_anno = anno_data.copy()
      

      for i in r_image:
          print("r_image 탐색중----: ", i)
          for j in image_all_list:
            if i == j :
              r_image.remove(j)          
              # print(j, "----삭제")
      print("images 삭제완료")
      for i in r_anno:
          print("r_anno 탐색중----: ", i)
          for sigle_anno in r_anno_all_list:
                  for j in sigle_anno:
                        if i == j :
                              r_anno.remove(j)
                              # print(j, "----삭제")
      print("anno 삭제완료")
                              
      return r_image, r_anno             
      
n_image, n_anno = delete_idx(w_image, w_anno,image_all_list, r_anno_all_list)
print("삭제 완료-----🧨🧨✨")
# %%

w_info  
n_image 
n_anno
w_licenses 

n_wild_data = {'info' : w_info,
               'images' : n_image,
               'annotations' : n_anno,
               'licenses' : w_licenses}


# %%
SAVE_PATH = "S:\\nexin\\AEye\\AI-HUB\\wild\\한국어 글자체 이미지\\04.Text in the wild\\after\\"
file_name = 'textinthewild_data_info.json'
def save_json(data, save_path):
  with open(save_path, 'w') as f:
    json.dump(data, f, indent=4)
    
save_json(n_wild_data, SAVE_PATH+file_name)
print("json 저장 완료-------------:",file_name )
# %%
