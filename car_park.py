import csv
from datetime import datetime

# Set hourly parking fee
HOURLY_RATE = 100  # Adjust as needed

# File to store parking records
FILENAME = 'carpark.csv'

def calculate_parking_fee(entry_time, exit_time):
    fmt = "%Y-%m-%d %H:%M"
    start = datetime.strptime(entry_time, fmt)
    end = datetime.strptime(exit_time, fmt)
    duration = (end - start).total_seconds() / 3600  # Convert to hours
    duration = max(1, round(duration))  # Minimum 1 hour charge
    return duration, duration * HOURLY_RATE

def write_to_csv(record):
    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(record)

def main():
    print("=== Car Park Entry ===")
    vehicle_no = input("Enter vehicle number: ")
    entry_time = input("Enter entry time (YYYY-MM-DD HH:MM): ")
    exit_time = input("Enter exit time (YYYY-MM-DD HH:MM): ")

    duration, fee = calculate_parking_fee(entry_time, exit_time)

    record = [vehicle_no, entry_time, exit_time, duration, fee]
    write_to_csv(record)

    print(f"Parking Duration: {duration} hour(s)")
    print(f"Parking Fee: Ksh {fee}")

if __name__ == "__main__":
    # Create header if file doesn't exist
    try:
        with open(FILENAME, 'x', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Vehicle No', 'Entry Time', 'Exit Time', 'Hours', 'Fee'])
    except FileExistsError:
        pass  # File already exists, no need to add headers again

    main()