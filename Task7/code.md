Attendance Recovery Computation Using Python
1. Problem Statement
Develop a Python program to calculate a student's current attendance percentage and determine the minimum number of consecutive classes the student must attend to reach the required attendance eligibility threshold.

The system should calculate attendance under different future attendance scenarios and identify how many additional classes are required to become eligible.

The program should perform the following operations:
1. Accept student details such as name and roll number.
2. Accept the total number of classes conducted.
3. Accept the number of classes attended.
4. Calculate the current attendance percentage.
5. Accept the minimum required attendance percentage.
6. Calculate the minimum consecutive classes required to reach the eligibility threshold.
7. Evaluate different future attendance scenarios.
8. Display the updated attendance percentage for each scenario.
9. Identify whether the student is eligible or not.
10. Display the final attendance recovery report.
Attendance Rules (Example):
Parameter	Value
Minimum attendance	75%
Total classes conducted	100
Classes attended	60
Classes absent	40

Formula:

Current attendance percentage:
\[
\text{Attendance}=\frac{\text{Classes Attended}}{\text{Total Classes}}\times100
\]

Future attendance percentage after attending \(x\) consecutive classes:
\[
\text{Future Attendance}=
\frac{A+x}{T+x}\times100
\]

Where:
- \(A\) = Classes attended.
- \(T\) = Total classes conducted.
- \(x\) = Additional consecutive classes attended.
Minimum additional classes required:
\[
x=\left\lceil\frac{(P\times T)-A}{1-P}\right\rceil
\]

Here, \(P\) is the eligibility threshold expressed as a decimal.
2. Algorithm
1. Start the program.
2. Input student name and roll number.
3. Input total classes conducted.
4. Input classes attended.
5. Validate that attended classes do not exceed total classes.
6. Input the required attendance percentage.
7. Calculate current attendance percentage.
8. Compare current attendance with the eligibility threshold.
9. If attendance is already sufficient, display eligible status.
10. Otherwise:
    - Calculate the minimum consecutive classes required.
    - Assume the student attends every upcoming class.
11. Input the number of future attendance scenarios.
12. For each scenario:
    - Input the number of future classes.
    - Calculate updated attendance percentage.
    - Check whether the student reaches the eligibility threshold.
13. Display the current attendance percentage.
14. Display minimum recovery classes.
15. Display the future scenario comparison.
16. Display the final eligibility status.
17. Stop.



5. Sample Input
==========================================
       ATTENDANCE RECOVERY SYSTEM
==========================================

Enter Student Name: Ravi
Enter Roll Number: 101

Enter Total Classes Conducted: 100
Enter Classes Attended: 60

Enter Minimum Attendance Percentage: 75

==========================================
       FUTURE ATTENDANCE SCENARIOS
==========================================

Enter Number of Future Scenarios: 3

Scenario 1
Enter Number of Future Classes: 20

Scenario 2
Enter Number of Future Classes: 40

Scenario 3
Enter Number of Future Classes: 60


6. Sample Output
==========================================
          CURRENT ATTENDANCE
==========================================

Student Name: Ravi
Roll Number: 101
Total Classes: 100
Attended Classes: 60
Current Attendance: 60.0 %

Minimum Consecutive Classes Required: 60

==========================================
       FUTURE ATTENDANCE SCENARIOS
==========================================

Scenario 1
Updated Attendance: 66.67 %
Eligibility Status: NOT ELIGIBLE

Scenario 2
Updated Attendance: 71.43 %
Eligibility Status: NOT ELIGIBLE

Scenario 3
Updated Attendance: 75.0 %
Eligibility Status: ELIGIBLE

==========================================
          FINAL ATTENDANCE REPORT
==========================================

Student Name: Ravi
Current Attendance: 60.0 %
Required Attendance: 75.0 %
Recovery Classes Required: 60
Final Status: NEEDS ATTENDANCE RECOVERY

==========================================
       ATTENDANCE ANALYSIS COMPLETED
==========================================


Sample Calculation:

Given:
- Total classes = 100
- Attended classes = 60
- Required attendance = 75%
Using the formula:
\[
x=\left\lceil\frac{75\times100/100-60}{1-0.75}\right\rceil
\]

\[
x=\left\lceil\frac{75-60}{0.25}\right\rceil
\]

\[
\boxed{x=60\text{ classes}}
\]

Therefore, the student must attend 60 consecutive upcoming classes without absence to reach 75% attendance.
```Mermaid
Flowchart Code

flowchart TD
    A([Start]) --> B[/Enter Student Details/]
    B --> C[/Enter Total Classes and Attended Classes/]

    C --> D{Attendance Details Valid?}

    D -- No --> E[Display Invalid Input]
    E --> Z([Stop])

    D -- Yes --> F[/Enter Eligibility Threshold/]

    F --> G{Threshold Between 0 and 100?}

    G -- No --> H[Display Invalid Threshold]
    H --> Z

    G -- Yes --> I[Calculate Current Attendance Percentage]

    I --> J{Attendance >= Threshold?}

    J -- Yes --> K[Recovery Classes = 0]
    J -- No --> L[Calculate Minimum Consecutive Classes]

    K --> M[/Enter Number of Future Scenarios/]
    L --> M

    M --> N[Initialize Scenario Counter]
    N --> O{More Scenarios?}

    O -- Yes --> P[/Enter Future Classes/]

    P --> Q{Future Classes Valid?}

    Q -- No --> R[Display Invalid Scenario]
    R --> S[Next Scenario]

    Q -- Yes --> T[Calculate Updated Attendance]
    T --> U{Updated Attendance >= Threshold?}

    U -- Yes --> V[Display ELIGIBLE]
    U -- No --> W[Display NOT ELIGIBLE]

    V --> S
    W --> S

    S --> X[Increment Scenario Counter]
    X --> O

    O -- No --> Y[Display Final Attendance Report]
    Y --> Z([Stop])

```




8. Expected Result
The Attendance Recovery Computation System successfully:
- Calculates current attendance percentages.
- Validates total and attended classes.
- Checks minimum attendance eligibility.
- Determines the minimum consecutive classes required.
- Evaluates multiple future attendance scenarios.
- Calculates updated attendance percentages.
- Identifies eligible and not-eligible students.
- Generates a final attendance report.
9. Conclusion
This Python project helps students and educational institutions monitor attendance and calculate the minimum number of consecutive classes required to achieve attendance eligibility. It evaluates different future attendance scenarios and provides accurate recovery calculations using mathematical formulas and conditional statements.
