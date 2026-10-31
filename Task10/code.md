Smart Parking Fee Management System – Python Program
1. Problem Statement
Develop a Smart Parking Fee Management System that calculates parking charges based on vehicle entry time, exit time, vehicle category, overnight parking, daily parking limits, and penalty conditions.

The system should:
1. Accept vehicle registration number and vehicle category.
2. Read parking entry and exit date and time.
3. Validate date and time inputs.
4. Calculate the total parking duration.
5. Apply different hourly rates for different vehicle categories.
6. Calculate additional overnight charges when applicable.
7. Apply a maximum daily parking fee.
8. Add penalty charges for special conditions, such as a lost parking ticket.
9. Display the total parking fee and parking details.
Assumed parking tariff for this program:
Vehicle category	Hourly rate	Daily maximum
Two-wheeler	₹10	₹100
Car	₹30	₹300
Bus	₹50	₹500

Additional rules:
- Any started hour is charged as a full hour.
- Overnight parking charge: ₹50 per overnight period.
- Lost ticket penalty: ₹200.
- Daily maximum applies to hourly parking charges for each 24-hour period.
- Overnight and penalty charges are added separately.
- Parking duration must be greater than zero.
2. Algorithm
1. Start the program.
2. Enter the vehicle registration number.
3. Select the vehicle category.
4. Enter parking entry date and time.
5. Enter parking exit date and time.
6. Validate the date and time formats.
7. Check whether the exit time is later than the entry time.
8. Calculate total parking duration in minutes.
9. Convert the duration into hours, rounding up partial hours.
10. Select the hourly rate and daily maximum based on vehicle category.
11. Calculate the hourly parking fee for each 24-hour period.
12. Apply the daily maximum limit.
13. Calculate overnight charges.
14. Check whether the parking ticket is lost.
15. Add the applicable penalty.
16. Calculate the final parking fee.
17. Display the parking receipt.
18. Stop.

5. Sample Input
Enter vehicle number: AP16AB1234

Vehicle Categories:
1. Two-wheeler
2. Car
3. Bus

Enter vehicle category: car

Enter entry date and time (YYYY-MM-DD HH:MM):
2026-10-30 20:00

Enter exit date and time (YYYY-MM-DD HH:MM):
2026-10-31 10:30

Is the parking ticket lost? (yes/no): no


6. Sample Output
====================================
     SMART PARKING FEE SYSTEM
====================================

====================================
          PARKING RECEIPT
====================================

Vehicle Number: AP16AB1234
Vehicle Category: Car
Entry Time: 2026-10-30 20:00:00
Exit Time: 2026-10-31 10:30:00
Total Parking Hours: 15

------------------------------------
Hourly Parking Charge: Rs. 300
Overnight Charge: Rs. 50
Penalty Charge: Rs. 0
------------------------------------
TOTAL PARKING FEE: Rs. 350
====================================
Thank you for using Smart Parking!


Calculation:
- Total duration = 14 hours 30 minutes.
- Rounded parking duration = 15 hours.
- Hourly charge = 15 × ₹30 = ₹450.
- Daily maximum = ₹300.
- Parking fee = ₹300.
- One overnight period = ₹50.
- Lost ticket penalty = ₹0.
- Total fee = ₹300 + ₹50 = ₹350.
```Mermaid
Flowchart Code

flowchart TD
    A([Start]) --> B[/Enter vehicle number and category/]
    B --> C{Valid vehicle category?}

    C -- No --> D[Display invalid category]
    D --> Z([Stop])

    C -- Yes --> E[/Enter entry and exit date-time/]
    E --> F{Valid date and time?}

    F -- No --> G[Display input error]
    G --> Z

    F -- Yes --> H{Exit time after entry time?}
    H -- No --> I[Display invalid duration]
    I --> Z

    H -- Yes --> J[Calculate parking duration]
    J --> K[Calculate rounded parking hours]
    K --> L[Select vehicle hourly rate and daily limit]
    L --> M[Calculate parking fee]
    M --> N[Apply daily maximum]
    N --> O[Calculate overnight charge]
    O --> P{Ticket lost?}

    P -- Yes --> Q[Add lost ticket penalty]
    P -- No --> R[Penalty = 0]

    Q --> S[Calculate total fee]
    R --> S

    S --> T[Display parking receipt]
    T --> U([Stop])

```




8. Conclusion
The Smart Parking Fee Management System calculates parking charges automatically based on vehicle type, parking duration, overnight stays, daily limits, and penalty conditions.

Advantages:
- Reduces manual calculation errors.
- Supports multiple vehicle categories.
- Validates parking entry and exit times.
- Automatically applies daily parking limits.
- Calculates overnight and penalty charges.
- Provides a clear parking receipt.
Note: The parking rates and penalties used in this program are illustrative values for an academic project. The overnight rule counts calendar midnights crossed, and the daily limit resets after each 24-hour parking period.
