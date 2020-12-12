import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

from classes.Integrated import integrated
from HelpMessages import whyWeMadeMessage, howToUseMessage

class helpDialog(QDialog): # 사용법 윈도우
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(850,100,400,600)
        self.setWindowTitle("How to Use")

        #개발목적 소개
        self.box0 = QHBoxLayout()

        self.label1 = QLabel("개발 목적 : ")
        self.purposeMessage = QLabel(whyWeMadeMessage)

        self.box0.addWidget(self.label1)
        self.box0.addWidget(self.purposeMessage)

        #사용방법 설명
        self.box1  = QHBoxLayout()

        self.label2 = QLabel("사용 방법 : ")
        self.howMessage = QLabel(howToUseMessage)

        self.box1.addWidget(self.label2)
        self.box1.addWidget(self.howMessage)

        #ok버튼 - 사용법 창 나가기버튼
        self.box2 = QHBoxLayout()

        self.okButton = QPushButton("OK")
        self.okButton.clicked.connect(self.pushButtonClicked)

        self.box2.addStretch()
        self.box2.addWidget(self.okButton)
        self.box2.addStretch()

        #사용법 창 메인 레이아웃
        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.box0)
        self.vbox.addStretch(1)
        self.vbox.addLayout(self.box1)
        self.vbox.addStretch(2)
        self.vbox.addLayout(self.box2)

        self.setLayout(self.vbox)

    def pushButtonClicked(self):
        self.close()

class sentence_corrector(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.vBox = QVBoxLayout()

        self.titleLabel = QLabel("AD프로젝트 F조 문장 교정기")

        self.helpButton = QToolButton()
        self.helpButton.setText("도움말")
        self.helpButton.clicked.connect(self.helpButtonClicked)

        self.titleBox = QHBoxLayout()

        self.titleBox.addStretch()
        self.titleBox.addWidget(self.titleLabel)
        self.titleBox.addStretch()
        self.titleBox.addWidget((self.helpButton))

        #input Sentence
        self.startLabel = QLabel("수정할 문장 :")

        self.sentenceEdit = QLineEdit()
        self.sentenceEdit.setAlignment(Qt.AlignRight)

        self.startButton = QToolButton()
        self.startButton.setText("Start")
        self.startButton.clicked.connect(self.buttonClicked)

        self.hbox0 = QHBoxLayout()

        self.hbox0.addWidget(self.startLabel)
        self.hbox0.addWidget(self.sentenceEdit)
        self.hbox0.addWidget(self.startButton)


        #Unnatural Expression장
        self.UNELabel = QLabel("수정할 표현 :")
        self.UNE_Edit = QTextEdit()
        self.UNE_Edit.setReadOnly(True)
        self.hbox1 = QHBoxLayout()

        self.hbox1.addWidget(self.UNELabel)
        self.hbox1.addWidget(self.UNE_Edit)

        #Suggetion
        self.suggestionLabel = QLabel("이렇게 수정 :")
        self.SuggestionEdit = QTextEdit()
        self.SuggestionEdit.setReadOnly(True)
        self.hbox2 = QHBoxLayout()

        self.hbox2.addWidget(self.suggestionLabel)
        self.hbox2.addWidget(self.SuggestionEdit)

        self.vBox.addLayout(self.titleBox)
        self.vBox.addLayout(self.hbox0)
        self.vBox.addLayout(self.hbox1)
        self.vBox.addLayout(self.hbox2)

        self.setLayout(self.vBox)
        self.setGeometry(200, 100, 600, 800)
        self.setWindowTitle('Sentence Corrector')
        self.show()


    def buttonClicked(self):
        button = self.sender().text()

        if button == 'Start':
            beforeSentence = self.sentenceEdit.text()
            #예문 : 잊혀진 철수는 그의 친구로부터 온 편지를 받고 오는 길에 중국으로부터 온 미세먼지를 맞으며 그는 과일가게에서 그의 사과를 샀다.

            sentence = integrated(beforeSentence)
            result = sentence.getPerfectSentence()
            self.UNE_Edit.setText(result)
            result2 = sentence.getSuggestion()
            self.SuggestionEdit.setText(result2)


    def helpButtonClicked(self):
        helpWindow = helpDialog()
        helpWindow.exec_()


if __name__=='__main__':
    app = QApplication(sys.argv)
    ex = sentence_corrector()
    sys.exit(app.exec_())


