from faker import Faker 

cnt = int(input('number : '))   


fake = Faker("ko-KR")  #Faker

#이름, 주소 리스트 생성
def make_user(num) :    
    user_name = []  #이름리스트
    user_adrs = []  #주소리스트
    for i in range(0,num):
        user_name.append(fake.name())
        user_adrs.append(fake.address())
    make_dict(num, user_name,user_adrs)


#dict 생성
def make_dict(num, user_name, user_adrs) :
    user_info = {}
    for i in range(0,num):    #user_name크기만큼 반복
        user_info[user_name[i]] = user_adrs[i]  #dict에 데이터 입력
        # user_info
    save_data(user_info)
    

def save_data(user_info) : 
    # file_path = input('파일저장경로:')
    
    f = open('/Users/kiny6.LAPTOP-097ORSID/Desktop/ksh/python/user_info.txt','w')   
    f.write("이름        주소\n")
    for name, adrs in user_info.items() : 
        f.write(f'{name} : {adrs}\n')

    f.close


def load_data() : 
    
    #원하는 경로 수정
    f = open('/Users/kiny6.LAPTOP-097ORSID/Desktop/ksh/python/user_info.txt','r')   
    while True:
        line = f.readline()
        if not line : 
            break
        print(line)
    f.close

make_user(cnt) #user데이터 생성
load_data() #확인용



