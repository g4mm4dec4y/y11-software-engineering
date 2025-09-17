max = 100
num_students = 0
# Define an empty list to store all the values
mark_list = []
# Using int to ensure the input isn't interpreted as a string
mark = int(input("Input mark: "))
while mark != 999:
# Program checks for sentinel and then appends mark to the list
    mark_list.append(mark)
    if mark > max:
        max = mark
# Program is already keeping track of the number of students which is handy
    num_students = num_students + 1
# Ensuring the input isn't interpreted as a string
    mark = int(input("Input mark: "))
# This time the average is properly calculated by taking all the marks given to the program and dividing by the counter.
average = sum(mark_list)/num_students
print("\nResults\nMaximum mark:", max, "\nAverage mark:", average, "\n")