assignments = ["dbms", "dsa", "pai", "se"]
print("Assignments:", assignments)
new_assignment = input("Enter a new assignment: ")
assignments.append(new_assignment)
completed_assignment = input("Enter the completed assignment: ")
if completed_assignment in assignments:
    assignments.remove(completed_assignment)
else:
    print("Assignment not found.")
print("Updated Assignments:")
for assignment in assignments:
    print(assignment)
