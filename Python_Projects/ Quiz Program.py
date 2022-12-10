quiz = {
    "question1":{"question":"What is the capital of France? ", "answer": "Paris"},
    "question2":{"question":"What is the capital of Japan? ", "answer": "Tokyo"},
    "question3":{"question":"What is the capital of Taiwan? ", "answer": "Taipei"},
    "question4":{"question":"What is the capital of Canada? ", "answer": "Outtawa"},
    "question5":{"question":"What is the capital of Germany? ", "answer": "Berlin"},
    "question6":{"question":"What is the capital of New Taipei? ", "answer": "Banqiao"},
}

score = 0
for key,value in quiz.items():
    print(value["question"])
    answer = input("enter your answer? ")
    
    if answer.lower() == value["answer"].lower():
        print("Correct")
        score+=1
        print("You got "+ str(score))
    else:
        print("Wrong")
        print("The answer is: "+ value["answer"])
        print("")
print("You got "+ str (score)+ " correctly")
print("You got "+str(score)+ "out of 7")
print("Your percentage is "+ str(int(score/7*100))+"%")