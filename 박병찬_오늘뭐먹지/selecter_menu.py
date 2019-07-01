# 강의실 위치 찾기
def classroom():
    import webbrowser
    print("이 프로그램은 강의실 위치를 찾아줍니다")
    num = int(input("강의실 번호를 입력해 주세요 : ")) 
    building = num // 1000
    stair = num // 100 - building *10
    if ( building == 1 ):
        print("강의실은 베어드홀 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19023017")
    elif ( building == 2 ):
        print("강의실은 경상관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19025939")
    elif ( building == 3 ):
        print("강의실은 문화관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19025914")
    elif ( building == 4 ): 
        print("강의실은 안익태기념관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19021696")
    elif ( building == 5 ):
        print("강의실은 형남공학관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19022584")
    elif ( building == 6 ):
        print("강의실은 교육관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19026737")
    elif ( building == 7 ):
        print("강의실은 백마관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19025712")
    elif ( building == 8 ):
        print("강의실은 한경직기념관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=13445041")
    elif ( building == 9 ):
        print("강의실은 신양관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19024405")
    elif ( building == 10 ):
        print("강의실은 벤처중소기업센터 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19026091")
    elif ( building == 11 ):
        print("강의실은 진리관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19024127")
    elif ( building == 12 ):
        print("강의실은 조만식기념관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19022033")
    elif ( building == 15 ):
        print("강의실은 연구관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19025224")
    elif ( building == 16 ):
        print("강의실은 창신관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19025670")
    elif ( building == 17 ):
        print("강의실은 Global Brain Hall %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19026280")
    elif ( building == 18 ):
        print("강의실은 Residence Hall %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19025182")
    elif ( building == 19 ):
        print("강의실은 전산관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19026089")
    elif ( building == 20 ):
        print("강의실은 미래관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=30850824")
    elif ( building == 21 ):
        print("강의실은 정보과학관 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19024744")
    elif ( building == 22 ):
        print("강의실은 웨스트민스터홀 %d층에 위치해 있습니다." %stair)
        webbrowser.open("https://map.naver.com/local/siteview.nhn?code=19023041")
    else :
        print("다시 확인하고 입력해주십시오")

    last() 

#숭실대 음식점 모음집
def allfood ():
    print("이 프로그램은 숭실대 근처 맛집을 알려주는 프로그램입니다")
    print("숭실대학교 식당\n 찌개 + 한식\n- 백채 김치찌개 (고기 통으로 줌 + 계란말이 짱)\n- 밀알 ( 모든 소스가 맛이 같음 )\n - 찌개대학 부대학과 ( 무한리필 )\n- 청운음식점\n- 따듯한 밥상\n- the진국 ( 반찬 재활용 논란 )\n- 논두렁갈비\n- 코웍비스트로\n- 곤지암\n- 신의주 찹쌀순대\n- 손칼국수\n- 이모네\n\n간단한 음식\n- 도스마스\n- 지지고 (숭실대점이 본점)\n- 맥도날드\n\n일식\n- 아쯔다무라\n- 우마이 (일식 카레)\n- 마루스시\n- lee 스시\n- 멘동\n- 도쿄야네\n- 돈스 앤 덮밥\n- 도쿄라멘3900\n\n중식\n- 가야성\n- 황궁\n- 강서\n- 연래춘\n- 취향\n\n분식\n- 동대문 엽떡\n- 신전\n- 추억과 김밥\n- 왕돈까스 왕 냉면\n- 준호네\n- 청년다방\n- 현선이네\n- 더코네\n\n고기집\n- 미담길 \n- 상도곱창\n- 고기스토리\n- 불타는  소금구이\n- 풍년집 (무한 리필)\n- 청솔막창\n\n피자&치킨\n- 더피자(피맥 쫀좋)\n- 대윤 파닭 (배달)\n\n돈까스 3대장\n- 아쯔다무라 ( 정문쪽 / 1번 출구)\n- 더 코네 ( 즉석 떡볶이 + 종류별 돈까스)\n- 숭실골 ( 혼밥을 위한 곳 )\n\n제육 3대장\n- 숭실골\n- 밀알\n- 추억과 김밥\n\n선배님 사주세요\n- 내찜닭(맛/양)\n- 샤로스톤 (규카츠 + 양식)\n- 스톤 504\n- 889 (화로구이)\n- 마루스시 (미미 1스타 초밥)\n\n학교 안\n- 푸드코트\n- 더키친\n- 학생식당\n- 교직원식당")
    last()

