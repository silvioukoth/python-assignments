def run_quiz():
    """Runs a multiple-choice quiz and displays the score."""

    questions = [
        {
            "question": "What is the primary purpose of the 'print()' function in Python?",
            "options": ["To display output to the console", "To read user input", "To perform mathematical calculations", "To define functions"],
            "answer": "To display output to the console",
        },
        {
            "question": "Which movie won the Academy Award for Best Picture in 2020?",
            "options": ["Parasite", "1917", "Joker", "Once Upon a Time in Hollywood"],
            "answer": "Parasite",
        },
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": "Paris",
        },
        {
            "question": "What does RAM stand for?",
            "options": ["Random Access Memory", "Read Only Memory", "Remote Access Module", "Rapid Application Method"],
            "answer": "Random Access Memory"
        }

    ]

    score = 0
    for q in questions:
        print("\n" + q["question"])
        for i, option in enumerate(q["options"]):
            print(f"{i + 1}. {option}")

        user_answer = input("Enter your answer (1, 2, 3, or 4): ")
        try:
            user_answer_index = int(user_answer) - 1
            if q["options"][user_answer_index] == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer is: {q['answer']}")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 4.")

    print(f"\nYour final score is: {score}/{len(questions)}")

def play_again():
    """Asks the user if they want to play again."""
    while True:
        play_again_input = input("Do you want to play again? (yes/no): ").lower()
        if play_again_input == "yes":
            return True
        elif play_again_input == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Main game loop
while True:
    run_quiz()
    if not play_again():
        break

print("Thanks for playing!")



# # 
# def run_quiz_simple():
#     questions = [
#         ["What is the primary purpose of 'print()' in Python?", "Display output", "Read input", "Math", "Functions", "Display output"],
#         ["Best Picture 2020?", "Parasite", "1917", "Joker", "Hollywood", "Parasite"],
#         ["Capital of France?", "Berlin", "Madrid", "Paris", "Rome", "Paris"]
#     ]

#     score = 0
#     for q in questions:
#         print("\n" + q[0])
#         for i in range(1, 5):
#             print(f"{i}. {q[i]}")

#         user_answer = input("Enter your answer (1, 2, 3, or 4): ")
#         try:
#             user_answer_index = int(user_answer)
#             if q[user_answer_index] == q[5]:
#                 print("Correct!")
#                 score += 1
#             else:
#                 print(f"Incorrect. The correct answer is: {q[5]}")
#         except (ValueError, IndexError):
#             print("Invalid input.")

#     print(f"\nYour final score is: {score}/{len(questions)}")

# # ... (play_again function and main loop remain the same)
# # 