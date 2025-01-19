def safe_divide(numerator, denominator):
    try:
        float_numerator = float(numerator)
        float_denominator = float(denominator)
        if float_denominator != 0:
            result = float_numerator / float_denominator
            return f"The result of the division is {result}"
        else:
            raise ZeroDivisionError
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."
