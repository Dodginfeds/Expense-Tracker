import csv
import os

# ------------------------------- #
#          Expense Tracker        #
# ------------------------------- #
# This program allows users to:
# 1. Add new expenses to a file (CSV format for structured storage).
# 2. View all expenses in a readable format.
# 3. Append new expenses to an existing file.
# 4. Calculate total expenses from the file.
# 5. Interact through a simple menu-driven system.

# -------------------------------
# Function to Write (Create) a New Expense File
# -------------------------------
def write():
    """
    Creates a new expense file or appends an entry to an existing one.
    The data is stored in CSV format (comma-separated values).
    """
    file_name = input("Enter a name for your expense file: ")
    if not file_name.endswith(".csv"):
        file_name += ".csv"

    expense = input("Enter the name of the expense: ")
    price = input("Enter the price of the expense: ")
    date = input("Enter the date (YYYY-MM-DD): ")

    try:
        # Check if the file exists to determine if headers need to be written
        file_exists = os.path.isfile(file_name)
        with open(file_name, mode="a", newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(["Date", "Expense", "Price"])  # Write headers only if new file
            writer.writerow([date, expense, price])
            print(f"Expense added to '{file_name}'!")
    except Exception as e:
        print(f"Error: {e}")

# -------------------------------
# Function to Read and Display Expenses
# -------------------------------
def read():
    """
    Reads and displays all expenses from a CSV file in a structured format.
    """
    file_name = input("Enter the expense file name: ")

    try:
        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            print("\n--- Expense List ---")
            for row in reader:
                print(f"{row[0]:<15} | {row[1]:<20} | ${row[2]:<10}")
            print("-" * 50)
    except FileNotFoundError:
        print("This file does not exist!")

# -------------------------------
# Function to Append a New Expense to an Existing File
# -------------------------------
def add():
    """
    Adds a new expense to an existing file, allowing users to also add notes.
    """
    file_name = input("Enter the name of the file you'd like to add to: ")
    
    new_expense = input("Enter the name of the new expense: ")
    new_price = input("Enter the price of the expense: ")
    new_date = input("Enter the date (YYYY-MM-DD): ")

    try:
        with open(file_name, mode="a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([new_date, new_expense, new_price])
            print("Your new expense has been added!")
    except FileNotFoundError:
        print("This file does not exist!")

# -------------------------------
# Function to Calculate Total Expenses
# -------------------------------
def calculate_total():
    """
    Calculates the total sum of all expenses in a given CSV file.
    """
    file_name = input("Enter the file name to calculate total expenses: ")

    try:
        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            total = sum(float(row[2]) for row in reader)  # Extract and sum price values
            print(f"\nTotal Expenses: ${total:.2f}")
    except FileNotFoundError:
        print("This file does not exist!")
    except ValueError:
        print("Error in reading price values! Ensure prices are valid numbers.")

# -------------------------------
# Main Menu System
# -------------------------------
def main_menu():
    """
    Displays the main menu and allows users to interact with the program.
    """
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add New Expense")
        print("2. View All Expenses")
        print("3. Append New Expense")
        print("4. Calculate Total Expenses")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            write()
        elif choice == 2:
            read()
        elif choice == 3:
            add()
        elif choice == 4:
            calculate_total()
        elif choice == 5:
            print("Thank you for using the Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

# -------------------------------
# Program Entry Point
# -------------------------------
if __name__ == "__main__":
    main_menu()
