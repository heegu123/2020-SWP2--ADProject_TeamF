# 번역투의 문제점 : 우리말에 부자연스러운 외국어 어순과 어법을 우리말처럼 둔갑시키면 우리말이 파괴됩니다.
#               번역투는 무슨 말인지는 알겠지만 깔끔한 문장이라고 느끼기엔 무리가 있습니다.
#               사용자가 작성한 문장이 깔끔한 문장인지 알아보기위해 이 프로그램을 고안하였습니다.

#               이 파일은 그 중 영어단어 'from' 번역투인 '~로 부터' 교정하기 위해 작성되었습니다.
from konlpy.tag import Hannanum

hannanum = Hannanum()

class fromClass:
    def __init__(self, sentence):
        """
        <예문>
        1. 한강으로부터 10미터 떨어진
        2. 너에게로부터 온 편지
        3. 중국으로부터 온 응답
        """
        self.sentence = sentence
        self.analyzed = hannanum.morphs(self.sentence)
        self.index = 0

    def getCorrectedSentence(self):
        fromExpressionList = []
        result = '*영어 번역투(from체)를 사용하셨습니다.*'
        for i in range(len(self.analyzed)):
            if self.analyzed[i][len(self.analyzed[i]) - 3: len(self.analyzed[i])] == "로부터":
                self.index+=1
                fromExpressionList.append("%s."%str(self.index)+"%d번째 어절에 from 번역투(~(으)로 부터) 사용" % (i + 1))
        if fromExpressionList == []:
            return ''
        else:
            for i in range(len(fromExpressionList)):
                result += ('\n'+'--->'+fromExpressionList[i])
            return result

    def getSuggestion(self):
        if self.index != 0:
            return """*'~(으)로 부터'표현을 %d번 사용하셨습니다.*
'~(으)로 부터'표현은 영어'from' 또는 일본어 '~から'의 번역투로 널리 쓰이는 번역체입니다.
앞말이 유정명사이면  '~에게서/~한테서/~께서'라는 우리말 표현으로,
앞말이 무정명사라면 '~에서'라는 우리말로 수정할 것을 권유해드립니다. """%self.index
        elif self.index == 0 :
            return ""

if __name__ == '__main__':
    inputSentence = input("문장을 입력하시오 : ")
    k = fromClass(inputSentence)
    sol = k.getCorrectedSentence()
    suggest = k.getSuggestion()
    print(sol)
    print(suggest)
