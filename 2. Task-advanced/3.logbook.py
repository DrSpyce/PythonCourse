import datetime
import os


def add_log_entry(entry, file_name):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - {entry}\n"

    with open(file_name, "a") as file:
        file.write(log_entry)

    print(f"Log entry added: {log_entry}")


def display_log_entries(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            log_entries = file.readlines()

            if not log_entries:
                print("No log entries found.")
            else:
                print("Log Entries:")
                for log_entry in log_entries:
                    print(log_entry)
    else:
        print("No log file found.")


file_name = "logs.txt"
while True:
    print("\nCommand Menu:")
    print("1. Add Log Entry")
    print("2. Display Log Entries")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        entry = input("Enter your log entry: ")
        add_log_entry(entry, file_name)
    elif choice == "2":
        display_log_entries(file_name)
    elif choice == "3":
        print("Exiting.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")


