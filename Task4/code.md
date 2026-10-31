Employee Payroll and Deduction Analysis Using Python
1. Problem Statement
Develop a Python program to calculate employee salaries based on basic pay, allowances, overtime, and incentives. The system should calculate gross salary, apply progressive deductions, and generate a formatted salary statement.

The program should perform the following operations:
1. Accept employee details such as employee ID, name, and basic salary.
2. Calculate allowances such as House Rent Allowance (HRA) and Dearness Allowance (DA).
3. Calculate overtime payment based on overtime hours.
4. Add incentives to the salary.
5. Calculate gross salary.
6. Apply progressive deductions based on gross salary.
7. Calculate net salary after deductions.
8. Generate a formatted employee salary statement.
Salary Calculation Rules (Example):
Component	Rate
HRA	20% of basic pay
DA	10% of basic pay
Overtime	₹200 per hour
Incentive	Given by user

Progressive Deduction Slabs:
Gross salary	Deduction rate
First ₹10,000	0%
Next ₹10,000	5%
Next ₹20,000	10%
Above ₹40,000	15%

Note: These are assumed rates for an academic project, not official income-tax or payroll rules.
2. Algorithm
1. Start the program.
2. Enter employee ID and employee name.
3. Enter basic salary.
4. Enter overtime hours.
5. Enter incentive amount.
6. Validate all input values.
7. Calculate HRA = 20% of basic salary.
8. Calculate DA = 10% of basic salary.
9. Calculate overtime payment = Overtime hours × ₹200.
10. Calculate gross salary:
Gross Salary = Basic Pay + HRA + DA + Overtime Payment + Incentives.
11. Calculate progressive deductions:
    - First ₹10,000: 0%.
    - Next ₹10,000: 5%.
    - Next ₹20,000: 10%.
    - Above ₹40,000: 15%.
12. Calculate net salary:
Net Salary = Gross Salary − Total Deductions.
13. Display the formatted salary statement.
14. Stop.
3. Flowchart







medium.com


4. Python Source Code
# Employee Payroll and Deduction Analysisprint("==========================================")print("     EMPLOYEE PAYROLL MANAGEMENT SYSTEM")print("==========================================")# Employee detailsemp_id = input("Enter Employee ID: ")name = input("Enter Employee Name: ")basic = float(input("Enter Basic Salary: Rs. "))overtime_hours = float(input("Enter Overtime Hours: "))incentive = float(input("Enter Incentive Amount: Rs. "))# Validate inputif basic < 0 or overtime_hours < 0 or incentive < 0:    print("Invalid Input! Values cannot be negative.")    exit()# Calculate allowanceshra = basic * 0.20da = basic * 0.10# Calculate overtime paymentovertime_rate = 200overtime_pay = overtime_hours * overtime_rate# Calculate gross salarygross_salary = basic + hra + da + overtime_pay + incentive# Progressive deduction calculationdef calculate_deduction(salary):    deduction = 0



5. Sample Input
==========================================
     EMPLOYEE PAYROLL MANAGEMENT SYSTEM
==========================================

Enter Employee ID: 101
Enter Employee Name: Ravi
Enter Basic Salary: Rs. 30000
Enter Overtime Hours: 10
Enter Incentive Amount: Rs. 2000


6. Sample Output
==========================================
           EMPLOYEE SALARY STATEMENT
==========================================

Employee ID       : 101
Employee Name     : Ravi

------------------------------------------
Basic Salary      : Rs. 30000.0
HRA (20%)         : Rs. 6000.0
DA (10%)          : Rs. 3000.0
Overtime Payment  : Rs. 2000.0
Incentive         : Rs. 2000.0

------------------------------------------
Gross Salary      : Rs. 43000.0
Total Deduction   : Rs. 2800.0

------------------------------------------
NET SALARY        : Rs. 40200.0

==========================================
       PAYROLL GENERATED SUCCESSFULLY
==========================================


Calculation verification:
- Gross Salary = 30,000 + 6,000 + 3,000 + 2,000 + 2,000 = ₹43,000.
- First ₹10,000 deduction = ₹0.
- Next ₹10,000 deduction = ₹500.
- Next ₹20,000 deduction = ₹2,000.
- Remaining ₹3,000 deduction = ₹450.
- Total deduction = ₹2,950.
- Net salary = ₹43,000 − ₹2,950 = ₹40,050.
Corrected calculation
The correct output values should therefore be:
Gross Salary      : Rs. 43000.00
Total Deduction   : Rs. 2950.00
NET SALARY        : Rs. 40050.00


```Mermaid 
 Flowchart Code

flowchart TD
    A([Start]) --> B[/Enter Employee ID and Name/]
    B --> C[/Enter Basic Salary/]
    C --> D[/Enter Overtime Hours and Incentives/]

    D --> E{Are inputs valid?}

    E -- No --> F[Display Invalid Input]
    F --> Z([Stop])

    E -- Yes --> G[Calculate HRA = 20%]
    G --> H[Calculate DA = 10%]
    H --> I[Calculate Overtime Payment]
    I --> J[Calculate Gross Salary]

    J --> K{Gross Salary > 10000?}

    K -- No --> P[Calculate Total Deduction]
    K -- Yes --> L[Apply 5% deduction on next 10000]

    L --> M{Gross Salary > 20000?}
    M -- Yes --> N[Apply 10% deduction on next 20000]
    M -- No --> P

    N --> O{Gross Salary > 40000?}
    O -- Yes --> Q[Apply 15% deduction above 40000]
    O -- No --> P

    Q --> P
    P --> R[Calculate Net Salary]
    R --> S[Generate Salary Statement]
    S --> T[Display Gross and Net Salary]
    T --> Z([Stop])

```




8. Expected Result
The Employee Payroll and Deduction Analysis System successfully:
- Calculates basic salary and allowances.
- Computes overtime payments and incentives.
- Calculates gross salary.
- Applies progressive deductions using salary slabs.
- Determines the final net salary.
- Generates a formatted salary statement.
9. Conclusion
This Python project automates employee salary calculations by considering basic pay, allowances, overtime, incentives, and progressive deductions. It reduces manual calculation errors and generates an accurate salary statement for employees.
