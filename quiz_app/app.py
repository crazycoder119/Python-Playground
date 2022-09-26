# dictionary of questions
# Player score

quiz = {
    "question1":{
        "quiz": "10/2 equals to :",
        "answers" : [2,3,4,5],
        "correct_answer" : 5
    },
    "question2":{
            "quiz": "4/2 equals to :",
            "answers" : [2,3,4,5],
            "correct_answer" : 2
    }
}

print("Welcome to quiz game........")
score = 0
game_continue = True
for key,value in quiz.items():
    if game_continue:
        print(value["quiz"],)
        print(value["answers"], "\nEnter the correct answer :")
        answer = int(input())
        if answer == value["correct_answer"]:
            score +=10
            print("That is correct answer")
        else :
            print("That is incorrect ")
        game_continue = input('Do you want to continue? (y/n): ').lower().strip() == 'y'
    else:
        break
print("Score is : ", score)