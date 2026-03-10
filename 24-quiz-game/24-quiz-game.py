# 24-quiz-game
# Python learning exercise

# Nested list structure: [question, [options], correct_index]
questions = [
    ["What is the capital of France?", ["London", "Berlin", "Paris", "Madrid"], 2],
    ["Which planet is known as the Red Planet?", ["Venus", "Mars", "Jupiter", "Saturn"], 1],
    ["What is 5 + 7?", ["10", "11", "12", "13"], 2],
    ["Who wrote 'Romeo and Juliet'?", ["Shakespeare", "Dickens", "Austen", "Hemingway"], 0],
    ["What is the largest ocean on Earth?", ["Atlantic", "Indian", "Arctic", "Pacific"], 3]
]

score = 0

for question_data in questions:
    question = question_data[0]
    options = question_data[1]
    correct_index = question_data[2]

    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    user_input = input("Enter your choice (1-4): ")
    try:
        user_choice = int(user_input) - 1
        if user_choice == correct_index:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {options[correct_index]}\n")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.\n")

print(f"Your final score is {score}/{len(questions)}")
