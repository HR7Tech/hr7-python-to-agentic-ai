from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain

question_bank = []

for quest in question_data:
    new_question = Question(quest["text"],quest["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()
else:
    print("You have completed the quiz.!")
    print(f"Your final score is {quiz.score}/{quiz.question_num}")


