from single_linked_list import SingleLinkedList, Node
from colorama import Fore, Style, init
init()

def printf(string, end="\n"):
    with open("output.txt", "a") as file:
        file.write(string + end)


theoretical_questions = SingleLinkedList()
theoretical_questions.from_list([
    "Question 1",
    "Question 2",
    "Question 3",
    "Question 4",
    "Question 5",
])

practical_questions = SingleLinkedList()
practical_questions.from_list([
    "Question 1",
    "Question 2",
    "Question 3",
    "Question 4",
    "Question 5",
])

answers_to_practical_questions = SingleLinkedList()
answers_to_practical_questions.from_list([
    False,
    True,
    False,
    True,
    False,
])

answers_to_theoretical_questions = SingleLinkedList()
answers_to_theoretical_questions.from_list([
    False,
    True,
    False,
    True,
    False,
])


# Get student list 
students = SingleLinkedList() 
students.from_list([
    "Student 1",
    "Kolosov Ihor",
    "Pedko Mykyra",
    "Vladislav Bakunets",
    "Student 5",
    "Student 6",
    "Student 7",
    
])


# General order of students 
order = SingleLinkedList()

print(Fore.GREEN, "[Students]: ", Fore.RESET)
printf("[Students]: ")
for student in students:
    print(student.value)


# calculate max grade 
max_grade = 4
print(Fore.GREEN, "[Exam]: ", Fore.RESET)
printf("[Exam]: ")
for stage in [0, 1]: # Two stages 
    # theoretical
    print(" <> Theoretical Stage ")
    printf(" <> Theoretical Stage ")
    old_question_str = ""
    for i, student in enumerate(students):
        # Keep track which student answered
        true_answer = answers_to_theoretical_questions[i % len(answers_to_theoretical_questions)].value
        order.append({"student": student, 
                "true_answer": true_answer})

        question = theoretical_questions[i % len(theoretical_questions)]
        #  при чому частина умови завдання отримується у попереднього студент
        student.answer(question.value + old_question_str, true_answer)
        old_question_str = question.value[:2]
    order.append(None) # End of stage  
    
    # practical 
    print(" <> Practical Stage ")
    printf(" <> Practical Stage ")
    for i, student in enumerate(students):
        true_answer = answers_to_practical_questions[i % len(answers_to_practical_questions)].value
        order.append({"student": student, 
                "true_answer": true_answer})

        question = practical_questions[i % len(practical_questions)]
        student.answer(question.value, true_answer)
    order.append(None) # End of stage


print(Fore.GREEN, "[Order of students for exam]: ", Fore.RESET)
printf("[Order of exam]: ")
for element in order:
    if element.value:
        student = element.value["student"]
        student_index = students.index_of(lambda x: x == student)
        print(student_index, end=" -> ")
        printf(f"{student_index}", end=" -> ")
    else:
        printf("End of stage")
        print("End of stage")

print(Fore.GREEN, "[Exam Results]: ", Fore.RESET)
print("[Exam Results]: ")
for element in order:
    if element.value:
        student = element.value["student"]
        student_index = students.index_of(lambda x: x == student)
        print(f" score: {student.score}/{max_grade} | {student_index} {student.value} ")
        printf(f" score: {student.score}/{max_grade} | {student_index} {student.value} ")

print(Fore.GREEN, "All done, check output.txt file", Fore.RESET)
