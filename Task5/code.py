
# Multi-Plan Telecommunications Cost Optimization

print("==============================================")
print(" TELECOMMUNICATION COST OPTIMIZATION SYSTEM")
print("==============================================")

customer = input("Enter customer name: ")

data_usage = float(input("Enter monthly data usage (GB): "))
call_usage = int(input("Enter calling minutes: "))

budget = float(input("Enter maximum budget (Rs.): "))
min_validity = int(input("Enter minimum validity (days): "))

if data_usage < 0 or call_usage < 0:
    print("Invalid usage details!")
    exit()

if budget < 0 or min_validity <= 0:
    print("Invalid budget or validity!")
    exit()

n = int(input("\nEnter number of mobile plans: "))

if n <= 0:
    print("Invalid number of plans!")
    exit()

plans = []
eligible_plans = []

for i in range(n):

    print("\nEnter Details of Plan", i + 1)

    name = input("Plan Name: ")
    price = float(input("Plan Price: Rs. "))
    data_limit = float(input("Data Limit (GB): "))
    call_limit = int(input("Call Minutes: "))
    validity = int(input("Validity (days): "))

    if price < 0 or data_limit < 0 or call_limit < 0 or validity <= 0:
        print("Invalid plan details! Plan skipped.")
        continue

    plan = {
        "name": name,
        "price": price,
        "data": data_limit,
        "calls": call_limit,
        "validity": validity
    }

    plans.append(plan)

    if price > budget or validity < min_validity:
        continue

    excess_data = max(0, data_usage - data_limit)
    excess_calls = max(0, call_usage - call_limit)

    # Calculate additional charges
    data_charge = excess_data * 50
    call_charge = excess_calls * 1

    total_cost = price + data_charge + call_charge

    plan["excess_data"] = excess_data
    plan["excess_calls"] = excess_calls
    plan["data_charge"] = data_charge
    plan["call_charge"] = call_charge
    plan["total_cost"] = total_cost

    # Check final budget
    if total_cost <= budget:
        eligible_plans.append(plan)

print("\n==============================================")
print("             PLAN COMPARISON")
print("==============================================")

if eligible_plans:

    for plan in eligible_plans:

        print("\nPlan Name:", plan["name"])
        print("Plan Price: Rs.", plan["price"])
        print("Excess Data: ", plan["excess_data"], "GB")
        print("Excess Calls:", plan["excess_calls"], "minutes")
        print("Data Charges: Rs.", round(plan["data_charge"], 2))
        print("Call Charges: Rs.", round(plan["call_charge"], 2))
        print("Total Cost: Rs.", round(plan["total_cost"], 2))

    best_plan = min(
        eligible_plans,
        key=lambda p: p["total_cost"]
    )

    print("\n==============================================")
    print("       MOST ECONOMICAL MOBILE PLAN")
    print("==============================================")

    print("Customer Name:", customer)
    print("Best Plan:", best_plan["name"])
    print("Plan Price: Rs.", best_plan["price"])
    print("Total Cost: Rs.", round(best_plan["total_cost"], 2))
    print("Validity:", best_plan["validity"], "days")

else:
    print("No eligible mobile plan found!")
    print("Please increase your budget or reduce requirements.")

print("\n==============================================")
print("           ANALYSIS COMPLETED")
print("==============================================")
