class QuizBrain:
    def __init__(self,q_list):
        self.question_number=0
        self.score=0
        self.question_list=q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        '''

        prints the (self.question_number)th index question of the question list passed during creating quiz brain

        '''
        current_question=self.question_list[self.question_number]
        self.question_number += 1
        user_ans=input(f"Q.{self.question_number} {current_question.text} ? (True/False)").lower()
        self.check_score(user_ans,current_question.answer)


    def check_score(self,user_ans,corr_ans):
       if user_ans.lower()==corr_ans.lower():
            print("You got it right")
            self.score+=1
       else:
           print("you got that wrong")
       print(f"the correct answer was {corr_ans}")
       print(f"Your current score is : {self.score}/{self.question_number}")
       print("\n")