#뭘먹을지 고민될때
def whatfood ():
    import random
    print("이 프로그램은 무슨 음식을 먹을지 랜덤으로 골라주는 프로그램입니다")
    print("찌개 + 한식 = 1, 간단한 음식 = 2, 일식 = 3, 중식 = 4, 분식 = 5, 고깃집 = 6, 피자,치킨 = 7, 돈까스 3대장 = 8, 제육 3대장 : 9 ")
    type = int(input("먼저 원하는 식사 타입을 고르시오 : "))
    print("음...... 제 추천은요....?")

    # 찌개 + 한식
    if (type == 1):
        a = random.randint(1,13)
        if a == 1 :
           print("백채 김치찌개를 추천드립니다!")
        elif a == 2 :
           print("밀알을 추천드립니다!")
        elif a == 3 :
           print("찌개대학 부대학과를 추천드립니다!")
        elif a == 4 :
           print("총운 음식점을 추천드립니다!")
        elif a == 5 :
           print("따뜻한 밥상을 추천드립니다!")
        elif a == 6 :
           print("the진국을 추천드립니다!")
        elif a == 7 :
           print("논두렁갈비를 추천드립니다!")
        elif a == 8 :
           print("코웩비스트로를 추천드립니다!")
        elif a == 9 :
           print("곤지암을 추천드립니다!")
        elif a == 10 :
           print("신의주 찹쌀순대를 추천드립니다!")
        elif a == 11 :
           print("손칼국수를 추천드립니다!")
        elif a == 12 :
           print("이모네를 추천드립니다!")

    # 간단한 음식       
    if (type == 2):
        a = random.randint(1,4)
        if a == 1 :
           print("도스마스를 추천드립니다!")
        elif a == 2 :
           print("지지고을 추천드립니다!")
        elif a == 3 :
           print("맥도날드를 추천드립니다!")

    # 일식
    if (type == 3):
        a = random.randint(1,9)
        if a == 1 :
           print("아쯔다무라를 추천드립니다!")
        elif a == 2 :
           print("우마이를 추천드립니다!")
        elif a == 3 :
           print("마루스시를 추천드립니다!")
        elif a == 4 :
           print("lee스시를 추천드립니다!")
        elif a == 5 :
           print("멘동을 추천드립니다!")
        elif a == 6 :
           print("도쿄야네를 추천드립니다!")
        elif a == 7 :
           print("돈스 앤 덮밥을 추천드립니다!")
        elif a == 8 :
           print("도쿄라멘3900을 추천드립니다!")
           

    # 중식
    if (type == 4):
        a = random.randint(1,6)
        if a == 1 :
           print("가야성을 추천드립니다!")
        elif a == 2 :
           print("황궁을 추천드립니다!")
        elif a == 3 :
           print("강서를 추천드립니다!")
        elif a == 4 :
           print("연래춘을 추천드립니다!")
        elif a == 5 :
           print("취향을 추천드립니다!")
     
      
    # 분식
    if (type == 5):
        a = random.randint(1,9)
        if a == 1 :
           print("동대문엽기떡볶이를 추천드립니다!")
        elif a == 2 :
           print("신전 떡볶이를 추천드립니다!")
        elif a == 3 :
           print("추억과 김밥을 추천드립니다!")
        elif a == 4 :
           print("왕돈가스 왕냉면을 추천드립니다!")
        elif a == 5 :
           print("준호네를 추천드립니다!")
        elif a == 6 :
           print("청년다방을 추천드립니다!")
        elif a == 7 :
           print("현선이네를 추천드립니다!")
        elif a == 8 :
           print("더코네를 추천드립니다!")
           
       
    # 고깃집
    if (type == 6):
        a = random.randint(1,7)
        if a == 1 :
           print("미담길을 추천드립니다!")
        elif a == 2 :
           print("상도곱창을 추천드립니다!")
        elif a == 3 :
           print("고기스토리를 추천드립니다!")
        elif a == 4 :
           print("불타는소금구이를 추천드립니다!")
        elif a == 5 :
           print("풍년집을 추천드립니다!")
        elif a == 6 :
           print("청솥막창을 추천드립니다!")
       
    
    # 피자, 치킨
    if (type == 7):
        a = random.randint(1,3)
        if a == 1 :
           print("더피자를 추천드립니다!")
        elif a == 2 :
           print("대윤파닭을 추천드립니다!")
           
        
    # 돈까스 3대장
    if (type == 8):
        a = random.randint(1,4)
        if a == 1 :
           print("아쯔다무라를 추천드립니다!")
        elif a == 2 :
           print("더코네를 추천드립니다!")
        elif a == 3 :
           print("숭실골을 추천드립니다!")

       
    # 제육 3대장
    if (type == 9):
        a = random.randint(1,4)
        if a == 1 :
           print("숭실골을 추천드립니다!")
        elif a == 2 :
           print("밀알을 추천드립니다!")
        elif a == 3 :
           print("추억과 김밥을 추천드립니다!")

    last()
    
# 초기화면
def first():
    print("신입생 여러분 아직 모르시는 것이 많을 것 같아 조금 도와드리고자 이 프로그램을 만들게 되었습니다")
    print("이 프로그램에는 총 3가지 기능이 있습니다")
    print("1. 강의실 찾기, 2,숭실대 음식점 모음집, 3,오늘 뭐먹지?")
    program = int(input("원하시는 프로그램을 적어주세요 : "))
    if( program == 1 ):
        classroom()
    elif( program == 2 ):
        allfood()
    elif( program == 3 ):
        whatfood()
    else :
         print("죄송합니다. 다른기능은 준비중입니다.")

# 다시묻기
def last():
    ab = int(input("종료하시겠습니까? [ 예 : 1 / 아니오 : 2 ]  :  "))
    if(ab == 1):
        print("사용해주셔서 감사합니다")
    elif(ab == 2):
        first()

first()



