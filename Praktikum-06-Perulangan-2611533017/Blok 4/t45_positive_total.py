total = 0
while True:
    number = int(input("Masukkan Angka: "))
    if number < 0:
        break
    if number == 2:
        continue
    print(f"Positive number: {number}")
    total += number
print(f"Total: {total}")