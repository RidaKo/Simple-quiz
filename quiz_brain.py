class QuizBrain:
    def __init__(self, question_bank: list) -> None:
        self.question_number = 0
        self.all_questions = question_bank
        self.score = 0

    def ask_question(self, question_number: int,  all_questions: list) -> None:
        question = self.all_questions[self.question_number]
        self.question_number += 1
        
        self.check_answer(input(f"Q{self.question_number} {question.text}. True or False? :"), question.answer)
        
    def still_has_questions(self) -> bool:
        return self.question_number < len(self.all_questions)

    def check_answer(self, user_answer, correct_answer, ):
        if correct_answer.lower() == user_answer.lower():
            print("You got it right. Good job.")
            self.score +=1
        else:
            print("wrong")
        print(f"The correct answer is {correct_answer}, Your score is {self.score}")
        print("/n")
