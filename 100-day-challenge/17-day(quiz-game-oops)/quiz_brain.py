class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_bank = question_bank

    def next_question(self):
        question = self.question_bank[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{str(self.question_number)}: {question.text} (True/False)?:")
        return [user_answer, question.answer]

    def check_answer(self, answers):
        if answers[0] == answers[1]:
            self.score += 1
            print("You're right")
        else:
            print("You gave an incorrect answer")

        print(f"Your score is: {self.score}/{self.question_numbert}\n")

    def has_new_question(self):
        return self.question_number < len(self.question_bank)
