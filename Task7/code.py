
# Attendance Recovery Computation

import math

print("==========================================")
print("       ATTENDANCE RECOVERY SYSTEM")
print("==========================================")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

total_classes = int(input("Enter Total Classes Conducted: "))
attended_classes = int(input("Enter Classes Attended: "))

if total_classes <= 0:
    print("Invalid Total Classes!")
    exit()

if attended_classes < 0 or attended_classes > total_classes:
    print("Invalid Attendance Details!")
    exit()

threshold = float(input("Enter Minimum Attendance Percentage: "))

if threshold <= 0 or threshold > 100:
    print("Invalid Eligibility Percentage!")
    exit()

current_percentage = (attended_classes / total_classes) * 100

print("\n==========================================")
print("          CURRENT ATTENDANCE")
print("==========================================")

print("Student Name:", name)
print("Roll Number:", roll_no)
print("Total Classes:", total_classes)
print("Attended Classes:", attended_classes)
print("Current Attendance:", round(current_percentage, 2), "%")

if current_percentage >= threshold:
    minimum_classes = 0
    print("\nStudent is already eligible!")

else:
    p = threshold / 100

    minimum_classes = math.ceil(
        (p * total_classes - attended_classes) / (1 - p)
    )

    print("\nMinimum Consecutive Classes Required:",
          minimum_classes)

print("\n==========================================")
print("       FUTURE ATTENDANCE SCENARIOS")
print("==========================================")

scenarios = int(input("Enter Number of Future Scenarios: "))

if scenarios <= 0:
    print("Invalid Number of Scenarios!")
    exit()

for i in range(scenarios):

    print("\nScenario", i + 1)

    future_classes = int(
        input("Enter Number of Future Classes: ")
    )

    if future_classes < 0:
        print("Invalid Future Classes!")
        continue

    updated_attended = attended_classes + future_classes
    updated_total = total_classes + future_classes

    future_percentage = (
        updated_attended / updated_total
    ) * 100

    print("Updated Attendance:",
          round(future_percentage, 2), "%")

    if future_percentage >= threshold:
        print("Eligibility Status: ELIGIBLE")
    else:
        print("Eligibility Status: NOT ELIGIBLE")

print("\n==========================================")
print("          FINAL ATTENDANCE REPORT")
print("==========================================")

print("Student Name:", name)
print("Current Attendance:",
      round(current_percentage, 2), "%")

print("Required Attendance:", threshold, "%")

if minimum_classes == 0:
    print("Recovery Classes Required: 0")
    print("Final Status: ELIGIBLE")
else:
    print("Recovery Classes Required:", minimum_classes)
    print("Final Status: NEEDS ATTENDANCE RECOVERY")

print("==========================================")
print("       ATTENDANCE ANALYSIS COMPLETED")
print("==========================================")

