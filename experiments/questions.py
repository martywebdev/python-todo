import json

questions = "questions.json"

with open(questions, 'r') as f:
    content = f.read()

data = json.loads(content)

score = 0

for question in data:
    print(question["question"])
    for index, item in enumerate(question["selections"]):
        print(f"{index + 1}-{item}")
    answer = input("Answer ")
    if answer.isdigit() and int(answer) == question["answer"]:
        print("correct")
        score += 1
    else:
        print(f"wrong, correct answer: {question['answer']}")

print(score)