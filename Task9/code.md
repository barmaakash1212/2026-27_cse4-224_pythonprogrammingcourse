Warehouse Inventory Reconciliation System – Python Program
1. Problem Statement
Develop a Warehouse Inventory Reconciliation System to compare the opening stock, incoming quantities, dispatched quantities, and actual closing stock of multiple products.

The system should:
1. Accept the number of products.
2. Read each product's name, opening stock, incoming quantity, dispatched quantity, and actual closing stock.
3. Calculate the expected closing stock using:
Expected Closing Stock = Opening Stock + Incoming Stock − Dispatched Stock
4. Compare expected closing stock with actual closing stock.
5. Identify and report stock discrepancies.
6. Calculate replenishment requirements based on the minimum stock level.
7. Display a complete inventory reconciliation report.
2. Algorithm
1. Start the program.
2. Read the number of products.
3. Initialize total discrepancy and product counters.
4. For each product:
   - Read product name.
   - Read opening stock.
   - Read incoming quantity.
   - Read dispatched quantity.
   - Read actual closing stock.
   - Read minimum stock level.
5. Calculate expected closing stock.
6. Compare expected stock with actual closing stock.
7. Calculate discrepancy:
   - If actual stock is greater than expected stock, report surplus.
   - If actual stock is less than expected stock, report shortage.
   - Otherwise, report no discrepancy.
8. Compare actual closing stock with minimum stock level.
9. Calculate replenishment quantity if actual stock is below minimum stock.
10. Display the reconciliation report.
11. Stop.


5. Sample Input
Enter number of products: 3

Product 1
Enter product name: Rice
Enter opening stock: 100
Enter incoming quantity: 50
Enter dispatched quantity: 80
Enter actual closing stock: 65
Enter minimum stock level: 80

Product 2
Enter product name: Wheat
Enter opening stock: 200
Enter incoming quantity: 100
Enter dispatched quantity: 120
Enter actual closing stock: 180
Enter minimum stock level: 100

Product 3
Enter product name: Sugar
Enter opening stock: 150
Enter incoming quantity: 50
Enter dispatched quantity: 70
Enter actual closing stock: 120
Enter minimum stock level: 130


6. Sample Output
WAREHOUSE INVENTORY RECONCILIATION
----------------------------------

--- Inventory Report ---
Product Name: Rice
Opening Stock: 100
Incoming Stock: 50
Dispatched Stock: 80
Expected Closing Stock: 70
Actual Closing Stock: 65
Stock Status: Shortage of 5
Minimum Stock Level: 80
Replenishment Required: 15

--- Inventory Report ---
Product Name: Wheat
Opening Stock: 200
Incoming Stock: 100
Dispatched Stock: 120
Expected Closing Stock: 180
Actual Closing Stock: 180
Stock Status: No Discrepancy
Minimum Stock Level: 100
Replenishment Required: 0

--- Inventory Report ---
Product Name: Sugar
Opening Stock: 150
Incoming Stock: 50
Dispatched Stock: 70
Expected Closing Stock: 130
Actual Closing Stock: 120
Stock Status: Shortage of 10
Minimum Stock Level: 130
Replenishment Required: 10

================================
FINAL WAREHOUSE SUMMARY
================================
Total Products: 3
Products with Shortage: 2
Products with Surplus: 0
Total Absolute Discrepancy: 15

Inventory Reconciliation Completed.


```Mermaid
Flowchart Code

flowchart TD
    A([Start]) --> B[/Enter number of products/]
    B --> C[Initialize counters]
    C --> D[/Enter product details/]
    D --> E[Calculate expected closing stock]
    E --> F[Calculate discrepancy]
    F --> G{Actual stock equals expected stock?}

    G -- Yes --> H[No discrepancy]
    G -- No --> I{Actual stock less than expected?}

    I -- Yes --> J[Report stock shortage]
    I -- No --> K[Report stock surplus]

    H --> L{Actual stock below minimum level?}
    J --> L
    K --> L

    L -- Yes --> M[Calculate replenishment quantity]
    L -- No --> N[Replenishment = 0]

    M --> O[Display product report]
    N --> O

    O --> P{More products?}
    P -- Yes --> D
    P -- No --> Q[Display final summary]
    Q --> R([Stop])

```




8. Conclusion
The Warehouse Inventory Reconciliation System helps warehouse managers maintain accurate stock records by comparing expected and actual stock quantities. It identifies shortages and surpluses and calculates the quantity required to replenish products below their minimum stock levels.

Advantages:
- Reduces inventory errors.
- Identifies missing or excess stock.
- Helps maintain minimum stock levels.
- Supports better warehouse management.
- Reduces the risk of running out of products.
