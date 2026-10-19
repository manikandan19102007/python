class Node:
    def __init__(self, key, question, options, answer):
        self.key = key
        self.question = question
        self.options = options
        self.answer = answer
        self.left = None
        self.right = None
 
 
def insert(root, key, question, options, answer):
    if root is None:
        return Node(key, question, options, answer)
 
    if key < root.key:
        root.left = insert(root.left, key, question, options, answer)
    elif key > root.key:
        root.right = insert(root.right, key, question, options, answer)
 
    return root
 
 
def search(root, key):
    if root is None:
        return None
 
    if key == root.key:
        return root
    elif key < root.key:
        return search(root.left, key)
    else:
        return search(root.right, key)
 
 
root = None
 
root = insert(
    root, 3,
    "Which keyword is used to define a function in Python?",
    ["A. func", "B. def", "C. function", "D. define"],
    "B"
)
 
root = insert(
    root, 1,
    "Which data structure stores data in key-value pairs?",
    ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
    "C"
)
 
root = insert(
    root, 5,
    "Which symbol is used to write comments in Python?",
    ["A. //", "B. /", "C. #", "D. --"],
    "C"
)
 
root = insert(
    root, 2,
    "Which function is used to display output in Python?",
    ["A. display()", "B. print()", "C. show()", "D. output()"],
    "B"
)
 
root = insert(
    root, 4,
    "Which data structure is ordered and changeable?",
    ["A. Tuple", "B. Set", "C. List", "D. String"],
    "C"
)
 
print("=" * 45)
print("      PYTHON QUIZ GAME")
print("    Using Binary Search Tree")
print("=" * 45)
 
score = 0
total_questions = 5
 
for question_id in range(1, total_questions + 1):
    question = search(root, question_id)
 
    if question is not None:
        print("\nQuestion", question_id)
        print(question.question)
 
        for option in question.options:
            print(option)
 
        answer = input("Enter your answer (A/B/C/D): ").upper()
 
        if answer == question.answer:
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", question.answer)
 
print("\n" + "=" * 45)
print("        QUIZ RESULT")
print("=" * 45)
print("Total Questions :", total_questions)
print("Correct Answers :", score)
print("Wrong Answers :", total_questions - score)
print("Final Score :", score, "/", total_questions)
 
if score == total_questions:
    print("Excellent! All answers are correct!")
elif score >= 3:
    print("Good job! Keep practicing.")
else:
    print("Keep learning and try again!")
 
print("=" * 45)
