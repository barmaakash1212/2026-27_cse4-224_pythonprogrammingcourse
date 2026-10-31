# Warehouse Inventory Reconciliation System

print("WAREHOUSE INVENTORY RECONCILIATION")
print("----------------------------------")

n = int(input("Enter number of products: "))

total_discrepancy = 0
shortage_count = 0
surplus_count = 0

for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")

    opening = int(input("Enter opening stock: "))
    incoming = int(input("Enter incoming quantity: "))
    dispatched = int(input("Enter dispatched quantity: "))
    actual_closing = int(input("Enter actual closing stock: "))
    minimum_stock = int(input("Enter minimum stock level: "))

    expected_closing = opening + incoming - dispatched

    discrepancy = actual_closing - expected_closing

    if actual_closing < minimum_stock:
        replenishment = minimum_stock - actual_closing
    else:
        replenishment = 0

    total_discrepancy += abs(discrepancy)

    print("\n--- Inventory Report ---")
    print("Product Name:", name)
    print("Opening Stock:", opening)
    print("Incoming Stock:", incoming)
    print("Dispatched Stock:", dispatched)
    print("Expected Closing Stock:", expected_closing)
    print("Actual Closing Stock:", actual_closing)

    if discrepancy == 0:
        print("Stock Status: No Discrepancy")

    elif discrepancy < 0:
        print("Stock Status: Shortage of", abs(discrepancy))
        shortage_count += 1

    else:
        print("Stock Status: Surplus of", discrepancy)
        surplus_count += 1

    print("Minimum Stock Level:", minimum_stock)
    print("Replenishment Required:", replenishment)

print("\n================================")
print("FINAL WAREHOUSE SUMMARY")
print("================================")
print("Total Products:", n)
print("Products with Shortage:", shortage_count)
print("Products with Surplus:", surplus_count)
print("Total Absolute Discrepancy:", total_discrepancy)

print("\nInventory Reconciliation Completed.")
