
#20192822_김현우 컴퓨팅적 사고 과제
#은행 프로그램 입니다
#사용자의 이름을 아이디로 정하여, 각 사용자의 계좌 잔액정보 확인과 자신의 계좌에 입출금, 예금 및 적금의 이자계산, 환전 등의 기능을 지원합니다
#어디까지 구현했는가 : 입력,회원 판별,신규 회원 가입,통장의 잔고 확인, 입출금, 한 50%부족한 환율계산,
#처리못한 부분. 동명이인은 계좌를 두개이상 못만듬. / 비밀번호 혹은 개인 식별 번호를 입력받는 부분은 미구현

def real_change_money():#환전
     print('1.원')
     print('2.달러')
     print('3.엔화')
     print('4.유로')
     print('5.위안')
     while True:
          s_money=int(input('현제 보유하고 계시는 화폐의 종류에 맞는 숫자를 입력해주세요 : '))
          if (s_money!=1 and s_money!=2 and s_money!=3 and s_money!=4 and s_money!=5):
               print('잘못된 입력입니다')
          else :
               e_money=int(input('환전을 원하십니까 : '))
               if ((e_money!=1 and e_money!=2 and e_money!=3 and e_money!=4 and e_money!=5) or (s_money==e_money)):
                    print('잘못된 입력입니다')
               else:
                    break
     how_much=int(input('얼마를 환전하실건가요? : '))
     print("한국 시 2019년 4월 24일 22시 50분을 기준으로\n")
     if(s_money==1 and e_money==2):
          print(how_much,'원은',how_much/1154.14,'달러 입니다\n')
     elif(s_money==1 and e_money==3):
          print(how_much,'원은',how_much/10.34,'엔 입니다\n')
     elif(s_money==1 and e_money==4):
          print(how_much,'원은',how_much/1,294.5,'유로 입니다\n')
     elif(s_money==1 and e_money==5):
          print(how_much,'원은',how_much/172.01,'위안 입니다\n')
     elif(s_money==2 and e_money==1):
          print(how_much,'달러는',how_much/0.00087,'원 입니다\n')
     elif(s_money==2 and e_money==3):
          print(how_much,'달러는',how_much/0.0089,'엔 입니다\n')
     elif(s_money==2 and e_money==4):
          print(how_much,'달러는',how_much/1.12,'유로 입니다\n')
     elif(s_money==2 and e_money==5):
          print(how_much,'달러는',how_much/0.15,'위안 입니다\n')
     elif(s_money==3 and e_money==1):
          print(how_much,'엔은',how_much/0.097,'원 입니다\n')
     elif(s_money==3 and e_money==2):
          print(how_much,'엔은',how_much/111.79,'달러 입니다\n')
     elif(s_money==3 and e_money==4):
          print(how_much,'엔은',how_much/125.11,'유로 입니다\n')
     elif(s_money==3 and e_money==5):
          print(how_much,'엔은',how_much/16.63,'위안 입니다\n')
     elif(s_money==4 and e_money==1):
          print(how_much,'유로는',how_much/0.00077,'원 입니다\n')
     elif(s_money==4 and e_money==2):
          print(how_much,'유로는',how_much/0.89,'달러 입니다\n')
     elif(s_money==4 and e_money==3):
          print(how_much,'유로는',how_much/0.008,'엔 입니다\n')
     elif(s_money==4 and e_money==5):
          print(how_much,'유로는',how_much/0.13,'위안 입니다\n')
     elif(s_money==5 and e_money==1):
          print(how_much,'위안은',how_much/0.0058,'원 입니다\n')
     elif(s_money==5 and e_money==2):
          print(how_much,'위안은',how_much/6.72,'달러 입니다\n')
     elif(s_money==5 and e_money==3):
          print(how_much,'위안은',how_much/0.06,'엔 입니다\n')
     elif(s_money==5 and e_money==4):
          print(how_much,'위안은',how_much/7.52,'유로 입니다\n')
     time.sleep(1)
     print()
#################################################################################################################################################################
     
def cal_reg_put_benefits1(money,bene,years): # 단리적금
     sum_of_money=0
     benes=0
     for i in range(years):
          sum_of_money=sum_of_money+money
          benes=benes+(sum_of_money*((bene*0.01)/12))
     print("\n\n적금을 통해, %d 개월 후 %d원(윈금 %d원 + 이자 %d원)을 얻을수 있습니다"%(years,sum_of_money+benes,sum_of_money,benes))
#################################################################################################################################################################
def cal_reg_put_benefits2(money,bene,years): # 복리적금
     sum_of_money=0
     _sums=money*years
     benes=0
     for i in range(years):
          benes=sum_of_money*((bene*0.01)/12)
          sum_of_money = sum_of_money  + benes + money
     benes=sum_of_money*((bene*0.01)/12)
     sum_of_money = sum_of_money  + benes
     print("\n\n적금을 통해, %d 개월 후 %d원(윈금 %d원 + 이자 %d원)을 얻을수 있습니다"%(years,sum_of_money,_sums,sum_of_money-_sums))
