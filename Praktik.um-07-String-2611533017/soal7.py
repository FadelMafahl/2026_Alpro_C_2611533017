# Name: Fadel Muhammad Naufal
# NIM: 2611533017
# Question 7

name = "fadel muhammad naufal"
nim = "2611533017"

pos = name.find(" ")
if pos == -1:
    first_name = name
else:
    first_name = name[:pos]
username = first_name + nim[-3:]

intake = "20" + nim[:2]

print("=" * 30)
print("STUDENT CARD".center(30))
print("=" * 30)
print("Name".ljust(10) + ": " + name.title())
print("Nim".ljust(10) + ": " + nim)
print("Username".ljust(10) + ": " + username)
print("Intake".ljust(10) + ": " + intake)
print("=" * 30)