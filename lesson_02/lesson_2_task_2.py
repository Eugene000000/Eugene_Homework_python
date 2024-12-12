def is_year_leap(year):
    if (year % 4 == 0):
        print("Год: " + str(year) + " True")
    else:
        print("Год: " + str(year) + " False")

year_check = 2024
result = is_year_leap(year_check)
