import csv
from faker import Faker


def file_read():    # 파일 읽어오기
    
    with open('./sample_data.csv','r',newline='', encoding='cp949') as r:    #newline ="행 데이터사이 공백제거용"
        data = csv.DictReader(r, delimiter=',') #',' 기준 분할
        data_list = list(data)  

        r.close()
 
    return data_list 


def file_save():     # 파일 저장하기
    new_data = make_ndata()
    print(new_data)     #확인용
    
    col = list(new_data[0].keys())  #key값을 list로 저장
    
    try:
        with open('./n_sample_data.csv', 'w', newline="", encoding='cp949') as w:
            write_data = csv.DictWriter(w, fieldnames=col)
            write_data.writeheader()  # 파일의 첫번째 행에 항목이름들을 넣어줄 것인지 결정

            for row in new_data:
                write_data.writerow(row)  # 데이터 한줄씩 입력

        w.close()

    except:
        print('I/O error')
 

def make_ndata():       #n_sample_data 데이터 생성

        data_list = file_read()         #sample_data 읽어옴
        user_info = make_user_info(30)  #성명, 주소 정보 생성

        name_col = make_column(user_info, 30, 0, 1)         ####성명컬럼
        adrs_col = make_column(user_info, 30, 1, 2)         ####주소지컬럼
        nm_bfor_col = make_column(data_list, 30, 0, 2)      ####성명이전컬럼
        nm_aftr_col = make_column(data_list, 30, 2, 12)     ####성명이후컬럼

    ###주소지 컬럼 분리하기
        adrs_dtl_col = []  # 상세주소 컬럼
        for i in range(30):
            if(adrs_col[i]['주소'].find("(") != -1):        # '(' 들어 있는 컬럼이면
                chrg_adrs = adrs_col[i]['주소'].split('(')  # '(' 기준 쪼갬
                adrs_dtl_col.append({'상세주소': chrg_adrs[1].replace(')', "")})
                adrs_col[i]['주소'] = chrg_adrs[0]          # 기존 주소 컬럼 교체
            else:
                adrs_dtl_col.append({'상세주소': " "})      # 상세주소 없을시, 공백 입력

     ###컬럼합치기
        new_data = {}
        new_data = nm_bfor_col
        for i in range(30) :
           new_data[i].update(name_col[i])                  # update를 이용하여 기존 데이터 뒤에 컬럼 추가
           new_data[i].update(nm_aftr_col[i])
           new_data[i]['접수자 주소'] = adrs_col[i]['주소'] # 주소수정
           new_data[i]['발생상세주소'] = adrs_dtl_col[i]['상세주소']
        # print(new_data)

        return new_data    


def make_user_info(len):    #faker로 정보 생성
    fake = Faker("ko-KR")
    user_info =[]
    for i in range(len):
        user_info.append({'성명':fake.name(),
                    '주소': fake.address()})

    # print(user_info) #확인용
    return user_info

# data:분리할 데이터, data_cnt:데이터 개수, col_str_cnt:나눌컬럼의 시작인덱스, col_end_cnt:나눌컬럼의 마지막인덱스
def make_column(data, data_cnt, col_str_cnt, col_end_cnt):  #sample_data 컬럼분리
    new_list = []  
    new_dict = {}
    col = list(data[0].keys())  #key값 얻어오기
    
    for i in range(data_cnt):
        for j in range(col_str_cnt, col_end_cnt):  # 몇번컬럼까지 담을지 범위 지정
            if (j == col_str_cnt):  # 첫컬럼일경우
                new_dict = {col[j]: data[i][col[j]]}  # new_dict에 j번째 컬럼 추가
                if(j == col_end_cnt-1):      #가져오려는 컬럼이 하나인 경우
                    new_list.append(new_dict)   #데이터를 new_list에 추가
            else:   #첫컬럼이 아닐경우
                new_dict.update({col[j]: data[i][col[j]]})     #new_dict에 j번째컬럼을 병합
                if(j == col_end_cnt-1):     #j가 col_end_cnt-1(마지막)일 경우
                    new_list.append(new_dict)   #new_list에 데이터를 추가

    return new_list

file_read() #파일읽기
file_save() #파일쓰기
