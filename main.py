import time
from colorama import Fore, Style, init
from tqdm import tqdm

# Initialize colorama
init()

# Function to print colored text
def print_color(text, color):
    print(color + text + Style.RESET_ALL)

# Function to calculate the budget plan
def calculate_budget():
    print_color(banner, Fore.BLUE)
    
    # Gather user inputs
    income = float(input("Enter your monthly income: $"))
    expenses = float(input("Enter your total monthly expenses: $"))
    
    # Calculate available funds
    available_funds = income - expenses
    
    # Get allocation percentages from the user
    print("\nEnter the desired allocation percentages for the following spending categories:")
    savings_percentage = float(input("Savings: "))
    entertainment_percentage = float(input("Entertainment: "))
    transportation_percentage = float(input("Transportation: "))
    other_percentage = float(input("Other: "))
    
    # Calculate budgeted amounts based on the allocation percentages
    savings = available_funds * savings_percentage / 100
    entertainment = available_funds * entertainment_percentage / 100
    transportation = available_funds * transportation_percentage / 100
    other = available_funds * other_percentage / 100
    
    # Display the budgeting plan with loading bars
    print("\n--- Your Budgeting Plan ---")
    time.sleep(1)  # Add a small delay for visual effect
    
    print_color("\nSavings: ", Fore.LIGHTCYAN_EX)
    for _ in tqdm(range(int(savings)), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTCYAN_EX, Style.RESET_ALL)):
        time.sleep(0.02)
    
    print_color("\nEntertainment: ", Fore.LIGHTCYAN_EX)
    for _ in tqdm(range(int(entertainment)), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTCYAN_EX, Style.RESET_ALL)):
        time.sleep(0.02)
    
    print_color("\nTransportation: ", Fore.LIGHTCYAN_EX)
    for _ in tqdm(range(int(transportation)), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTCYAN_EX, Style.RESET_ALL)):
        time.sleep(0.02)
    
    print_color("\nOther: ", Fore.LIGHTCYAN_EX)
    for _ in tqdm(range(int(other)), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.LIGHTCYAN_EX, Style.RESET_ALL)):
        time.sleep(0.02)
    
    # Offer the option to adjust the budget
    print("\nWould you like to adjust your budget? (yes/no)")
    adjust_budget = input("> ").lower()
    
    if adjust_budget == "yes":
        calculate_budget()
    else:
        print_color("Thank you for using the budgeting tool!", Fore.CYAN)

# Run the budgeting tool
calculate_budget()
