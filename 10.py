with open('/Users/altanazambaldorzieva/Desktop/input.txt', 'r') as file:
    current_date = file.readline().strip()
    n = int(file.readline().strip())
    cell_data = [line.strip().split() for line in file.readlines()]


def days_difference(date1, date2):
    day1, month1 = map(int, date1.split('.'))
    day2, month2 = map(int, date2.split('.'))
    days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    if month1 == month2:
        return abs(day2 - day1)
    days = days_in_month[month1] - day1 + day2
    for m in range(month1+1, month2):
        days += days_in_month[m]
    return days


result = []
for cell, date in cell_data:
    days_stored = days_difference(date, current_date)
    if days_stored > 3:
        result.append(cell)
with open('/Users/altanazambaldorzieva/Desktop/output.txt', 'w') as file:
    for cell in result:
        file.write(f"{cell}\n")
