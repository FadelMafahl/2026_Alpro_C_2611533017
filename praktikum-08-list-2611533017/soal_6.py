LAST_DIGIT = 7  # change to the last digit of your NIM
daily_limit = 30000 + LAST_DIGIT * 1000
expenses = []
# Write your code below
total = 0
highest = 0
day_limit = 0

for i in range(7):
    pengeluaran = int(input(f"Day {i+1}: "))
    expenses.append(pengeluaran)
    total += pengeluaran
    if highest < pengeluaran:
        highest = pengeluaran
    if pengeluaran >= daily_limit:
        day_limit += 1

print(f"Daily limit: {daily_limit}")
print(f"Total: {total}")
print(f"Average: {total/7:.1f}")
print(f"Highest: day {expenses.index(highest)+1} ({highest})")
print(f"Days above limit: {day_limit}")