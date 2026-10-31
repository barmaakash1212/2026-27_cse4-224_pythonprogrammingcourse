ATM Transaction Sequence Simulation Using Python
1. Problem Statement
Develop a Python program to simulate ATM transactions by processing a sequence of deposits and withdrawals while maintaining an account balance.

The system should perform the following operations:
1. Accept customer account details and initial balance.
2. Allow multiple deposit and withdrawal transactions.
3. Update the account balance after every valid transaction.
4. Enforce withdrawal limits.
5. Reject invalid transactions such as negative deposits, insufficient balance, and withdrawals exceeding the permitted limit.
6. Maintain a record of successful and rejected transactions.
7. Calculate total deposits and withdrawals.
8. Generate a final transaction summary.
ATM Transaction Rules (Example):
Parameter	Value
Initial balance	User-defined
Maximum withdrawal per transaction	₹10,000
Minimum deposit	₹1
Maximum deposit	₹50,000
Minimum balance	₹500

Note: These are assumed rules for an academic project.
2. Algorithm
1. Start the program.
2. Enter customer name and account number.
3. Enter the initial account balance.
4. Validate the initial balance.
5. Enter the number of transactions.
6. For each transaction:
   - Select deposit or withdrawal.
   - Enter the transaction amount.
7. If the transaction is a deposit:
   - Check whether the amount is positive.
   - Check whether the deposit is within the maximum limit.
   - Add the amount to the account balance.
8. If the transaction is a withdrawal:
   - Check whether the amount is positive.
   - Check whether the amount is within the withdrawal limit.
   - Check whether sufficient balance remains after withdrawal.
   - Subtract the amount from the account balance.
9. Reject invalid transactions and display the reason.
10. Record successful and rejected transactions.
11. Calculate total deposits and withdrawals.
12. Display the final account balance.
13. Display the transaction summary.
14. Stop.


5. Sample Input
========================================
       ATM TRANSACTION SYSTEM
========================================

Enter Customer Name: Ravi
Enter Account Number: 123456789
Enter Initial Balance: Rs. 15000

Enter Number of Transactions: 5

Transaction 1
1. Deposit
2. Withdrawal
Enter Transaction Type: 1
Enter Amount: Rs. 5000

Transaction 2
1. Deposit
2. Withdrawal
Enter Transaction Type: 2
Enter Amount: Rs. 3000

Transaction 3
1. Deposit
2. Withdrawal
Enter Transaction Type: 2
Enter Amount: Rs. 12000

Transaction 4
1. Deposit
2. Withdrawal
Enter Transaction Type: 1
Enter Amount: Rs. 2000

Transaction 5
1. Deposit
2. Withdrawal
Enter Transaction Type: 2
Enter Amount: Rs. 4000


6. Sample Output
========================================
        ATM TRANSACTION SUMMARY
========================================

Customer Name       : Ravi
Account Number      : 123456789

----------------------------------------
Transaction Details
----------------------------------------

Transaction No: 1
Transaction Type: 1
Amount: Rs. 5000.0
Status: Successful Deposit
Balance: Rs. 20000.0

Transaction No: 2
Transaction Type: 2
Amount: Rs. 3000.0
Status: Successful Withdrawal
Balance: Rs. 17000.0

Transaction No: 3
Transaction Type: 2
Amount: Rs. 12000.0
Status: Rejected - Withdrawal Limit Exceeded
Balance: Rs. 17000.0

Transaction No: 4
Transaction Type: 1
Amount: Rs. 2000.0
Status: Successful Deposit
Balance: Rs. 19000.0

Transaction No: 5
Transaction Type: 2
Amount: Rs. 4000.0
Status: Successful Withdrawal
Balance: Rs. 15000.0

----------------------------------------
Total Deposits      : Rs. 7000.0
Total Withdrawals   : Rs. 7000.0

Successful Transactions: 4
Rejected Transactions  : 1

----------------------------------------
Final Account Balance: Rs. 15000.0

========================================
       TRANSACTION PROCESS COMPLETED
========================================


```Mermaid
Flowchart Code

flowchart TD
    A([Start]) --> B[/Enter Customer Details/]
    B --> C[/Enter Initial Balance/]

    C --> D{Initial Balance Valid?}
    D -- No --> E[Display Invalid Balance]
    E --> Z([Stop])

    D -- Yes --> F[/Enter Number of Transactions/]
    F --> G[Initialize Balance and Counters]

    G --> H{More Transactions?}

    H -- Yes --> I[/Select Deposit or Withdrawal/]
    I --> J[/Enter Transaction Amount/]

    J --> K{Valid Transaction Type?}

    K -- No --> L[Reject Invalid Transaction]
    K -- Yes --> M{Deposit or Withdrawal?}

    M -- Deposit --> N{Amount Positive and Within Deposit Limit?}

    N -- No --> O[Reject Deposit]
    N -- Yes --> P[Add Amount to Balance]
    P --> Q[Update Total Deposits]

    M -- Withdrawal --> R{Amount Positive and Within Withdrawal Limit?}

    R -- No --> S[Reject Withdrawal]
    R -- Yes --> T{Minimum Balance Maintained?}

    T -- No --> U[Reject Insufficient Balance]
    T -- Yes --> V[Subtract Amount from Balance]
    V --> W[Update Total Withdrawals]

    L --> X[Record Transaction]
    O --> X
    Q --> X
    S --> X
    U --> X
    W --> X

    X --> Y[Increment Transaction Counter]
    Y --> H

    H -- No --> AA[Calculate Transaction Summary]
    AA --> AB[Display Deposits and Withdrawals]
    AB --> AC[Display Successful and Rejected Transactions]
    AC --> AD[Display Final Account Balance]
    AD --> Z

```




8. Expected Result
The ATM Transaction Sequence Simulation successfully:
- Accepts customer and account details.
- Processes multiple deposits and withdrawals.
- Maintains the updated account balance.
- Enforces deposit and withdrawal limits.
- Prevents withdrawals below the minimum balance.
- Rejects invalid transactions.
- Maintains a transaction history.
- Calculates total deposits and withdrawals.
- Generates a complete transaction summary.
9. Conclusion
This Python project simulates an ATM transaction system using conditional statements, loops, and lists. It maintains account balances, validates deposits and withdrawals, enforces transaction limits, and generates a detailed transaction summary. It helps understand how basic banking operations can be implemented using Python programming.
