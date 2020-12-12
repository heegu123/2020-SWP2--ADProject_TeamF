from konlpy.tag import Komoran
#from check import Check
k = Komoran()

#input 문장 #output 표시된 문장
class Mark():
  # (checkList는 번역투에 사용되는 표현에서 예시문장의 형태소를 분석했을때 겹치는 부분으로 만들었습니다.)
    def __init__(self):
        self.checkList = [{"내용":"에 의하","종류":"~에 의해(수동태 번역)","출신":"영어",'대체표현':"\'에 의해\'를 붙이지 않고 바로 주어로 사용하시면 깔끔해집니다."},
             {"내용":"에 있","종류":"~에 있어(‘in/are going to’의 번역투)","출신":"영어",'대체표현':"\'~하는 데에 있어\'같은 표현을 \'~하는 데\'로 고치듯 표현자체를 사용하지 않으면 좋습니다."},
             {"내용":"의","종류":"~의(남용되기 쉬운 조사)","출신":"일본어",'대체표현':"일본어는 공식적으로 띄어쓰기가 없습니다.그래서 쉼표와 ‘의(-の)’로 그 역할을 대신합니다.\n그런데 우리말에는 띄어쓰기라는 훌륭한 기법이 있으니 ‘의’를 열심히 쓰지 않아도 됩니다.\n영어 ‘~of’도 마찬가지입니다."},
             {"내용":"경우","종류":"~경우(남용되기 쉬운 단어)","출신":"일본어",'대체표현':"문장의 첫머리에 자주 오는 \'~의 경우\'라는 표현은 대체로 생략하시는 것이 좋습니다. 한번 더 확인해 주세요."},
             {"내용":"대하","종류":"~에 대해(\'about\'의 번역투)","출신":"영어",'대체표현':"\'~에 대해\'라는 표현은 \'about\'의 영향을 받아 많이 사용되고 있습니다.\n 삭제하거나 \'혹은 '~대하여'를 목적격 조사 '을(를)'로 바꾼 표현이나 ~를 주제로\'같은 표현으로 대체하길 권장합니다."},
             {"내용":"관하","종류":"~에 관하여(\'about\'의 번역투)","출신":"영어",'대체표현':"\'~에 관하여\'라는 표현은 \'about\'의 영향을 받아 많이 사용되고 있습니다.\n 삭제하거나 \'~를 주제로\'같은 표현으로 대체하길 권장합니다."},
             {"내용": "중", "종류": "~하는 중이다(\'is -ing\'의 번역투)", "출신": "영어", '대체표현': "진행을 나타내기 위한 \'중\'은 \'~하는 중이다\'를 \'~한다\'로 고치듯 표현자체사용하지 않길 권장합니다."}, ]
#는 중이다 필요 방법

###checkList의 내용을 하나당 한번씩 문장을 확인하고 표시합니다.
    def marking(self, munjang):#문장을 받아옵니다.
        madiList = munjang.split(" ")#문장을 마디로 자릅니다.
        foundCheckList = []
        for a in self.checkList:#checkList 지금확인할거 돌림.
            madiIdx = 0
            beingNum = []
            while madiIdx < len(madiList):#마디마다 검사를함.(표시단위가 마디이기때문입니다.)

                # IN -> 입력된 마디에서 번역투 표현을 확인하기 위한 인덱스, 검사할 내용, 문장전체를 넘겨줍니다.
                #    마디를 바로 넘기지 않는 이유는 확인할 번역투가 한 마디 내에 모두 있진 않기 때문입니다.
                # OUT -> 확인한 마디를 포함하여 다음 몇 마디동안 확인한 번역투가 있는지를 숫자로 반환합니다
                check = self.checker(madiIdx, a["내용"],munjang)

                if check != 0:
                    for i in range(check):#받은 값만큼 다음 마디에도 표시해 줍니다.
                        madiList[madiIdx+i] = f"{self.checkList.index(a)+1}){madiList[madiIdx+i]}"
                        beingNum.append(madiIdx+i+1)
                    madiIdx += check - 1 #움직인 만큼 다음 검사할 INDEX도 움직입니다


                madiIdx += 1
            if len(beingNum) >0:
                foundCheckList.append((self.checkList.index(a),beingNum))  # 발견한 문제 인덱스 저장

        return (" ".join(madiList),foundCheckList )# 마디모음(list)을 다시 문장으로 만듭니다.,나온


    ###검사하는거
    def checker(self, madiIdx , checking, munjang):
        madiList = munjang.split(" ")#받은 문장을 마디모음으로 만듭니다.
        cuttedMadi = k.morphs(madiList[madiIdx])#받은 마디를 형태소로 나눕니다.
        having = 0 #번역투의 형태소가 있는 마디의 갯구 저장
        s = 0 #마디에 검사할 번역투의 형태소가 몇개 있는지 저장함.
        for b in k.morphs(checking):#확인해야하는 번역투를 형태소 단위로 나누고 순서대로 사용합니다.
            if having == 0:#함수 최초 실행(검사할 마디가 입력되고 처음 검사함.)
                if b in cuttedMadi:#검사할 번역투의 첫번째 형태소가 검사할 마디에 있는지 확인
                    having = 1
                    s += 1
                    #번역투 종류는 여기서 처리하면될듯(종류 확정 구간)
                else:
                    break
            #다음 마디에 있는지 확인
            elif (madiIdx+1 != len(madiList) and (b in k.morphs(madiList[madiIdx + 1]))):
                having += 1
                s += 1
            elif b in cuttedMadi:# 이 마디에 있는지 확인 (띄어쓰기를 안했을 경우를 위해)
                s += 1
        # 확인한 마디에 있는 겹치는 형태소의 갯수가 번역투에서 확인한 형태소의 개수와 같은지 확인합니다.
        if s != len(k.morphs(checking)):
            having=0;
        return having

#-------------------------------------------------
if __name__ == '__main__' :
    testList=["나비에 의해 꿈을 꿉니다.",
          "성능을 높이는 데에 있어 메모리 용량은",
          "원인 분석 중에 있다.",
          "승합차 경우에는",
          "합격하는 경우 좋겠네",
          "저의 경우에는",
          "그 회사의 직원의 평균 연봉의 수준은",
          "경우에 대해 제대로 이해하고 있다.",
          "친구 사귀는 중이다",]
    a = Mark()
    for y in testList:
        try:
            print(a.marking(y))
        except Exception as e:
            print(e)




