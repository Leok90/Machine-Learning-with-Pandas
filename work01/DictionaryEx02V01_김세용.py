# DictionaryEx02V01.py
# 평균 70점 이상 합격
'''
# 조건1]
	01.  없는 번호 입력시 에러메세지

	02.  없는 아이디 입력시 해당ID없음 확인
	   - in연산자 적용 get 메소드
	   - id 삭제시 xx님 탈퇴확인
	   - del 메소드 적용 삭제후 학생목록 출력

	03. 추가 등록
	   - id 존재시 중복id확인
	   - 연산자적용
'''
import sys

def Systemexit():   # 종료 함수
    print("학생관리시스템을 종료합니다")
    sys.exit()

def Signout():  # 탈퇴학생 함수
    x = input('삭제할 ID: ')
    if dic.get(x) == None:  # ID가 목록에 없을 경우
        print('해당 ID 없음')
        return
    if x in dic.keys():
        del dic[x]
        del idList[idList.index(x)]
        deleteIDList.append(x)
        print('Red님 탈퇴확인')
    else:
        print('해당 ID 없음')
    Showlist()

def Signin():   # 추가등록 함수
    print('회원가입')
    id = input('ID 입력: ')
    if id in idList:
        print('중복 ID 확인')
        return
    if id in deleteIDList:
        print('탈퇴한 ID로는 가입할 수 없습니다.')
        return
    idList.append(id)
    score1 = int(input('필기점수 입력: '))
    score2 = int(input('실기점수 입력: '))
    score3 = int(input('인성점수 입력: '))
    dic[idList[-1]] = [score1, score2, score3]  # 딕셔너리 타입으로 학생 정보를 저장
    avgScore[idList[-1]] = round(sum(dic[idList[-1]]) / 3, 2)  # 딕셔너리 타입으로 평균점수를 저장
    if avgScore[idList[-1]] >= 70:
        passStudent[idList[-1]] = '합격'
    elif avgScore[idList[-1]] < 70 and 0 < avgScore[idList[i]]:
        passStudent[idList[-1]] = '불합격'
    Showlist()

def Showlist(): # 학생 목록을 출력하는 함수
    print('학생목록')
    for i in range(len(MenuList)):
        print(MenuList[i], end='\t')
    print('')
    print('-' * 60)
    for i in idList:
        print(i, '\t', dic[i][0], '\t', dic[i][1], '\t', dic[i][2], '\t', sum(dic[i]), '\t', avgScore[i], '\t',
              passStudent[i])
    print('')


menu = [' 1. 탈퇴학생 ', ' 2. 추가등록 ', ' 3. 학생목록 ', ' 9. 메뉴종료 ']
menuChk = ['1', '2', '3', '9']
itemList = ['ID', '필기점수', '실기점수', '인성점수']
MenuList = ["ID", "필기", "실기", "인성", "합계", "평균", "합격유무"]

idList = ["Orange", "Red", "Yellow", "Green", "Blue", "Navy", "Purple"];
scoreList = [[47, 58, 85], [12, 75, 84], [57, 75, 84], [36, 86, 87],
             [89, 67, 46], [45, 86, 46], [68, 47, 98]];
avgScore = {}   # 평균점수를 담은 딕셔너리
passStudent = {}    # 합격여부를 담은 딕셔너리

dic = {}    # 학생 점수 정보를 담은 딕셔너리
deleteIDList = []   # 탈퇴한 회원 ID 리스트
idx = 0;

n = len(idList)
for i in range(n):  # 평균 점수를 구해 avgScore에 담고 합불 여부를 passStudent에 담음
    dic[idList[i]] = scoreList[i]  # 딕셔너리 타입으로 학생 정보를 저장
    avgScore[idList[i]] = round(sum(scoreList[i]) / 3, 2)  # 딕셔너리 타입으로 평균점수를 저장
    if avgScore[idList[i]] >= 70:
        passStudent[idList[i]] = '합격'
    elif avgScore[idList[i]] < 70 and 0 < avgScore[idList[i]]:
        passStudent[idList[i]] = '불합격'

while True: # 메뉴 출력
    print('-' * 60)
    print('학생관리시스템v01')
    print('-' * 60)
    for i in range(len(menu)):
        print(menu[i], end='\t')
    print('')
    print('-' * 60)

    idx = int(input('번호 입력: '))
    if idx == 1:    # 탈퇴학생
        Signout()
    elif idx == 2:  # 추가등록
        Signin()
    elif idx == 3:  # 학생목록
        Showlist()
    elif idx == 9:  # 메뉴종료
        Systemexit()
    else:
        print('에러가 발생했습니다.')
