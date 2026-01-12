#1- Create list of question dictionaries
#   - each has question text, options, correct answer
#2- Define run_quiz function
#   -Set score to 0
#   -Loop through questions-For each question in questions:
#     -Display question and options
#     -Get user input
#     -While input is not A, B,C, or D:
#       -Prompt user to enter valid option
#     -If input matches correct answer:
#       -Increment score by 1
#       -print correct
#     -Else:
#       -print incorrect and show correct answer
#  -Calculate percentage
#  -Print final score and personalized message
#3- Call run_quiz function to start quiz
questions = [
    {
        "question": "What is the capital of France?",
        "options": [
            "A: Berlin",
            "B: Madrid",
            "C: Paris",
            "D: Rome"
        ],
        "answer": "C"
    },
    {
        "question": "What is 2 + 2?",
        "options": [
            "A: 3",
            "B: 4",
            "C: 5",
            "D: 6"
        ],
        "answer": "B"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": [
            "A: Earth",
            "B: Mars",
            "C: Jupiter",
            "D: Saturn"
        ],
        "answer": "C"
    }
]  

def run_quiz(list_of_questions):    
    score = 0
    print("Welcome to the quiz!")
    print("Choose your answer by entering A, B, C, or D.\n")
    total_questions = len(list_of_questions)
    
    for i, q in enumerate(list_of_questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q["options"]:
            print(option)
        
        user_answer = input("Your answer (A, B, C, or D): ").upper()

        if user_answer == q["answer"]:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {q['answer']}.")
        
    print(f"You got {score} out of {total_questions} questions correct!")

run_quiz(questions)
        
        
    