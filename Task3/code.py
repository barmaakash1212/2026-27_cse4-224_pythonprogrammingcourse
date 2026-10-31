
# Hospital Billing and Patient Classification System

print("======================================")
print(" HOSPITAL BILLING MANAGEMENT SYSTEM")
print("======================================")

name = input("Enter patient name: ")
age = int(input("Enter patient age: "))

print("\nPatient Categories:")
print("1. General")
print("2. Senior Citizen")
print("3. Student")
print("4. BPL")

category = input("Enter patient category: ").strip().lower()

if age <= 0 or age > 120:
    print("Invalid age!")
    exit()

valid_categories = [
    "general",
    "senior citizen",
    "student",
    "bpl"
]

if category not in valid_categories:
    print("Invalid patient category!")
    exit()

print("\nEnter Hospital Charges")

consultation = float(input("Consultation charges: Rs. "))
diagnostic = float(input("Diagnostic charges: Rs. "))
treatment = float(input("Treatment charges: Rs. "))

if consultation < 0 or diagnostic < 0 or treatment < 0:
    print("Invalid billing! Charges cannot be negative.")
    exit()

total_bill = consultation + diagnostic + treatment

if category == "senior citizen":
    if age < 60:
        print("Invalid category: Senior citizen must be 60 or above.")
        exit()
    concession_rate = 10

elif category == "student":
    concession_rate = 5

elif category == "bpl":
    concession_rate = 20

else:
    concession_rate = 0

concession = total_bill * concession_rate / 100

final_bill = total_bill - concession

if final_bill < 1000:
    classification = "Low Payment"

elif final_bill <= 5000:
    classification = "Medium Payment"

else:
    classification = "High Payment"

# Display bill
print("\n======================================")
print("          HOSPITAL BILL")
print("======================================")

print("Patient Name       :", name)
print("Patient Age        :", age)
print("Patient Category   :", category.title())

print("--------------------------------------")
print("Consultation Charge: Rs.", consultation)
print("Diagnostic Charge  : Rs.", diagnostic)
print("Treatment Charge   : Rs.", treatment)

print("--------------------------------------")
print("Total Bill         : Rs.", round(total_bill, 2))
print("Concession Rate    :", concession_rate, "%")
print("Concession Amount  : Rs.", round(concession, 2))
print("Final Payable      : Rs.", round(final_bill, 2))

print("--------------------------------------")
print("Patient Class      :", classification)

print("======================================")
print("       BILLING COMPLETED")
print("======================================")