#################################################################################################################################################################
def cal_benefits1(money,bene,years): # 단리예금
     a_money=money*(1+((bene*0.01)*years/12))
     print("\n\n예금을 통해, %d 개월 후 %d원(윈금 %d원 + 이자 %d원)을 얻을수 있습니다"%(years,a_money,money,a_money-money))

#################################################################################################################################################################
def cal_benefits2(money,bene,years): # 복리예금
     a_money=money
     for i in range(years):
          a_money=a_money+a_money*(bene*0.01/12)
     print("\n\n예금을 통해, %d 개월 후 %d원(윈금 %d원 + 이자 %d원)을 얻을수 있습니다"%(years,a_money,money,a_money-money))
#################################################################################################################################################################
def deposit_cal():                                                                                                                                                                                           # 예적금 이자계산
     check=input("예금이자를 계산하신다면 1번, 적금 이자를 계산하신다면 2번. 계산을 원치 않으신다면 그 이외의 키를 입력해주세요")
     if(check=='1'):
          ways=int(input('단리일경우 1번, 복리일경우 2번을 눌러주세요 : '))
          b_money=int(input('원금을 입력하세요(원) : '))
          benefits=float(input('년 이율을 입력하세요(%) : '))
          years=int(input('납입 기간을 입력하세요(월) : '))
          if ways==2: # 복리예금
                   cal_benefits2(b_money,benefits,years)
          elif ways==1: #단리예금
                   cal_benefits1(b_money,benefits,years)
     elif(check=='2'):
          ways=int(input('단리일경우 1번, 복리일경우 2번을 눌러주세요 : '))
          b_money=int(input('매달 납입금액을 입력하세요 '))
          benefits=float(input('년 이율을 입력하세요(%) : '))
          years=int(input('납입 기간을 입력하세요(월) : '))
          if ways==1 : # 단리적금
             cal_reg_put_benefits1(b_money,benefits,years)
          elif ways==2 : #복리적금
             cal_reg_put_benefits2(b_money,benefits,years)
     else:
          print('\n')
          return 0
#################################################################################################################################################################
def change_money():                                                                                                                                        #변명/ 환율 api를 가져오지 못해서, 하나의 사용자에 여러가지 계좌를 구현하지 못해서 미구현
     print('\n죄송합니다만, 저희 은행의 외환 보유 상태가 좋지못해, 환전이 불가능합니다.\n')
     time.sleep(0.5)
     print("직접적으로 환전이 불가능하오나, 저희 은행은 가상 환전 서비스를 제공하고 있습니다.\n")
     time.sleep(0.5)
     check=input("가상환전 서비스를 시작하시려면 1번, 아니라면 1번을 제외한 아무키나 눌러 주십시오")
     if check=='1':
          real_change_money()
     else :
          return 0
#################################################################################################################################################################
def inout_money(name):                                                                                                  #내 계좌에서 입출금을 시행함
     _check=input("입금을 원하시면 1번, 출금을 원하시면 2번을 눌러주세요")
     if _check=='1' :
          while True:
               in_money=input('입금할 금액을 입력하세요(원) : ')
               balance=str(int(in_money)+int(check_money(name)))                                              #계좌에 입금
               update_info(name,balance)
               break
     if _check=='2' :
          while True:
               out_money=input('출금할 금액을 입력하세요(원) : ')
               if (int(out_money)>int(check_money(name))) :                                                        #출금액이 현제 통장 잔고보다 많으면
                    print("통장에 금액이 충분하지 않습니다.")                                                     #출금 거부
               else:
                    balance=str(int(check_money(name))-int(out_money))                                        #계좌에서 출금
                    update_info(name,balance)
                    break
#################################################################################################################################################################               
def check_money(name):
      f = open("useraccount.txt",'r')
      next_money=0
      moneyis=0
      while True:
               num_account = f.readline()[:-1]
               if next_money==1:                                      #이번줄이 잔고가 있는 줄이면
                    moneyis = num_account                        #가장 최근의 통장잔고상태를 저장함
                    next_money=0 #초기화
               if num_account == name :                          #현제 사용자의 이름이 파일을 쭉읽었을때 있으면
                    next_money=1                                      # 다음줄에 사용자의 통장 잔고가 남아있음을 표시
               if not num_account: 
                    f.close()
                    return moneyis                                     #useraccount 파일이 갱신정보를 뒤에 추가하는 형태임, 가장 나중의 계좌 입출금 정보를 확인하기위해 파일이 다 끝난 뒤 리턴함
                    break
