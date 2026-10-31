Multi-Plan Telecommunications Cost Optimization Using Python
1. Problem Statement
Develop a Python program to evaluate multiple mobile telecommunications plans based on customer usage, validity period, and budget constraints.

The system should compare different mobile plans and identify the most economical eligible plan according to the customer's requirements.

The program should perform the following operations:
1. Accept customer details and requirements.
2. Accept the number of mobile plans to compare.
3. Input plan details such as plan name, price, data limit, call minutes, and validity.
4. Accept customer usage details, including data consumption and call minutes.
5. Check whether each plan satisfies the validity and budget constraints.
6. Calculate excess data charges and additional calling charges.
7. Calculate the total cost of each eligible plan.
8. Compare all eligible plans.
9. Identify and display the most economical plan.
10. Display a comparison report of all plans.
Example Mobile Plan Details:
Plan	Price	Data limit	Call minutes	Validity
Plan A	₹199	2 GB	200 min	28 days
Plan B	₹299	3 GB	500 min	28 days
Plan C	₹399	5 GB	1000 min	56 days
Plan D	₹499	8 GB	1200 min	84 days

Additional Charges:
- Excess data charge = ₹50 per GB.
- Excess calling charge = ₹1 per minute.
- Budget and minimum validity must be satisfied.
Note: All plan prices and charges are hypothetical values for this academic project.
2. Algorithm
1. Start the program.
2. Input customer name.
3. Input the customer's monthly data usage.
4. Input the customer's calling minutes.
5. Input the maximum budget.
6. Input the minimum required validity.
7. Enter the number of mobile plans.
8. For each plan, input:
   - Plan name.
   - Plan price.
   - Data limit.
   - Calling minutes.
   - Validity days.
9. Validate all input values.
10. Check whether the plan satisfies the budget and validity requirements.
11. Calculate excess data usage.
12. Calculate excess calling minutes.
13. Calculate additional charges:
    - Data excess charge = Excess GB × ₹50.
    - Calling excess charge = Excess minutes × ₹1.
14. Calculate total plan cost:
    Total Cost = Plan Price + Data Excess Charge + Calling Excess Charge.
15. Store all eligible plans and their total costs.
16. Compare the eligible plans.
17. Select the plan with the lowest total cost.
18. Display the comparison report.
19. Display the most economical eligible plan.
20. If no plan is eligible, display an appropriate message.
21. Stop.


5. Sample Input
==============================================
 TELECOMMUNICATION COST OPTIMIZATION SYSTEM
==============================================

Enter customer name: Ravi
Enter monthly data usage (GB): 4
Enter calling minutes: 300
Enter maximum budget (Rs.): 500
Enter minimum validity (days): 28

Enter number of mobile plans: 4

Enter Details of Plan 1
Plan Name: Plan A
Plan Price: Rs. 199
Data Limit (GB): 2
Call Minutes: 200
Validity (days): 28

Enter Details of Plan 2
Plan Name: Plan B
Plan Price: Rs. 299
Data Limit (GB): 3
Call Minutes: 500
Validity (days): 28

Enter Details of Plan 3
Plan Name: Plan C
Plan Price: Rs. 399
Data Limit (GB): 5
Call Minutes: 1000
Validity (days): 56

Enter Details of Plan 4
Plan Name: Plan D
Plan Price: Rs. 499
Data Limit (GB): 8
Call Minutes: 1200
Validity (days): 84


6. Sample Output
==============================================
             PLAN COMPARISON
==============================================

Plan Name: Plan A
Plan Price: Rs. 199.0
Excess Data: 2.0 GB
Excess Calls: 100 minutes
Data Charges: Rs. 100.0
Call Charges: Rs. 100.0
Total Cost: Rs. 399.0

Plan Name: Plan B
Plan Price: Rs. 299.0
Excess Data: 1.0 GB
Excess Calls: 0 minutes
Data Charges: Rs. 50.0
Call Charges: Rs. 0.0
Total Cost: Rs. 349.0

Plan Name: Plan C
Plan Price: Rs. 399.0
Excess Data: 0.0 GB
Excess Calls: 0 minutes
Data Charges: Rs. 0.0
Call Charges: Rs. 0.0
Total Cost: Rs. 399.0

Plan Name: Plan D
Plan Price: Rs. 499.0
Excess Data: 0.0 GB
Excess Calls: 0 minutes
Data Charges: Rs. 0.0
Call Charges: Rs. 0.0
Total Cost: Rs. 499.0

==============================================
       MOST ECONOMICAL MOBILE PLAN
==============================================

Customer Name: Ravi
Best Plan: Plan B
Plan Price: Rs. 299.0
Total Cost: Rs. 349.0
Validity: 28 days

==============================================
           ANALYSIS COMPLETED
==============================================

```Mermaid
Flowchart Code

flowchart TD
    A([Start]) --> B[/Enter Customer Details/]
    B --> C[/Enter Data Usage and Call Usage/]
    C --> D[/Enter Budget and Minimum Validity/]
    D --> E[/Enter Number of Plans/]

    E --> F[Initialize Plan Counter]
    F --> G{More Plans?}

    G -- Yes --> H[/Enter Plan Details/]
    H --> I{Plan Details Valid?}

    I -- No --> J[Display Invalid Plan]
    J --> K[Next Plan]

    I -- Yes --> L{Price Within Budget and Validity Sufficient?}

    L -- No --> K

    L -- Yes --> M[Calculate Excess Data]
    M --> N[Calculate Excess Calling Minutes]
    N --> O[Calculate Additional Charges]
    O --> P[Calculate Total Plan Cost]

    P --> Q{Total Cost Within Budget?}

    Q -- Yes --> R[Store Eligible Plan]
    Q -- No --> K

    R --> K
    K --> S[Increment Plan Counter]
    S --> G

    G -- No --> T{Any Eligible Plans?}

    T -- No --> U[Display No Eligible Plan]
    T -- Yes --> V[Compare Total Costs]

    V --> W[Select Lowest Cost Plan]
    W --> X[Display Best Plan and Comparison]

    U --> Y([Stop])
    X --> Y

```




8. Expected Result
The Multi-Plan Telecommunications Cost Optimization System successfully:
- Evaluates multiple mobile recharge plans.
- Checks customer usage requirements.
- Validates budget and plan validity.
- Calculates excess data and calling charges.
- Computes the total cost of each eligible plan.
- Compares different mobile plans.
- Identifies the most economical eligible plan.
9. Conclusion
This Python project helps customers select the most economical mobile plan according to their data usage, calling requirements, validity period, and budget. It reduces manual calculations and provides an efficient way to compare multiple telecommunications plans and identify the best option.
