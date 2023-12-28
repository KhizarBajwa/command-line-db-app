# main.py

import os
import sys
import datetime
from database import Database
from colorama import Fore, Style, init

# Initialize colorama for colored output
init(autoreset=True)

def print_commands():
    print(f"\n{Fore.BLUE}Available Commands:{Style.RESET_ALL}")
    print(f"1. {Fore.CYAN}Fetch all users{Style.RESET_ALL}")
    print(f"2. {Fore.CYAN}Insert a new user{Style.RESET_ALL}")
    print(f"3. {Fore.CYAN}Update user email{Style.RESET_ALL}")
    print(f"4. {Fore.CYAN}Delete a user{Style.RESET_ALL}")
    print(f"5. {Fore.CYAN}Fetch orders by user{Style.RESET_ALL}")
    print(f"6. {Fore.RED}Execute custom query{Style.RESET_ALL}")
    print(f"7. {Fore.RED}Display Application Info{Style.RESET_ALL}")
    print(f"8. {Fore.RED}Exit{Style.RESET_ALL}")

def execute_custom_query(db):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print("\nTables:")
    tables = db.get_table_names()
    for table in tables:
        print(f"{table}")

    user_query = input(f"\nEnter your custom SQL query:{Fore.GREEN} ")
    result = db.execute_custom_query(user_query)
    
    if result is not None:
        print(f"\n{Fore.BLUE}Query Result:{Style.RESET_ALL}")
        for row in result:
            print(row)

    input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

def display_info(db):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    tables = db.get_table_names()
    operations = 6  # Update this count if more operations are added in the future
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    info_text = f" Application Information:\n Number of Tables: {len(tables)}\n Number of Operations: {operations}\n Date and Time: {date_time} "
    
    box_width = max(len(line) for line in info_text.splitlines()) + 4
    separator = "+" + "-" * (box_width - 2) + "+"

    print(f"\n{Fore.BLUE}{separator}{Style.RESET_ALL}")
    print(f"{Fore.BLUE}|{Style.RESET_ALL}{info_text.center(box_width - 2)}{Fore.BLUE}|{Style.RESET_ALL}")
    print(f"{Fore.BLUE}{separator}{Style.RESET_ALL}")

    input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

def display_help():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
    print(f"\n{Fore.BLUE}Command-Line Database Application Help:{Style.RESET_ALL}")
    print("\nUsage:")
    print("python main.py [options]")
    print("\nOptions:")
    print("-h, --help    : Display this help message")
    print("\nCommands:")
    print_commands()

# Instantiate the Database class
db = Database("app.db")

if len(sys.argv) > 1:
    if sys.argv[1] in ['-h', '--help']:
        display_help()

while True:
    # os.system('cls' if os.name == 'nt' else 'clear')  # Do not clear screen here
    # print_commands()

    user_input = input(f"\n{Fore.GREEN}Enter the command number (or type '-h' for help):{Style.RESET_ALL} ")

    if user_input in ['-h', '--help']:
        display_help()
        continue

    if user_input == "1":
        users = db.fetch_all("users")
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the terminal screen
        print(f"\n{Fore.BLUE}All Users:{Style.RESET_ALL}")
        for user in users:
            print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

        input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

    # ... (rest of the commands)
    elif user_input == "2":
        name = input(f"{Fore.GREEN}Enter user name:{Style.RESET_ALL} ")
        email = input(f"{Fore.GREEN}Enter user email:{Style.RESET_ALL} ")
        db.insert_user(name, email)
        print(f"\n{Fore.GREEN}User inserted successfully!{Style.RESET_ALL}")

        input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

    elif user_input == "3":
        user_id = input(f"{Fore.GREEN}Enter user ID:{Style.RESET_ALL} ")
        new_email = input(f"{Fore.GREEN}Enter new email:{Style.RESET_ALL} ")
        db.update_user_email(user_id, new_email)
        print(f"\n{Fore.GREEN}User email updated successfully!{Style.RESET_ALL}")

        input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

    elif user_input == "4":
        user_id = input(f"{Fore.GREEN}Enter user ID to delete:{Style.RESET_ALL} ")
        db.delete_user(user_id)
        print(f"\n{Fore.GREEN}User deleted successfully!{Style.RESET_ALL}")

        input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

    elif user_input == "5":
        user_id = input(f"{Fore.GREEN}Enter user ID to fetch orders:{Style.RESET_ALL} ")
        orders = db.fetch_orders_by_user(user_id)
        print(f"\n{Fore.BLUE}Orders for User:{Style.RESET_ALL}")
        for order in orders:
            print(f"Order ID: {order[0]}, Product: {order[2]}, Quantity: {order[3]}")

        input("\nPress Enter to continue...")  # Wait for user input before clearing the screen

    elif user_input == "6":
        execute_custom_query(db)

    elif user_input == "7":
        display_info(db)

    elif user_input == "8":
        print(f"\n{Fore.RED}Exiting the program. Goodbye!{Style.RESET_ALL}")
        break

    else:
        print(f"\n{Fore.RED}Invalid command. Please enter a valid command number.{Style.RESET_ALL}")

    # os.system('cls' if os.name == 'nt' else 'clear')  # Do not clear screen here
