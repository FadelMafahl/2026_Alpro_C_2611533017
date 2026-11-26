# Name: Fadel Muhammad Naufal
# NIM: 2611533017
# Question 4

phone = "081234567890"
masked = phone[:4] + "*" * (len(phone)-7) + phone[-3:]
print(masked)

phone = "08123456789"
masked = phone[:4] + "*" * (len(phone)-7) + phone[-3:]
print(masked)

phone = "0812345678"
masked = phone[:4] + "*" * (len(phone)-7) + phone[-3:]
print(masked)

phone = "082611533017"
masked = phone[:4] + "*" * (len(phone)-7) + phone[-3:]
print(masked)