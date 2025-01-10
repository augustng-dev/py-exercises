def catch_zero_division():
    try:
        return 10 / 0
    except ZeroDivisionError:
        print("division by zero!")

# Example usage
catch_zero_division()