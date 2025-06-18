import csv
from datetime import datetime
import os

DATA_FILE = "data/expenses.csv"

def add_expense(amount, category, description=""):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), amount, category, description])

def view_expenses():
    if not os.path.exists(DATA_FILE):
        print("No expenses found.")
        return
    with open(DATA_FILE, newline='') as file:
        reader = csv.reader(file)
        print("\nDate & Time\t\tAmount\tCategory\tDescription")
        print("-"*50)
        for row in reader:
            print("\t".join(row))

def generate_summary():
    if not os.path.exists(DATA_FILE):
        print("No expenses to summarize.")
        return

    summary = {}
    total = 0
    with open(DATA_FILE, newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            amount = float(row[1])
            category = row[2]
            summary[category] = summary.get(category, 0) + amount
            total += amount

    os.makedirs("reports", exist_ok=True)
    with open("reports/summary.txt", "w") as report:
        report.write(f"📊 Expense Summary Report\n\nTotal Spent: ${total:.2f}\n\nBreakdown by Category:\n")
        for category, amt in summary.items():
            report.write(f"- {category}: ${amt:.2f}\n")

    print("Summary report generated: reports/summary.txt")
