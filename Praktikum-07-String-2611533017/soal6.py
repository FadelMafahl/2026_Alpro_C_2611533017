# Name: Fadel Muhammad Naufal
# NIM: 2611533017
# Question 6

full_name = "  siti Aisyah  "
nim = "2610511023"

name = full_name.strip()
pos = name.find(" ")

if pos == -1:
    first_name = name
else:
    first_name = name [:pos]

username = first_name.lower() + nim [-3:]
print(username)

# Build the username: first name in lowercase + last 3 digits of the NIM.
# Do not use split().