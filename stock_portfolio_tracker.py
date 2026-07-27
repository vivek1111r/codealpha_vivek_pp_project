# ==============================
# Stock Portfolio Tracker
# CodeAlpha Internship - Task 2
# ==============================

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOGLE": 170,
    "AMZN": 200
}

total_investment = 0

print("===================================")
print("     STOCK PORTFOLIO TRACKER")
print("===================================")

while True:
    stock_name = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        try:
            quantity = int(input("Enter Quantity: "))

            if quantity <= 0:
                print("Quantity must be greater than 0!")
                continue

            price = stocks[stock_name]
            investment = price * quantity
            total_investment += investment

            print("\n------ Investment Details ------")
            print("Stock Name :", stock_name)
            print("Price      : $", price)
            print("Quantity   :", quantity)
            print("Investment : $", investment)

        except ValueError:
            print("Please enter a valid number.")

    else:
        print("Invalid Stock Name!")
        print("Available Stocks:", ", ".join(stocks.keys()))

print("\n===================================")
print("Total Investment = $", total_investment)
print("===================================")

# Save result in a text file
try:
    with open("investment.txt", "w") as file:
        file.write("Stock Portfolio Tracker\n")
        file.write("=========================\n")
        file.write(f"Total Investment = ${total_investment}\n")

    print("Result saved successfully in investment.txt")

except Exception as e:
    print("Could not save file:", e)