from datetime import datetime
import math

print("====================================")
print("     SMART PARKING FEE SYSTEM")
print("====================================")

tariffs = {
    "two-wheeler": {"rate": 10, "daily_limit": 100},
    "car": {"rate": 30, "daily_limit": 300},
    "bus": {"rate": 50, "daily_limit": 500}
}

vehicle_no = input("Enter vehicle number: ").upper()

print("\nVehicle Categories:")
print("1. Two-wheeler")
print("2. Car")
print("3. Bus")

category = input("Enter vehicle category: ").lower()

if category not in tariffs:
    print("Invalid vehicle category!")
    exit()

date_format = "%Y-%m-%d %H:%M"

try:
    entry_input = input(
        "Enter entry date and time (YYYY-MM-DD HH:MM): "
    )
    exit_input = input(
        "Enter exit date and time (YYYY-MM-DD HH:MM): "
    )

    entry_time = datetime.strptime(entry_input, date_format)
    exit_time = datetime.strptime(exit_input, date_format)

except ValueError:
    print("Invalid date or time format!")
    exit()

if exit_time <= entry_time:
    print("Error: Exit time must be after entry time!")
    exit()

duration = exit_time - entry_time
total_minutes = duration.total_seconds() / 60

total_hours = math.ceil(total_minutes / 60)

rate = tariffs[category]["rate"]
daily_limit = tariffs[category]["daily_limit"]

full_days = int(total_minutes // (24 * 60))
remaining_minutes = total_minutes % (24 * 60)

remaining_hours = math.ceil(remaining_minutes / 60)

parking_fee = (
    full_days * daily_limit
    + min(remaining_hours * rate, daily_limit)
)

overnight_count = (
    exit_time.date() - entry_time.date()
).days

overnight_fee = overnight_count * 50

lost_ticket = input(
    "Is the parking ticket lost? (yes/no): "
).lower()

if lost_ticket == "yes":
    penalty = 200
elif lost_ticket == "no":
    penalty = 0
else:
    print("Invalid ticket status!")
    exit()

total_fee = parking_fee + overnight_fee + penalty

print("\n====================================")
print("          PARKING RECEIPT")
print("====================================")

print("Vehicle Number:", vehicle_no)
print("Vehicle Category:", category.title())
print("Entry Time:", entry_time)
print("Exit Time:", exit_time)
print("Total Parking Hours:", total_hours)

print("------------------------------------")
print("Hourly Parking Charge: Rs.", parking_fee)
print("Overnight Charge: Rs.", overnight_fee)
print("Penalty Charge: Rs.", penalty)
print("------------------------------------")
print("TOTAL PARKING FEE: Rs.", total_fee)
print("====================================")
print("Thank you for using Smart Parking!")
