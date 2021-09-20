from Question import Question
        
question_summary = [
    "(1) What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "(2) Python is object oriented programming language?\n(a) True\n(b) False\n\n",
    "(3) Who developed the Python language?\n(a) Zim Den\n(b) Guido van Rossum\n(c) Nienevan Rossum\n\n",
    "(4) In which year was the Python language developed?\n(a) 1995\n(b) 1971\n(c) 1989\n\n"
]

questions = [
    Question(question_summary[0], "a"),
    Question(question_summary[1], "a"),
    Question(question_summary[2], "b"),
    Question(question_summary[3], "c")
    
]

def ques_test(questions):
    score = 0
    for question in questions:
        answer = input(question.summary)
        if answer == question.answer:
            score = score+1
    print("You got " + str(score) + "/" + str(len(questions)) + "correct")

ques_test(questions)