print("===================================")
print("3. OPERATOR BITWISE")
print("===================================")

angka1_3017 = int(input("Masukkan angka biatwise-1: "))
angka2_3017 = int(input("Masukkan angka biatwise-2: "))

print("\nAngka dalam bentuk desimal dan biner")
print("angka1 =", angka1_3017, "| biner =", bin(angka1_3017))
print("angka2 =", angka2_3017, "| biner =", bin(angka2_3017))

# Bitwise AND
hasil = angka1_3017 & angka2_3017
print("\nBitwise AND (&)")
print(angka1_3017, "&", angka2_3017, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise OR
hasil = angka1_3017 | angka2_3017
print("\nBitwise OR (|)")
print(angka1_3017, "|", angka2_3017, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise XOR
hasil = angka1_3017 ^ angka2_3017
print("\nBitwise AND (^)")
print(angka1_3017, "^", angka2_3017, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise NOT
hasil = ~angka1_3017
print("\nBitwise NOT (~)")
print(angka1_3017, "~", angka2_3017, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kiri
jumlah_geser = int(input("\nMasukkan jumlah pergeseran bit: "))

hasil = angka1_3017 << jumlah_geser
print("\nBitwise geser kiri (<<)")
print(angka1_3017, "<<", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))

# Bitwise geser kanan
hasil = angka1_3017 >> jumlah_geser
print("\nBitwise geser kiri (>>)")
print(angka1_3017, ">>", jumlah_geser, "=", hasil)
print("Biner hasil =", bin(hasil))
print("Biner hasil (8 bit) =", format(hasil, "08b"))