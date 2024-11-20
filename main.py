import random

def questions_list(filename):
    with open(filename ,"r") as file:
        return [line.strip().split(';') for line in file]

def Quiz():
    name = input("Input your Name Here: ")
    question_num = int(input("Input Number of Questions Here: "))

    questions = questions_list("questions.txt")
    question_sel = random.sample(questions, question_num)
    score = 0
    for question in question_sel:
        print(f"Question: {question[0]}")
        print(f"A: {question[1]}")
        print(f"B: {question[2]}")
        print(f"C: {question[3]}")
        print(f"D: {question[4]}")
        guess = input("Input Your Guess (A,B,C,D): ")

        if guess == "A" and question[1] == question[5]:
            print("Correct Answer!")
            score+=1

        elif guess == "B" and question[2] == question[5]:
            print("Correct Answer!")
            score+=1

        elif guess == "C" and question[3] == question[5]:
            print("Correct Answer!")
            score+=1

        elif guess == "D" and question[4] == question[5]:
            print("Correct Answer!")
            score += 1

        else:
            print("Incorrect Answer!")

    with open("data.txt","a") as file:
        file.writelines(f"Name: {name}, Score: {score}.")


    print(f"{name} You Scored {score}.")



Quiz()







































