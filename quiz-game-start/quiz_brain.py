from data import question_data

class QBrain :
    
    def __init__(self,qlist):
        self.qnum = 0
        self.questionList = qlist
    
    def qrem(self) :
        qr = True
        length = len(self.questionList)
        if self.qnum < length :
            qr = True
            return qr
        elif self.qunm >= length :
            qr = False
            return qr
    def nextQues(self) :
        cques = self.questionList[self.qnum]
        uchoice = input(f"Q.{self.qnum}: {cques.text} \nEnter your answer (True/False) : ").lower()
        self.qnum +=1  
        self.check(uchoice , cques.answer)
        
    def check(self,uchoice,crct) :
        self.score = 0
        if uchoice == crct.lower() :
            print("You got the Correct Answer")
            self.score += 1
            print("\n") 
        
        else :
            print("You got the Wrong Answer")
            print(f"Your score is : {self.score}")
            print("\n")