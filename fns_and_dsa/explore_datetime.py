from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in the format 'YYYY-MM-DD HH:MM:SS'.
    """
    # Save the current date and time
    current_date = datetime.now()
    
    # Format the date and time
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
    
    # Print the formatted date and time
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date(current_date,days):
    future_date = current_date + timedelta (days=days)
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    # Print the future date
    print(f"Future Date after {days} days: {formatted_future_date}")
    return future_date

def main():
    current_date = display_current_datetime()

    try:
       days = int(input("Enter the number of days to cdd to the current  date: "))
       calculate_future_date(current_date, days)
    except ValueError:
        print("Invalid input. Please enter an interger value for the number of days.")

if __name__ == "__main__":
    main()

    
    
    
    
    


