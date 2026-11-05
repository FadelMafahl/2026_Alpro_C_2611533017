total = 0
while True:
    number = int(input("Masukkan Angka: "))
    if number < 0:
        break
    total += number
    if number == 0:
        continue
    print("Positive number:",number)
print("Total:",total)