menus = ["Nasi Goreng", "Mie Ayam", "Soto"]
number_of_days = 3
sales = []
# Write your code below
for day in range(number_of_days):
    row = []
    for menu in menus:
        portions = int(input("Day " + str(day + 1) + ", " + menu + ": "))
        row.append(portions)
    sales.append(row)

print("Total per day:")
for day in range(number_of_days):
    day_total = 0
    for portions in sales[day]:
        day_total += portions
    print("Day " + str(day + 1) + ": " + str(day_total))

menu_totals = []
for col in range(len(menus)):
    menu_total = 0
    for row in range(number_of_days):
        menu_total += sales[row][col]
    menu_totals.append((menus[col], menu_total))
print("Total per menu:", menu_totals)

best_name = ""
best_total = -1
for name, total in menu_totals:
    if total > best_total:
        best_name = name
        best_total = total
print("Best seller: " + best_name + " (" + str(best_total) + ")")