def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-----------------------------")
        print(key)
        for i in answers[question_num-1]:
            print(i)

        guess = input("Enter A, B, C, or D: ").upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess) # we compare correct answer to user's guess
        question_num += 1

    display_score(correct_guesses, guesses)


# -----------------------------

def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0
# -----------------------------

def display_score(correct_guesses, guesses):
    print("-----------------------------")
    print("RESULTS")
    print("-----------------------------")

    print("Correct answers: ", end="") # cancel line break
    for i in questions:
        print(questions.get(i)+" ", end="") # display all answers on a single line
    print()

    print("Your guesses: ", end="") 
    for i in guesses:
        print(i+" ", end="")
    print()

# -----------------------------

def play_again():
    pass

# -----------------------------

# a dictionary will contain our questions
questions = {
    "Who created Python? ":"A",
    "What year was Python created? ":"B",
    "Python is tributed to which comedy group? ":"C",
    "Is the Earth round? ":"A"
}

# a 2D list will contain all possible answers 
answers = [
    ["A. Guido Van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
    ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
    ["A. Lonely Island", "B. Smosh", "C. Monthy Python", "D. SNL"],
    ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]
]

new_game()
