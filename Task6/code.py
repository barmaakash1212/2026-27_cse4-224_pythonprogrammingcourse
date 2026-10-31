
# Examination Result and Grace-Mark Validation

print("==========================================")
print(" EXAMINATION RESULT MANAGEMENT SYSTEM")
print("==========================================")

MAX_MARKS = 100
PASS_MARKS = 35
MAX_GRACE = 5

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

n = int(input("Enter Number of Subjects: "))

if n <= 0:
    print("Invalid number of subjects!")
    exit()

subjects = []
total_marks = 0
all_passed = True

for i in range(n):

    print("\nSubject", i + 1)

    subject = input("Enter Subject Name: ")
    marks = float(input("Enter Marks Obtained: "))

    if marks < 0 or marks > MAX_MARKS:
        print("Invalid marks! Enter marks between 0 and 100.")
        exit()

    grace = 0

    if marks >= PASS_MARKS:
        status = "PASS"

    elif marks >= 30:
        required_grace = PASS_MARKS - marks

        if required_grace <= MAX_GRACE:
            grace = required_grace
            marks = min(marks + grace, MAX_MARKS)
            status = "PASS"
        else:
            status = "FAIL"

    else:
        status = "FAIL"

    if status == "FAIL":
        all_passed = False

    subjects.append({
        "name": subject,
        "marks": marks,
        "grace": grace,
        "status": status
    })

    total_marks += marks

maximum_total = n * MAX_MARKS
percentage = (total_marks / maximum_total) * 100

if not all_passed:
    result = "FAIL"
    classification = "No Classification"

elif percentage >= 75:
    result = "PASS"
    classification = "Distinction"

elif percentage >= 60:
    result = "PASS"
    classification = "First Class"

elif percentage >= 50:
    result = "PASS"
    classification = "Second Class"

else:
    result = "PASS"
    classification = "Third Class"

print("\n==========================================")
print("          STUDENT RESULT SHEET")
print("==========================================")

print("Student Name :", name)
print("Roll Number  :", roll_no)

print("------------------------------------------")
print("Subject      Marks   Grace   Status")
print("------------------------------------------")

for sub in subjects:
    print(
        f"{sub['name']:<12}"
        f"{sub['marks']:<8.1f}"
        f"{sub['grace']:<8.1f}"
        f"{sub['status']}"
    )

print("------------------------------------------")
print("Total Marks :", round(total_marks, 2), "/", maximum_total)
print("Percentage  :", round(percentage, 2), "%")
print("Final Result:", result)
print("Classification:", classification)

print("==========================================")
print("       RESULT PROCESSING COMPLETED")
print("==========================================")

