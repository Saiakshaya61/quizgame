
quiz = [
    {"question": "What is the capital of India?", "answer": "Delhi"},
    {"question": "How many legs does a spider have?", "answer": "8"},
    {"question": "What is 5 + 7?", "answer": "12"}
]

score = 0

for item in quiz:
    print(item["question"])
    user_answer = input("Your answer: ").strip()

    if user_answer.lower() == item["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {item['answer']}")

print(f"\nQuiz Over! Your total score is {score} out of {len(quiz)}")
