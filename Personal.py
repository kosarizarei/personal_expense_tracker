from datetime import date
import json

print()
print("Welcome to small Personal Expense Tracker! ✌️\n".center(140))
print("Please enter your amounts follow the orders\n".center(130))

# Load expenses from file
try:
    with open("expenses.json", "r", encoding="utf-8") as f:
        expenses = json.load(f)
except FileNotFoundError:
    expenses = []   

def expensivest_of_month():

    now = date.today()
    year = now.year
    month = now.month

    daily_total = {}
    
    for exp in expenses:
        exp_date = exp.get("date")
        y, m, d = exp_date.split("-")

        if int(y) == year and int(m) == month:
            if exp_date not in daily_total:
                daily_total[exp_date] = 0

            daily_total[exp_date] += exp["amount"]
    if not daily_total:
        print("\nThere is no any amounts for this month\n")
        return
    
    max_day = max(daily_total, key=daily_total.get)
    max_amount = daily_total[max_day]

    print(f"\nMost expensive day on this month is :{max_day}")
    print(f"\nTotal expenses are: {max_amount}\n")
    for i in expenses:
        if i["date"] == max_day:
            print(f"- {i['category']}: {i['amount']:,} ({i.get('desc','')})\n")

def Submition_of_categories(category = None):

    total = 0
    for exp in expenses:
        if exp["category"] == category:
            total += exp["amount"]
    print(f"You expend {total} on {category}\n")

def expenses_by_date(str_date = None):
    if str_date is None:
        str_date = date.today().strftime("%Y-%m-%d")

    totall = 0
    found = False
    for i in expenses:
        if i["date"] == str_date:
            print(f"\namount {i['amount']:,} for {i['category']}")
            totall += i["amount"]
            found = True

    if found:
        print(f"Totall expenses are: {totall}")
    else:
        print(f"Not expenses on {'str_date'}\n")

while True:
    # Get input from user

    cost = int(input("Enter amount : "))
    cat = input("Enter category (food, transport, fun, savings): ")
    date_amount = input("Enter date (YYYY-MM-DD): ")
    desc = input("Enter description (optional): ")

    # Add new expense and save
    new_expense = {
        "amount": cost,
        "category": cat,
        "date": date_amount,
        "desc": desc
    }
    expenses.append(new_expense)

    # Save back to file
    with open("expenses.json", "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)

    x = input("\n Do you have more amount? Y/N? \n")
    if x == "N" or x == "n":
        while True:
            print("I can show you below orders; you just need to enter that number.\n")
            x = input("1- Most expensive day on this month\n2- Sumation of spetial category\n3- All amounts of petecillar day\n4- Exit\n :")

            if x == "1":
                expensivest_of_month()
            
            elif x == "2":
                category = input("\nPlease enter your category: ")
                Submition_of_categories(category)

            elif x == "3":
                day = input("Enter the date (YYYY-MM-DD): ")
                expenses_by_date(day)

            else:
                break
        break

now = date.today().strftime("%Y-%m-%d")

print(f"Total expenses: {len(expenses)} items")