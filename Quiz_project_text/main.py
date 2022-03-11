

from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_list = []
for i in question_data:
    question = i["question"]
    answer = i["correct_answer"]
    all_question = Question(question,answer)
    question_list.append(all_question)

# to access the data from Question object we print
#print(question_list[0].answer)


quiz = QuizBrain(question_list)

while quiz.still_has_question():
    quiz.next_question()

print("you have completed the Quiz")
print(f"you finall score was {quiz.score}/{len(question_list)}")



