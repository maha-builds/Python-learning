score=0

for i in range(3):
    question=input("Enter the question: ")
    user_answer=input("Enter the answer: ")

    correct_answer="python"
    correct_answer="java"
    correct_answer="c#"

    if user_answer==correct_answer:
        print("Correct")
        score=score+1
    else:
        print("Wrong")

print(score)
print("Quiz completed!")
