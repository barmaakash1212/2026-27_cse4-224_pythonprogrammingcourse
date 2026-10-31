Develop a Python program to calculate hospital bills based on consultation charges, diagnostic charges, and treatment charges.

The system should perform the following operations:
1. Accept patient details such as patient name, age, and patient type.
2. Calculate consultation charges.
3. Calculate diagnostic test charges.
4. Calculate treatment charges.
5. Apply conditional concessions based on patient category.
6. Validate billing constraints, such as invalid age, negative charges, and invalid patient type.
7. Calculate the final payable amount after concessions.
8. Classify patients according to a payment policy.
Payment Policy (Example):
Patient category	Concession
General patient	0%
Senior citizen (age 60 or above)	10%
Student	5%
Below poverty line (BPL)	20%

Patient classification:
Final bill amount	Classification
Below ₹1,000	Low Payment
₹1,000–₹5,000	Medium Payment
Above ₹5,000	High Payment

Note: The charges and concession percentages are assumed for this academic project.
2. Algorithm
1. Start the program.
2. Input patient name, age, and patient category.
3. Validate the patient's age and category.
4. Input consultation charges.
5. Input diagnostic charges.
6. Input treatment charges.
7. Check whether all charges are non-negative.
8. Calculate the total bill:
   Total Bill = Consultation + Diagnostic + Treatment
9. Determine the concession percentage:
   - Senior citizen: 10%.
   - Student: 5%.
   - BPL: 20%.
   - General: 0%.
10. Calculate the concession amount.
11. Calculate the final payable amount.
12. Classify the patient based on the final bill:
- Below ₹1,000: Low Payment.
- ₹1,000 to ₹5,000: Medium Payment.
- Above ₹5,000: High Payment.
13. Display the complete billing details.
14. Stop.

5. Sample Input
======================================
 HOSPITAL BILLING MANAGEMENT SYSTEM
======================================

Enter patient name: Ravi
Enter patient age: 65

Patient Categories:
1. General
2. Senior Citizen
3. Student
4. BPL

Enter patient category: senior citizen

Enter Hospital Charges

Consultation charges: Rs. 500
Diagnostic charges: Rs. 1500
Treatment charges: Rs. 4000


6. Sample Output
======================================
          HOSPITAL BILL
======================================

Patient Name       : Ravi
Patient Age        : 65
Patient Category   : Senior Citizen

--------------------------------------
Consultation Charge: Rs. 500.0
Diagnostic Charge  : Rs. 1500.0
Treatment Charge   : Rs. 4000.0

--------------------------------------
Total Bill         : Rs. 6000.0
Concession Rate    : 10 %
Concession Amount  : Rs. 600.0
Final Payable      : Rs. 5400.0

--------------------------------------
Patient Class      : High Payment

======================================
       BILLING COMPLETED
======================================


```Mermaid
Flowchart Code

flowchart TD
    A([Start]) --> B[/Enter patient details/]
    B --> C[/Enter age and category/]

    C --> D{Age valid?}
    D -- No --> E[Display invalid age]
    E --> Z([Stop])

    D -- Yes --> F{Category valid?}
    F -- No --> G[Display invalid category]
    G --> Z

    F -- Yes --> H[/Enter consultation charges/]
    H --> I[/Enter diagnostic charges/]
    I --> J[/Enter treatment charges/]

    J --> K{Charges non-negative?}
    K -- No --> L[Display billing error]
    L --> Z

    K -- Yes --> M[Calculate total bill]

    M --> N{Patient category?}

    N -- Senior Citizen --> O{Age >= 60?}
    O -- No --> P[Display category error]
    P --> Z
    O -- Yes --> Q[Apply 10 percent concession]

    N -- Student --> R[Apply 5 percent concession]
    N -- BPL --> S[Apply 20 percent concession]
    N -- General --> T[No concession]

    Q --> U[Calculate final payable amount]
    R --> U
    S --> U
    T --> U

    U --> V{Final bill < 1000?}

    V -- Yes --> W[Low Payment]
    V -- No --> X{Final bill <= 5000?}

    X -- Yes --> Y[Medium Payment]
    X -- No --> AA[High Payment]

    W --> AB[Display hospital bill]
    Y --> AB
    AA --> AB

    AB --> Z

```




9. Expected Result
The Hospital Billing and Patient Classification System successfully:
- Calculates consultation, diagnostic, and treatment charges.
- Applies concessions based on patient category.
- Validates patient information and billing constraints.
- Calculates the final payable amount.
- Classifies patients into Low, Medium, and High Payment categories.
- Displays a complete hospital bill.
9. Conclusion
This project provides an efficient hospital billing system using Python. It reduces manual calculation errors, applies conditional concessions, validates billing information, and classifies patients according to the payment policy.
