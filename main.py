from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []
for dic in question_data:
    question_bank.append(Question(dic["question"], dic["correct_answer"]))

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_questions():
    quiz_brain.ask_question(quiz_brain.question_number, quiz_brain.all_questions)
print(f"You have completed the quiz, your score is {quiz_brain.score}/{quiz_brain.question_number}")