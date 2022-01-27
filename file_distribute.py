#%%
import os
import time
import datetime
import shutil

origin_path ="C:\\Users\\tneoe\\Desktop\\파이널\\데이터셋 테스트용\\finalDataset\\trainset"
origin_file = '구두'
i = 1
target_path = "target_{}".format(i)


def dir_load(path):
    dir_list = os.listdir(path)
    print("하위 디렉토리 및 파일 확인 : ",dir_list)
    return dir_list

def _copyfileobj_patched(fsrc, fdst, length=16*1024*1024):  #shutil.copy 속도 향상용(대략 2배정도 빨라지는듯..?) 
    """Patches shutil copyfileobj method to hugely improve copy speed""" 
    while 1:
        buf = fsrc.read(length)
        if not buf:
            break 
        fdst.write(buf)
shutil.copyfileobj = _copyfileobj_patched # shutil 의 copyfileobj 대신 _copyfileobj_patched 이 호출됨

def create_dir(origin_path, target_path):  #path1 상위폴더 /path1및이 하위 폴더리스트를 path2경로에 생성
   dir_list = dir_load(origin_path)
   os.makedirs(target_path, exist_ok=True) #target폴더 생성
   for dir in dir_list:
        dir_path = os.path.join(target_path, dir)
        os.makedirs(dir_path, exist_ok=True) #exist_ok=True : 기존 디렉토리가 없을 경우에만 생성
   create_file(origin_path,target_path, dir_list, 30)  #폴더별로 파일 30개씩 복사
   print("------copy_dir 완료------") 

def create_file(default_path,target,path_list, num=1):
    start = time.time()
    for pidx, path in enumerate(path_list):
            dir_path = os.path.join(default_path, path)
            dir_list = os.listdir(dir_path)   #파일이름 리스트
            target_path = os.path.join(target, path)
            for idx, file in enumerate(dir_list):
                # print("file_list : ",dir_list[0:10])
                if idx < num*i :  #num만큼 반복
                    shutil.copy(os.path.join(dir_path, file), os.path.join(target_path, file))
                    # i+1
                    # target_path = "target_{}".format(i)
                    # os.makedirs(dir_path, exist_ok=True)
                    
    end = time.time()-start   
    print("걸린시간 : ", datetime.timedelta(seconds=end))    
    print("------create_file 끝------")   
        

create_dir(origin_path, target_path)




# dir_load('C:\\\\Users\\\\tneoe\\\\Desktop\\\\파이널\\\\데이터셋 테스트용\\\\OrginFinalDataset\\\\trainset')

    