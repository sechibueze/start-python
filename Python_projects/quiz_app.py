questions = [
    "What is the first letter ? \n (a) a \n (b) b \n (c) c \n (d) d",
    "Who created python ? \n (a) Sam  \n (b) Van \n (c) Google \n (d) Bill",
    "Which is an OS ? \n (a) Google \n (b) Microsoft \n (c) Mac \n (d) Python"
]

score = 0
num_of_questions = len(questions)
count = 0
correct_answer = ['a', 'a', 'a']

while count < num_of_questions:
    print(questions[count])
    user_attempt = input("Type the letter that bears your answer : ")

    if user_attempt.lower() == correct_answer[count]:
        # User has answered correctly
        score += 1

    # Next question
    count += 1

print(3 * "*", "Question ended ", 3 * "*")
print("Question score : ", score, "/" , num_of_questions)
