from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    # recommended to mention attribute name
    question_bank.append(Question(text=question["text"], answer=question["answer"]))

quiz = QuizBrain(question_bank)

while quiz.has_new_question():
    answers = quiz.next_question()
    quiz.check_answer(answers)

