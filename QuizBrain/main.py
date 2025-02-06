from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for ques in question_data:
    question_text=ques["question"]
    question_ans=ques["correct_answer"]
    new_question=Question(question_text,question_ans)
    question_bank.append(new_question)

print(question_bank)
quiz=QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
print("You've completed the quiz")
print(f"Your final  score was : {quiz.score}/{quiz.question_number}")
