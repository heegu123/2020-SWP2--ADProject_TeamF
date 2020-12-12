# 번역투의 문제점 : 우리말에 부자연스러운 외국어 어순과 어법을 우리말처럼 둔갑시키면 우리말이 파괴됩니다.
# 번역투는 무슨 말인지는 알겠지만 깔끔한 문장이라고 느끼기엔 무리가 있습니다.
# 사용자가 작성한 문장이 깔끔한 문장인지 알아보기위해 이 프로그램을 고안하였습니다.
# 목적 : 문장을 '말하는것처럼(구어체처럼) 자연스럽게 수정하는게 목표입니다.

# 이 파일은 그 중 이중피동 문장을 교정하기 위해 작성되었습니다.
from konlpy.tag import Hannanum

hannanum = Hannanum()

class doublePassiveExpression:
    def __init__(self, sentence):
        self.sentence = sentence
        self.analyzed = hannanum.morphs(self.sentence)
        """
        <예시문 List>

        예문 1 : 교실이 밝혀졌다. --> *예외 우* '밝히다' 는 '밝 + 히'가 아니고 기본형이 '밝히'임
        예문 2 : 내 이름이 잊혀지다.
        """

        """
        <Error Case>

        문장1 : 내 교실이 바뀌어졌어
            바꾸 + "이"(피동접미사) + "어지다"(피동형 보조동사)로 이중피동에 해당하는 경우인데 hannanum.morphs에서 '바꾸+이'를 '바뀌'로 한번에 처리해버림.

        """
        self.index = 0
        self.suggestionMessages = []
    def getCorrectedSentence(self):
        doublePassiveExpressionList = []
        result = "*이중피동 표현을 사용하였습니다*"
        for i in range(len(self.analyzed) - 3):

            # self.analyzed[i][-1]에서 [-1]이 있는 이유는 피동접미사 "이,히,리,기" 가 hannum.morphs에서 따로 추출되지 않는 경우가 있음
            # self.analyzed[i+1]+ self.analyzed[i+2] 는 주된 이중표현 형식인 (피동표현 + 피동형 보조동사"-어지")의 꼴에 나오는 "어지"를 추출

            if self.analyzed[i][-1] + self.analyzed[i + 1] + self.analyzed[i + 2] + self.analyzed[i+3] == "되이어지":
                self.index += 1
                doublePassiveExpressionList.append("%s.피동 표현'되(다)'와 '-어지다' 표현이 중복사용된 '되어지다'표현이 있습니다." %str(self.index))
                self.suggestionMessages.append("'~되어지다' 표현은 이중피동 오류이므로 '~되다' 또는 '~어지다'표현로 수정해 피동표현을 한번만 사용하게 수정해야합니다.")
            elif self.analyzed[i][-1] + self.analyzed[i + 1] + self.analyzed[i + 2] == "되어지":
                self.index += 1
                doublePassiveExpressionList.append("%s.피동 표현'되(다)'와 '-어지다' 표현이 중복사용된 '되어지다'표현이 있습니다." %str(self.index))
                self.suggestionMessages.append("'~되어지다' 표현은 이중피동 오류이므로 '~되다' 또는 '~어지다'표현로 수정해 피동표현을 한번만 사용하게 수정해야합니다.")
            elif self.analyzed[i][-1] + self.analyzed[i + 1] + self.analyzed[i + 2] == "이어지":
                self.index += 1
                doublePassiveExpressionList.append("%s.피동 접사'이'와 '-어지다' 표현이 중복사용된 '-여지다'표현이 있습니다."%str(self.index))
                self.suggestionMessages.append("'~여지다' 표현은 이중피동 오류이므로 피동접사'-이-' 또는 '~어지다'를 한번만 사용한 표현으로 수정해야합니다.")
            elif self.analyzed[i][-1] + self.analyzed[i + 1] + self.analyzed[i + 2] == "려지다":  # Hannanum.morphs가 '리'를 못잡는것 같음
                self.index += 1
                doublePassiveExpressionList.append("%s.피동 접사'리'와 '-어지다' 표현이 중복사용된 '-려지다'표현이 있습니다."%str(self.index))
                self.suggestionMessages.append("'~려지다' 표현은 이중피동 오류이므로 피동접사'-리-' 또는 '~어지다'를 한번만 사용한 표현으로 수정해야합니다.")

            elif self.analyzed[i][-1] + self.analyzed[i + 1] + self.analyzed[i + 2] == "기어지":
                self.index += 1
                doublePassiveExpressionList.append("%s.피동 접사'기'와 '-어지다' 표현이 중복사용된 '-겨지다'표현이 있습니다."%str(self.index))
                self.suggestionMessages.append("'~겨지다' 표현은 이중피동 오류이므로 피동접사'-기-' 또는 '~어지다'를 한번만 사용한 표현으로 수정해야합니다.")
            elif self.analyzed[i][-1] + self.analyzed[i + 1] + self.analyzed[i + 2] == "히어지":
                if self.analyzed[i] == "밝히":  # 위에 예문1에서 설명했음
                    pass
                else:
                    self.index+=1
                    doublePassiveExpressionList.append("%s.피동 접사'히'와 '-어지다' 표현이 중복사용된 '-혀지'표현이 있습니다."%str(self.index))
                    self.suggestionMessages.append("'~혀지다' 표현은 이중피동 오류이므로 피동접사'--' 또는 '~어지다'를 한번만 사용한 표현으로 수정해야합니다.")
        if doublePassiveExpressionList == []:
            return ''
        else:
            for i in range(len(doublePassiveExpressionList)):
                result += ('\n'+'--->'+doublePassiveExpressionList[i])
            return result

    def getSuggestion(self):
        message = "*이중피동표현을 %d번 사용하였습니다.*"%self.index
        for i in self.suggestionMessages:
            message += '\n'
            message += i

        if self.index == 0:
            message = ""

        return message

if __name__ == '__main__':
    inputSentence = input("문장을 입력하시오 : ")
    k = doublePassiveExpression(inputSentence)
    sol = k.getCorrectedSentence()
    suggest = k.getSuggestion()
    print(sol)
    print(suggest)
