
# ATM Transaction Sequence Simulation

print("========================================")
print("       ATM TRANSACTION SYSTEM")
print("========================================")

MAX_WITHDRAWAL = 10000
MAX_DEPOSIT = 50000
MIN_BALANCE = 500

name = input("Enter Customer Name: ")
account = input("Enter Account Number: ")

balance = float(input("Enter Initial Balance: Rs. "))

if balance < MIN_BALANCE:
    print("Invalid Initial Balance!")
    exit()

n = int(input("\nEnter Number of Transactions: "))

if n <= 0:
    print("Invalid Number of Transactions!")
    exit()

total_deposits = 0
total_withdrawals = 0
successful = 0
rejected = 0

transactions = []

for i in range(n):

    print("\nTransaction", i + 1)
    print("1. Deposit")
    print("2. Withdrawal")

    choice = input("Enter Transaction Type: ").strip()

    amount = float(input("Enter Amount: Rs. "))

    status = ""

    if choice == "1":

        if amount <= 0:
            status = "Rejected - Invalid Amount"
            rejected += 1

        elif amount > MAX_DEPOSIT:
            status = "Rejected - Deposit Limit Exceeded"
            rejected += 1

        else:
            balance += amount
            total_deposits += amount
            successful += 1
            status = "Successful Deposit"

    elif choice == "2":

        if amount <= 0:
            status = "Rejected - Invalid Amount"
            rejected += 1

        elif amount > MAX_WITHDRAWAL:
            status = "Rejected - Withdrawal Limit Exceeded"
            rejected += 1

        elif balance - amount < MIN_BALANCE:
            status = "Rejected - Insufficient Available Balance"
            rejected += 1

        else:
            balance -= amount
            total_withdrawals += amount
            successful += 1
            status = "Successful Withdrawal"

    else:
        status = "Rejected - Invalid Transaction Type"
        rejected += 1

    transactions.append({
        "number": i + 1,
        "type": choice,
        "amount": amount,
        "status": status,
        "balance": balance
    })

    print("Transaction Status:", status)
    print("Available Balance: Rs.", round(balance, 2))


print("\n========================================")
print("        ATM TRANSACTION SUMMARY")
print("========================================")

print("Customer Name       :", name)
print("Account Number      :", account)

print("----------------------------------------")
print("Transaction Details")
print("----------------------------------------")

for t in transactions:
    print("\nTransaction No:", t["number"])
    print("Transaction Type:", t["type"])
    print("Amount: Rs.", round(t["amount"], 2))
    print("Status:", t["status"])
    print("Balance: Rs.", round(t["balance"], 2))

print("\n----------------------------------------")
print("Total Deposits      : Rs.",
      round(total_deposits, 2))

print("Total Withdrawals   : Rs.",
      round(total_withdrawals, 2))

print("Successful Transactions:", successful)
print("Rejected Transactions  :", rejected)

print("----------------------------------------")
print("Final Account Balance: Rs.",
      round(balance, 2))

print("========================================")
print("       TRANSACTION PROCESS COMPLETED")
print("========================================")

