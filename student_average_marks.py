# Python program to read student information from a file
# and calculate average marks

# Opening the input file
file = open("students.txt", "r")

total_marks = 0
count = 0

print("Student Information:\n")

# Reading file line by line
for line in file:
    data = line.strip().split(",")

    name = data[0]
    age = data[1]
    marks = int(data[2])

    print("Name:", name)
    print("Age:", age)
    print("Marks:", marks)
    print()

    total_marks += marks
    count += 1

file.close()

# Calculating average
average = total_marks / count

# Writing average to a new file
output_file = open("average.txt", "w")

output_file.write("Average Marks = " + str(average))

output_file.close()

print("Average marks stored in average.txt")
