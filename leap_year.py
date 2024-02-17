print("This program will check if the year provided is a leap year or not.")

# Asks user for a year.
year = int(input("What year do you want to check? "))


def is_leap(year):
    """ Returns True if year is a leap year, else False """
    if year % 4 == 0:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        else:
            return True
    else:
        return False


print(f"{year} is a leap year.") if is_leap(year) else print(f"{year} is not a leap year.")
