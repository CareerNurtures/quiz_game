class questionBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
        self.user_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"\nQ{self.question_number} : {current_question.text} (True/False) : ").capitalize()
        self.check_ans(user_ans, current_question.answer)

    def check_ans(self,user_ans,current_ans):

        if user_ans == current_ans:
            self.user_score += 1
            print("Yes Your are right..!")
        else:
            print(f"oops! that is wrong answer and correct answer was '{current_ans}'")

        print(f"Your score is {self.user_score}/{self.question_number}")
        if self.question_number == len(self.question_list):
            print("\n You've completed the quiz")
            print(f"And your total score is {self.user_score}/{len(self.question_list)}")





