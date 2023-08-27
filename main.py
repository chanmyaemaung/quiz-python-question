from question_model import Question
from question_data import quiz_questions_list
from quiz_brain import QuizBrain

question_bank = []

for question in quiz_questions_list:
    question_name = question['ask_question']
    answer = question['the_answer']

    new_question = Question(question_name, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz challenge.")
print(f"Your final score was {quiz.score}/{quiz.question_number}")
