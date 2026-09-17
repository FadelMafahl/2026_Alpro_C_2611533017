angka1_3017 = int(input("input angka-1: "))
angka2_3017 = int(input("input angka-2: "))

# Penjumlahan
hasil = angka1_3017 + angka2_3017
print("\n0perator Penjumlahan")
print("Hasil =", hasil)

# Pengurangan
hasil = angka1_3017 - angka2_3017
print("\n0perator Pengurangan")
print("Hasil =", hasil)

# Perkalian
hasil = angka1_3017 * angka2_3017
print("\n0perator Perkalian")
print("Hasil =", hasil)

# Pembagian, Pembagian bulat, dan Sisa bagi
if angka2_3017 != 0:
    hasil = angka1_3017 / angka2_3017
    print("\n0perator Pembagian")
    print("Hasil =", hasil)

    hasil = angka1_3017 // angka2_3017
    print("\n0perator Pembagian bulat")
    print("Hasil =", hasil)

    hasil = angka1_3017 % angka2_3017
    print("\n0perator sisa bagi")
    print("Hasil =", hasil)
else:
    print("Angka kedua tidak boleh bernilai 0")

# Pangkat
hasil = angka1_3017 ** angka2_3017
print("\n0perator Pangkat")
print("Hasil =", hasil)