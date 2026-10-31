
# Progressive Electricity Billing System

def calculate_energy_charge(units):
    charge = 0

    if units <= 100:
        charge = units * 2

    elif units <= 200:
        charge = (100 * 2) + (units - 100) * 3

    elif units <= 300:
        charge = (100 * 2) + (100 * 3) + (units - 200) * 5

    else:
        charge = (100 * 2) + (100 * 3) + (100 * 5) + (units - 300) * 7

    return charge


def calculate_bill(units):
    energy_charge = calculate_energy_charge(units)

    fixed_charge = 50
    surcharge = energy_charge * 0.05

    rebate = 20 if units < 100 else 0

    total_bill = energy_charge + fixed_charge + surcharge - rebate

    return energy_charge, surcharge, rebate, total_bill


print("===================================")
print(" PROGRESSIVE ELECTRICITY BILLING")
print("===================================")

months = int(input("Enter number of months: "))

consumption = []
bills = []

for i in range(months):
    print("\nMonth", i + 1)

    units = float(input("Enter electricity units consumed: "))

    if units < 0:
        print("Invalid units! Enter a positive value.")
        continue

    energy, surcharge, rebate, total = calculate_bill(units)

    consumption.append(units)
    bills.append(total)

    print("Energy Charge : Rs.", round(energy, 2))
    print("Fixed Charge  : Rs. 50.00")
    print("Surcharge     : Rs.", round(surcharge, 2))
    print("Rebate        : Rs.", round(rebate, 2))
    print("Total Bill    : Rs.", round(total, 2))

print("\n========== MONTHLY BILL REPORT ==========")

for i in range(len(bills)):
    print("Month", i + 1, "- Units:", consumption[i],
          "Bill: Rs.", round(bills[i], 2))

    if i > 0:
        increase = bills[i] - bills[i - 1]

        if increase > 0:
            percentage = (increase / bills[i - 1]) * 100
            print("Bill Increase:", round(percentage, 2), "%")

            if percentage > 30:
                print("WARNING: Unusual increase detected!")

        elif increase < 0:
            print("Bill decreased by:",
                  round(abs(increase), 2))

        else:
            print("No change in bill.")

print("\nTotal Electricity Expense: Rs.",
      round(sum(bills), 2))

print("Average Monthly Bill: Rs.",
      round(sum(bills) / len(bills), 2) if bills else 0)

print("\nThank you!")

