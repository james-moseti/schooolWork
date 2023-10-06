# JAMES MOSETI MOTURI
# SCT211-0095/2022

year_to_check = int(input("Enter a year to check whether its a leap year or not: "))

if (year_to_check % 4) == 0:
    if (year_to_check % 100) == 0:
        if (year_to_check % 400) == 0:
            print(f"{year_to_check} has 366 days hence it's a leap year. ")
        else:
            print(f"{year_to_check} is not a leap year. ")
    else:
        print(f"{year_to_check} has 366 days hence it's a leap year. ")
else:
    print(f"{year_to_check} is not a leap year. ")
