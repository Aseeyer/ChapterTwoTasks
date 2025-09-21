# Computer-Assisted Instruction: Reducing Student Fatigue
import random


def ask_question():
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    correct_answer = num1 * num2

    correct_responses = [
        "Very good!",
        "Excellent!",
        "Nice work!",
        "Keep up the good work!"
    ]

    wrong_responses = [
        "No. Please try again.",
        "Wrong. Try once more.",
        "Don't give up!",
        "No. Keep trying."
    ]

    while True:
        answer = int(input(f"How much is {num1} times {num2}? "))

        if answer == correct_answer:
            print(random.choice(correct_responses))
            break
        else:
            print(random.choice(wrong_responses))


ask_question()
