class Question:

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def show_question(self):
        print(self.question)

    def is_correct_answer(self, user_attempt):
        return user_attempt.lower() == self.correct_answer


class Quiz:

    score = 0

    def __init__(self):
        print("Quz started ....'")

    def calculate_score(self, user_score):
        print("Quiz ended ...")
        print("Total score : ", user_score)

# create questions from quiz dataset
questions = [
    Question("What is the first letter ? \n (a) a \n (b) b \n (c) c \n (d) d", "a"),
    Question("Who created python ? \n (a) Sam  \n (b) Van \n (c) Google \n (d) Bill", "a"),
    Question("Which is an OS ? \n (a) Google \n (b) Microsoft \n (c) Mac \n (d) Python", "a")
]

count = 0
score = 0
quiz = Quiz()
while count < len(questions):
    Current_question = questions[count]
    Current_question.show_question()
    user_attempt = input("Type answer : ")

    if Current_question.is_correct_answer(user_attempt) :
        score += 1

    if count == len(questions) - 1:
        quiz.calculate_score(score)

    count += 1

print("Thank you : ")
