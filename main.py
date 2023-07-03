from data import question_data
from question_model import Questions
from quiz_brain import questionBrain

question_bank = []

for question in question_data:
    question_text = question["question"]
    question_ans = question["correct_answer"]
    new_questions = Questions(question_text,question_ans)
    question_bank.append(new_questions)

question = questionBrain(question_bank)

while question.still_has_questions():
    question.next_question()

print("\nYou've completed the quiz")
print(f"And your total score is {question.user_score}/{len(question.question_list)}")
