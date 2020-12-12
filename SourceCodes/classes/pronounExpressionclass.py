# 번역투의 문제점 : 우리말에 부자연스러운 외국어 어순과 어법을 우리말처럼 둔갑시키면 우리말이 파괴됩니다.
#               번역투는 무슨 말인지는 알겠지만 깔끔한 문장이라고 느끼기엔 무리가 있습니다.
#               사용자가 작성한 문장이 깔끔한 문장인지 알아보기위해 이 프로그램을 고안하였습니다.

#               이 파일은 그 중 영어 번역투에서 발생한 문제인 대명사의 남용을 교정하기 위해 작성되었습니다.
#               why? 우리말은 유추가 가능하면 대명사를 쓰지 않습니다.
#               why? 한국어의 '구어'에서는 '그'나 '그녀'를 사용하지 않습니다.
#               (추가 정보 : '그', '그녀'는 한국어에 없던 표현이고, 게다가 영어의 직역도 아닌 영어의 일본어번역을 중역한 단어입니다.)

#               <예시>
#               1. 철수는 사과를 좋아해서 퇴근길에 그는 과일가게에서 사과를 샀습니다.
#               2. 철수는 사과를 좋아해서 퇴근길에 과일가게에서 사과를 샀습니다.
#               ----> 대명사 '그는'을  사용한 1번 문장보다 2번 문장이 우리말 표현에 더 가깝고 말하기 자연스럽습니다.

from konlpy.tag import Hannanum

hannanum = Hannanum()

class pronounExpression:
    def __init__(self, sentence):
        self.sentence = sentence
        self.analyzed = hannanum.analyze(self.sentence)
        # hannanum.analyze 메소드는 각 어절별 품사와 한국어 품사 태그를 제시합니다.
         # 그 중 대명사의 태그는 인칭대명사 npp 지시대명사 npd입니다. 이를 통해 대명사를 찾습니다.
        self.index = 0
    def getCorrectedeSentence(self):

        resultList = []
        result = '*대명사를 사용하였습니다.----대명사를 삭제했을 때 뜻이 유추 가능하면 삭제를 추천합니다*'
        for i in range(len(self.analyzed)):
            for j in range(len(self.analyzed[i][0])):
                if 'npp' in self.analyzed[i][0][j] or 'npd' in self.analyzed[i][0][j]:
                    self.index+=1
                    resultList.append("%s."%str(self.index)+"%d번째 어절에서 대명사를 사용하셨습니다." %(i + 1))

        if resultList == []:
            return ""
        else:
            for i in range(len(resultList)):
                result += ('\n'+'--->'+resultList[i])
            return result

    def getSuggetstion(self):
        message = """*대명사를 %d번 사용하셨습니다.*
우리말은 뜻을 유추할 수 있으면 대명사를 쓰지 않습니다.
우리말의 구어(口語)에서는 '그'나 '그녀'를 사용하지 않습니다.
그러므로 대명사를 지웠을 때 뜻을 알 수 있으면 삭제하는 것을 권유드립니다."""%self.index
        if self.index == 0:
            message = ""

        return message


if __name__ == '__main__':
    inputSentence = input("문장을 입력하시오 : ")
    k = pronounExpression(inputSentence)
    sol = k.getCorrectedeSentence()
    suggest = k.getSuggetstion()
    print(sol)
    print(suggest)

