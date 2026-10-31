Examination Result and Grace-Mark Validation Using Python
1. Problem Statement
Develop a Python program to process student examination marks across multiple subjects, apply subject-wise passing criteria, and provide grace marks according to a specified grace-mark policy.

The system should perform the following operations:
1. Accept student details such as name, roll number, and number of subjects.
2. Accept marks obtained in each subject.
3. Validate marks to ensure they are between 0 and the maximum marks.
4. Check subject-wise minimum passing marks.
5. Apply grace marks to students who fail by a small number of marks.
6. Ensure that grace marks do not exceed the maximum subject marks.
7. Calculate total marks and percentage.
8. Generate final results and classifications.
9. Display whether the student passed or failed.
Examination Rules (Example):
Parameter	Value
Maximum marks per subject	100
Minimum passing marks	35
Maximum grace marks per subject	5
Maximum subjects	User-defined

Grace-Mark Policy:
- If a student scores between 30 and 34 marks, grace marks can be awarded to reach 35.
- Maximum grace marks allowed per subject = 5.
- Grace marks cannot increase a subject's score beyond 100.
- Students scoring below 30 are not eligible for grace marks.
- Students must pass all subjects to receive an overall PASS result.
Final Classification:
Percentage	Classification
75% and above	Distinction
60%–74.99%	First Class
50%–59.99%	Second Class
35%–49.99%	Third Class
Below 35%	Fail

Note: These are assumed academic rules for this project. Actual grace-mark policies differ between educational institutions.
2. Algorithm
1. Start the program.
2. Input student name and roll number.
3. Input the number of subjects.
4. Set maximum marks to 100.
5. Set minimum passing marks to 35.
6. Set maximum grace marks to 5.
7. For each subject:
   - Input subject name.
   - Input marks obtained.
   - Validate marks between 0 and 100.
8. Check whether the student has passed the subject.
9. If marks are between 30 and 34:
   - Calculate required grace marks.
   - Apply grace marks if they are within the allowed limit.
10. If marks are below 30, declare the subject failed.
11. Ensure final marks do not exceed 100.
12. Calculate total marks and percentage using final marks.
13. Check whether all subjects are passed.
14. If all subjects are passed, classify the student according to percentage.
15. Otherwise, declare the overall result as FAIL.
16. Display subject-wise marks, grace marks, total marks, percentage, and classification.
17. Stop.


5. Sample Input
==========================================
 EXAMINATION RESULT MANAGEMENT SYSTEM
==========================================

Enter Student Name: Ravi
Enter Roll Number: 101
Enter Number of Subjects: 5

Subject 1
Enter Subject Name: English
Enter Marks Obtained: 85

Subject 2
Enter Subject Name: Maths
Enter Marks Obtained: 32

Subject 3
Enter Subject Name: Physics
Enter Marks Obtained: 75

Subject 4
Enter Subject Name: Chemistry
Enter Marks Obtained: 90

Subject 5
Enter Subject Name: Computer
Enter Marks Obtained: 80


6. Sample Output
==========================================
          STUDENT RESULT SHEET
==========================================

Student Name : Ravi
Roll Number  : 101

------------------------------------------
Subject      Marks   Grace   Status
------------------------------------------
English      85.0    0.0     PASS
Maths        35.0    3.0     PASS
Physics      75.0    0.0     PASS
Chemistry    90.0    0.0     PASS
Computer     80.0    0.0     PASS
------------------------------------------
Total Marks : 365.0 / 500
Percentage  : 73.0 %
Final Result: PASS
Classification: First Class

==========================================
       RESULT PROCESSING COMPLETED
==========================================


Sample calculation:
- English = 85
- Maths = 32 + 3 grace marks = 35
- Physics = 75
- Chemistry = 90
- Computer = 80
Total marks = 85 + 35 + 75 + 90 + 80 = 365.

Percentage:
\[
\frac{365}{500}\times100=73\%
\]

Final classification = First Class.
```Mermaid
Flowchart Code

flowchart TD
    A([Start]) --> B[/Enter Student Name and Roll Number/]
    B --> C[/Enter Number of Subjects/]
    C --> D{Number of Subjects Valid?}

    D -- No --> E[Display Invalid Input]
    E --> Z([Stop])

    D -- Yes --> F[Initialize Total Marks and Result]
    F --> G[/Enter Subject Name and Marks/]

    G --> H{Marks Between 0 and 100?}

    H -- No --> I[Display Invalid Marks]
    I --> Z

    H -- Yes --> J{Marks >= 35?}

    J -- Yes --> K[Subject PASS]
    J -- No --> L{Marks >= 30?}

    L -- No --> M[Subject FAIL]
    L -- Yes --> N[Calculate Required Grace Marks]

    N --> O{Grace Marks <= 5?}

    O -- No --> M
    O -- Yes --> P[Apply Grace Marks]

    P --> Q[Ensure Final Marks <= 100]
    Q --> K

    K --> R[Store Subject Result and Add Marks]
    M --> R

    R --> S{More Subjects?}
    S -- Yes --> G
    S -- No --> T[Calculate Total and Percentage]

    T --> U{All Subjects Passed?}

    U -- No --> V[Final Result FAIL]
    U -- Yes --> W{Percentage >= 75?}

    W -- Yes --> X[Distinction]
    W -- No --> Y{Percentage >= 60?}

    Y -- Yes --> AA[First Class]
    Y -- No --> AB{Percentage >= 50?}

    AB -- Yes --> AC[Second Class]
    AB -- No --> AD[Third Class]

    V --> AE[Display Final Result]
    X --> AE
    AA --> AE
    AC --> AE
    AD --> AE

    AE --> Z

```




8. Expected Result
The Examination Result and Grace-Mark Validation System successfully:
- Processes marks across multiple subjects.
- Validates marks within the maximum limit.
- Checks subject-wise passing criteria.
- Applies grace marks according to the specified policy.
- Prevents marks from exceeding 100.
- Calculates total marks and percentage.
- Classifies students based on their performance.
- Generates the final PASS or FAIL result.
9. Conclusion
This Python project automates examination result processing by calculating subject-wise marks, applying grace-mark policies, and generating final classifications. It reduces manual calculation errors and ensures that grace marks are awarded only according to predefined rules without exceeding maximum marks.
