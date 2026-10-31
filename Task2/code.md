Develop a Python program to calculate household electricity bills based on monthly electricity consumption using a progressive slab billing system.

The system should:
1. Accept the number of units consumed by a household.
2. Calculate electricity charges using multiple consumption slabs.
3. Add fixed charges to the bill.
4. Apply additional surcharges.
5. Provide rebates based on eligibility.
6. Calculate the total electricity bill for multiple months.
7. Compare monthly bills and identify unusual increases in electricity consumption or billing amounts.
Billing Slab Rates (Example):
Units consumed	Rate per unit
0–100	₹2.00
101–200	₹3.00
201–300	₹5.00
Above 300	₹7.00

Additional charges:
- Fixed charge = ₹50
- Surcharge = 5% of energy charges
- Rebate = ₹20 if consumption is below 100 units
- Unusual increase = More than 30% compared with the previous month's bill.
Note: These are assumed rates for an academic project, not official electricity tariffs.
2. Algorithm
1. Start the program.
2. Read the number of months.
3. For each month, input electricity units consumed.
4. Calculate energy charges using progressive slabs:
   - First 100 units: ₹2 per unit.
   - Next 100 units: ₹3 per unit.
   - Next 100 units: ₹5 per unit.
   - Above 300 units: ₹7 per unit.
5. Add fixed charges of ₹50.
6. Calculate a 5% surcharge on energy charges.
7. If consumption is below 100 units, subtract a ₹20 rebate.
8. Calculate the final bill.
9. Store the monthly consumption and bill amount.
10. Compare the current month's bill with the previous month's bill.
11. If the increase is greater than 30%, display an unusual increase warning.
12. Display all monthly bills and total expenditure.
13. Stop.

5. Sample Input
Enter number of months: 4

Month 1
Enter electricity units consumed: 80

Month 2
Enter electricity units consumed: 150

Month 3
Enter electricity units consumed: 250

Month 4
Enter electricity units consumed: 350


6. Sample Output
===================================
 PROGRESSIVE ELECTRICITY BILLING
===================================

Month 1
Energy Charge : Rs. 160.0
Fixed Charge  : Rs. 50.00
Surcharge     : Rs. 8.0
Rebate        : Rs. 20.0
Total Bill    : Rs. 198.0

Month 2
Energy Charge : Rs. 350.0
Fixed Charge  : Rs. 50.00
Surcharge     : Rs. 17.5
Rebate        : Rs. 0.0
Total Bill    : Rs. 417.5

Month 3
Energy Charge : Rs. 850.0
Fixed Charge  : Rs. 50.00
Surcharge     : Rs. 42.5
Rebate        : Rs. 0.0
Total Bill    : Rs. 942.5

Month 4
Energy Charge : Rs. 1550.0
Fixed Charge  : Rs. 50.00
Surcharge     : Rs. 77.5
Rebate        : Rs. 0.0
Total Bill    : Rs. 1677.5

========== MONTHLY BILL REPORT ==========

Month 1 - Units: 80.0 Bill: Rs. 198.0

Month 2 - Units: 150.0 Bill: Rs. 417.5
Bill Increase: 110.86 %

WARNING: Unusual increase detected!

Month 3 - Units: 250.0 Bill: Rs. 942.5
Bill Increase: 125.75 %

WARNING: Unusual increase detected!

Month 4 - Units: 350.0 Bill: Rs. 1677.5
Bill Increase: 77.98 %

WARNING: Unusual increase detected!

Total Electricity Expense: Rs. 3235.5
Average Monthly Bill: Rs. 808.88

Thank you!


 ```Mermaid
 Flowchart

flowchart TD
    A([Start]) --> B[/Enter number of months/]
    B --> C[Initialize month counter]
    C --> D{More months?}

    D -- Yes --> E[/Enter units consumed/]
    E --> F{Units valid?}

    F -- No --> G[Display invalid input]
    G --> E

    F -- Yes --> H{Units <= 100?}

    H -- Yes --> I[Charge = Units * 2]
    H -- No --> J{Units <= 200?}

    J -- Yes --> K[Charge = 200 + (Units-100)*3]
    J -- No --> L{Units <= 300?}

    L -- Yes --> M[Charge = 500 + (Units-200)*5]
    L -- No --> N[Charge = 1000 + (Units-300)*7]

    I --> O[Add fixed charge]
    K --> O
    M --> O
    N --> O

    O --> P[Calculate 5 percent surcharge]
    P --> Q{Units < 100?}

    Q -- Yes --> R[Apply Rs.20 rebate]
    Q -- No --> S[No rebate]

    R --> T[Calculate final bill]
    S --> T

    T --> U[Store monthly bill and units]
    U --> V[Increment month counter]
    V --> D

    D -- No --> W[Compare monthly bills]
    W --> X{Increase greater than 30 percent?}

    X -- Yes --> Y[Display unusual increase warning]
    X -- No --> Z[Display normal bill change]

    Y --> AA[Display total and average bill]
    Z --> AA
    AA --> AB([Stop])
```
9. Expected Result
The Progressive Electricity Billing System successfully:
- Calculates electricity charges using progressive slabs.
- Adds fixed charges and surcharges.
- Applies eligible rebates.
- Generates monthly electricity bills.
- Compares bills across different months.
- Detects unusual increases greater than 30%.
- Displays total and average electricity expenditure.
Conclusion: This Python project helps households calculate electricity bills accurately and monitor monthly electricity expenses by identifying unusual increases in billing amounts.
