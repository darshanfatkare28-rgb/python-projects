questions = [
    {
        "question": "1. What is the capital of Gujarat?",
        "options": ["A. Ahmedabad", "B. Surat", "C. Gandhinagar", "D. Rajkot"],
        "answer": "C"
    },
    {
        "question": "2. What is the national animal of India?",
        "options": ["A. Lion", "B. Tiger", "C. Elephant", "D. Deer"],
        "answer": "B"
    },
    {
        "question": "3. Which planet is closest to the Sun?",
        "options": ["A. Earth", "B. Mars", "C. Venus", "D. Mercury"],
        "answer": "D"
    },
    {
        "question": "4. What is the brain of a computer?",
        "options": ["A. CPU", "B. Mouse", "C. Keyboard", "D. Monitor"],
        "answer": "A"
    },
    {
        "question": "5. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Chennai", "D. Jaipur"],
        "answer": "B"
    },
    {
        "question": "6. How many days are there in a week?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "7. How many hearts does a human have?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 4"],
        "answer": "A"
    },
    {
        "question": "8. When did India get independence?",
        "options": ["A. 26 January 1950", "B. 15 August 1947",
                    "C. 2 October 1947", "D. 15 August 1950"],
        "answer": "B"
    },
    {
        "question": "9. Which is the largest planet in the Solar System?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "C"
    },
    {
        "question": "10. Which Python function is used to display output?",
        "options": ["A. input()", "B. print()", "C. len()", "D. int()"],
        "answer": "B"
    }
]


def run_quiz():
    score = 0

    print("===== PYTHON QUIZ GAME =====")

    for item in questions:
        print("\n" + item["question"])

        for option in item["options"]:
            print(option)

        answer = input("Enter your answer (A/B/C/D): ").strip().upper()

        if answer == item["answer"]:
            print("Correct answer!")
            score += 1
        else:
            print("Wrong answer!")
            print("Correct answer:", item["answer"])

    print("\n===== QUIZ RESULT =====")
    print("Total Questions:", len(questions))
    print("Correct Answers:", score)
    print("Wrong Answers:", len(questions) - score)
    print("Final Score:", score, "/", len(questions))

    if score >= 8:
        print("Excellent!")
    elif score >= 5:
        print("Good! Keep practicing.")
    else:
        print("Try again!")


run_quiz()