#################################################################################################################################################################
def work_space(name): ## 은행업무 공간, 예적금 이자계산,계좌 정보 확인,환전,등등의 기능// 송금, 계좌개설 기능 미구현
     print(name,'고객님 반갑습니다. 은행에 오신것을 환영합니다\n\n')
     next_money=0
     money=0
     while True:
        print("1.잔액 확인")
        print("2.환전")
        print("3.입출금")
        print("4.예적금 이자 계산")
        print("5.종료\n\n")
        n=input("하실 업무의 번호를 입력해주세요")
        if(n=='1'):
             money=check_money(name)                                                           #잔고확인
             print('잠시만 기다려 주세요\n')
             time.sleep(1)
             print("현제",name,"님의 통장 잔액은",money,"원 입니다\n\n")
             time.sleep(1)
        elif n=='2':
             print('잠시만 기다려 주세요\n')
             time.sleep(1)
             change_money()                                                                            #환전,좀 많이 부족함
        elif n=='3':
             print('잠시만 기다려 주세요\n')
             time.sleep(1)
             inout_money(name)                                                                       #내 계좌에 입출금
        elif n=='4':
             print('잠시만 기다려 주세요\n')
             time.sleep(1)
             deposit_cal()                                                                                 #예적금 이자 확인
        elif n=='5':
             print("이용해 주셔서 감사합니다")                                                  #종료
             time.sleep(1)
             sys.exit()
        else :
             print("잘못된 입력입니다. 다시 입력해 주시기 바랍니다")
     return 0
#################################################################################################################################################################

def update_info(name,money):                            #통장 잔액 갱신해주는 부분
     f_user = open("useraccount.txt",'a+')               # useraccount 라는 파일에 하나하나씩 갱신시켜준다
     f_user.write(name) 
     f_user.write('\n')
     f_user.write(money)
     f_user.write('\n')

#################################################################################################################################################################

def member_checking(ch_user): ##고객인지 아닌지를 파악하는 역할
     f = open("userlist.txt", "r")
     while True:
        line = f.readline()[:-1] # 요게 뒤에 엔터값 잡아주는 역할, 엔터값 잡아주니까 무조건 새로 입력 넣을떄 이름엔터
        if line==ch_user: # 고객의 이름이 확인되면 
            member=1     # 고객임을 표시함
            break
        if not line:
            member=0
            break
     f.close()
     return member

#################################################################################################################################################################

def new_member(): ## 신규 가입/ 이름을 입력하여 신규 가입을 한다
     print("\n신규 가입을 환영합니다!")
     while True:
          new=input("사용자의 이름을 입력해 주세요") # 사용자 이름 입력
          chk=member_checking(new)
          if chk==1:
               print('이미 등록된 사용자 입니다')
               return 0
          else :
               f = open("userlist.txt", "a+") 
               f.write(new)                            # 새 사용자의 등록
               f.write('\n')
               f.close()
               update_info(new,'0')               # 사용자의 돈 정보 확
               return 0
     
#################################################################################################################################################################

def whoru():
     while True:
          user_name=input("사용자의 이름을 입력해 주세요 : ")
          if user_name==' ' :
               print("잘못 입력하셨습니다. 다시 입력해주세요")
          else :
               break
     i=member_checking(user_name)
     if i==1:                                 #고객이면
          work_space(user_name)    #작업공간으로 이동
          i=0
     elif i==0:                              # 등록되지 않은 사용자일경우
          print("가입되지 않은 사용자 입니다.")
          i=0

#################################################################################################################################################################

import time
import sys
for i in range(8):
     print('\n')
     time.sleep(0.1)
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n\n')
time.sleep(0.3)
print('''
         *********                  *****                 ****          ***          ***      ***          
         ***      ***               *** **                 *** **       ***           ***    ***          
         ***      ***              ***   **                ***  **      ***           ***  ***              
         ********                 *********               ***   **     ***           ******             
         ***      ***             ***      **              ***    **    ***           ***  ***                 
         ***      ***            ***        **             ***     **   ***           ***    ***            
         ***      ***           ***          **            ***       ** ***           ***      ***          
         *********             ***           **           ***         ****            ***       ***         
''')
time.sleep(0.3)
print('\n\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
for i in range(8):
     print('\n')
     time.sleep(0.1)

print('\n * 윈도우 명령 프롬프트 상에서 실행하면 신규 가입을 했으나 이름이 인식이 되지 않는 버그가 발생합니다. 버그가 발생할경우 파일을 종료한 후 다시 실행시키거나, 파이썬 쉘 창에서 실행시키는 것을 권장합니다.*\n')

file_info = open("useraccount.txt",'a+')
file_info.close()
file_user = open("userlist.txt", "a+")
file_user.close()
check=0
print('안녕하십니까 \"숭실\" 은행입니다')         # 사용자의 이름을 입력하는 부분
while True:
     check=input('새로운 회원 가입을 원하시면 1번, 고객이면 2번을, 프로그램 종료를 원하시면  3번을 눌러주세요 : ')
     if check=='2' :                                                                                                     # 가입된 고객일경우 업무환경으로 이동
          whoru()

     elif check=='1' :                                                                                                   # 신규가입
          new_member()   

     elif check=='3' :                                                                                                  # 종료
          sys.exit()
          
     else:                                                                                                                  #잘못된 입력, 다시 입력받게됨
          print('잘못된 정보입니다, 다시 입력해주세요')
