n = int(input("Enter number of students: "))

total = 0

for i in range(n):
    print("Enter marks for Student", i + 1)

    sum = 0

    for j in range(5):
        marks = float(input("Enter marks for test " + str(j + 1) + ": "))
        sum = sum + marks

    average = sum / 5
    print("Average of Student", i + 1, "=", average)

    total = total + average

overall_average = total / n

print("Overall average of all students =", overall_average)
