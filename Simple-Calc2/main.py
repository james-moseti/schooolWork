# JAMES MOSETI MOTURI
# SCT211-0095/2022

year_of_birth = int(input("Enter your year of birth (e.g., 1990): "))

from datetime import datetime
current_date = datetime.now()

age_years = current_date.year - year_of_birth

current_month = current_date.month
current_day = current_date.day
birth_month = 1  # Assume birth month is January
birth_day = 1    # Assume birthday is the 1st

age_months = current_month - birth_month
age_days = current_day - birth_day

print(f"Your age is {age_years} years, {age_months} months, and {age_days} days.")
