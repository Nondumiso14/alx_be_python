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

def calculate_future_date(days):
    """
    Calculate the future date after adding the specified number of days to the current date.

    Parameters:
        days (int): Number of days to add.

    Prints:
        The future date in the format 'YYYY-MM-DD'.
    """
    # Save the current date and time
    current_date = datetime.now()
    
    # Calculate the future date
     days_to_add = int(input("Enter the number of days to cdd to the current  date: "))
    future_date = current_date + timedelta(days=days_to_add)

    # Format the future date
    formatted_future_date = future_date.strftime('%Y-%m-%d')

    # Print the future date
    print(f"Future Date: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()

    # Prompt the user for the number of days
    try:
        days_to_add = int(input("Enter the number of days to cdd to the current  date: "))
        calculate_future_date(days_to_add)
    except ValueError:
        print("Please enter a valid integer for the number of days.")

