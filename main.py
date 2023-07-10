import math


def main():
    date_1 = input('Enter the first date (MM/DD/YY): \n')
    date_1 = date_1.split('/')
    date_1 = [int(x) for x in date_1]  # convert string to int array
    date_2 = input('Enter the second date (MM/DD/YY): \n')
    date_2 = date_2.split('/')
    date_2 = [int(x) for x in date_2]  # convert string to int array

    print('Choose an output option:')
    option = input('1 = Years + Months + Weeks + Days, 2 = Months + Weeks + Days, 3 = Weeks + Days, 4 = Days\n')
    option = int(option)  # convert string to int
    time_diff = convert_time(option, date_1, date_2)
    formatted_time_diff = format_time(time_diff, option)
    print(*formatted_time_diff, sep=', ')
    # optional: check for valid inputs


def check_leap_year(year):
    if year < 0:
        return False
    if year % 4 == 0: # first check
        if (year % 100 == 0) and (year % 400 != 0):  # second check
            return False
        return True
    return False


def find_day_in_year(date):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 0
    for month in range(date[0] - 1):
        if month == 3 and check_leap_year(date[2]):  # april case
            day += days[month] + 1
        else:
            day += days[month]
    day += date[1]
    return day


def find_diff_between_months(month_1, day_1, day_2):
    # fix this
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if day_1 > day_2:
        return (days[month_1 - 1] - day_1) + day_2
    else:
        return day_2 - day_1


def convert_time(option, date_1, date_2):
    day_1 = find_day_in_year(date_1)
    day_2 = find_day_in_year(date_2)
    if date_1[2] > date_2[2] or day_1 > day_2:  # find larger of the two dates
        temp_date = date_1
        date_1 = date_2
        date_2 = temp_date
        temp_day = day_1
        day_1 = day_2
        day_2 = temp_day
    days_diff = day_2 - day_1
    years_diff = date_2[2] - date_1[2]
    if date_2[0] - date_1[0] < 0:
        years_diff -= 1
    months_diff = date_2[0] - date_1[0]
    if date_2[1] - date_1[1] < 0:
        months_diff -= 1

    time_diff = [0] * 4
    if option == 1:
        time_diff[0] = years_diff
    if option <= 2:
        time_diff[1] = months_diff
        days_diff = find_diff_between_months(date_1[0], date_1[1], date_2[1])
    if option <= 3:
        time_diff[2] = math.floor(days_diff / 7)
        days_diff = days_diff % 7
    time_diff[3] = days_diff
    return time_diff


def format_time(time_diff, option):
    formatted_time = []
    if option == 1:
        formatted_time.append(str(time_diff[0]) + ' Years')
    if option <= 2:
        formatted_time.append(str(time_diff[1]) + ' Months')
    if option <= 3:
        formatted_time.append(str(time_diff[2]) + ' Weeks')
    formatted_time.append(str(time_diff[3]) + ' Days')
    for i in range(len(time_diff)):
        if time_diff[i] == 1:  # remove plural from string
            formatted_time[i] = formatted_time[i][:-1]
    return formatted_time


if __name__ == "__main__":
    main()