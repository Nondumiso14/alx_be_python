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
    print(f"Current date and time: {formatted_date}")
    
    
def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    # Print the future date
    print(f"Future date: {formatted_future_date}")
    
def main():
    display_current_datetime()

    days = int(input("Enter the number of days to cdd to the current  date: "))
    calculate_future_date(days)

if _name_ == "_main_":
    main()






    
    
    
    
    


