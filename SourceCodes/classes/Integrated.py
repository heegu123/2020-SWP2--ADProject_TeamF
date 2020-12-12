from classes.doublePassiveExpressionClass import doublePassiveExpression
from classes. fromClass import fromClass
from classes.pronounExpressionclass import pronounExpression
from classes.Mark import Mark

class integrated:
    def __init__(self,sentence):
        self.sentence = sentence
        self.fromSentence = fromClass(self.sentence)
        self.pronounExpressionSentence = pronounExpression(self.sentence)
        self.doublePassiveExpressionSentence = doublePassiveExpression(self.sentence)
        self.mark = Mark()
        self.m = self.mark.marking(self.sentence)

    def getPerfectSentence(self):
        self.perfectSentenceList = []

        self.modifiedFromSentence = self.fromSentence.getCorrectedSentence()
        self.perfectSentenceList.append(self.modifiedFromSentence)

        self.modifiedPronounSentence = self.pronounExpressionSentence.getCorrectedeSentence()
        self.perfectSentenceList.append(self.modifiedPronounSentence)

        self.modifiedDoublePassiveExpressionSentence = self.doublePassiveExpressionSentence.getCorrectedSentence()
        self.perfectSentenceList.append(self.modifiedDoublePassiveExpressionSentence)

        result = ''
        for i in range(len(self.perfectSentenceList)):
            if self.perfectSentenceList[i]== '':
                pass
            elif result == '' and self.perfectSentenceList[i]!="":
                result+=self.perfectSentenceList[i]
            elif result!='' and self.perfectSentenceList[i]!="":
                result += ('\n'+'\n'+str(self.perfectSentenceList[i]))
            else:
                pass

        for i in self.m[1]:
            if result != '':
                result += '\n\n'
            result += '*'
            for k in i[1]:
                if i[1].index(k) != 0:
                    result += ','
                result += f" {k}"
            result += f"번째 어절에서 \'{self.mark.checkList[i[0]]['종류']}({self.mark.checkList[i[0]]['출신']} 표현)\'이 사용되었습니다."

        if result == "":
            result = "수정할 표현이 없습니다!"

        return result

    def getSuggestion(self):
        self.suggestionList = []

        self.fromSuggestion = self.fromSentence.getSuggestion()
        self.suggestionList.append(self.fromSuggestion)

        self.pronounSuggestion = self.pronounExpressionSentence.getSuggetstion()
        self.suggestionList.append(self.pronounSuggestion)

        self.doublePassiveExpressionSuggestion = self.doublePassiveExpressionSentence.getSuggestion()
        self.suggestionList.append(self.doublePassiveExpressionSuggestion)

        result2 = ''
        for i in range(len(self.suggestionList)):
            if self.suggestionList[i] == '':
                pass
            elif result2 == '' and self.suggestionList[i] != "":
                result2 += self.suggestionList[i]
            elif result2 != '' and self.suggestionList[i] != "":
                result2 += ('\n' + '\n' + str(self.suggestionList[i]))
            else:
                pass

        for i in self.m[1]:
            if result2 != '':
                result2+= '\n\n'
            result2 += f"* {self.mark.checkList[i[0]]['대체표현']}"

        if result2 == "":
            result2 = "올바른 문장입니다!"

        return result2

if __name__ == '__main__':
    inputSentence = input("문장을 입력하시오 : ")
    #예문 : 잊혀진 철수는 그의 친구로부터 온 편지를 받고 오는 길에 중국으로부터 온 미세먼지를 맞으며 그는 과일가게에서 그의 사과를 샀다.
    k = integrated(inputSentence)
    sol = k.getPerfectSentence()
    j = k.getSuggestion()
    print(sol)
    print()
    print(j)
