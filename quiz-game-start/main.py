from data import question_data
from question_model import Question
import random
from quiz_brain import QBrain

qbank = []
for i in question_data :
    txt = i["text"]
    answer = i["answer"]
    qnew = Question(txt,answer)
    qbank.append(qnew)
    
quiz = QBrain(qbank)
qrem = quiz.qrem()

while qrem == True :
    quiz.nextQues()
    
print("You have Completed the quiz !")
print(f"Your FinalScore is : {quiz.score}/{quiz.qnum}")
