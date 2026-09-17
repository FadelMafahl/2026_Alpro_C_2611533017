angka1_3017 = int(input("Input angka-1:"))
angka2_3017 = int(input("Input angka-2:"))

# Assigment biasa
hasil = angka1_3017
print("\nAssigment biasa (=)")
print("Hasil =", hasil)

# Assigment penambahan 
hasil = angka1_3017
hasil += angka2_3017
print("\nAssigment penambahan (+=)")
print("Hasil =", hasil)

# Assigment pengurangan 
hasil = angka1_3017
hasil -= angka2_3017
print("\nAssigment pengurangan (-=)")
print("Hasil =", hasil)

# Assigment perkalian
hasil = angka1_3017
hasil *= angka2_3017
print("\nAssigment penambahan (*=)")
print("Hasil =", hasil)

# Assigment pembagian, pembagian bulat, dan sisa bagi
if angka2_3017 != 0:
    hasil = angka1_3017
    hasil /= angka2_3017
    print("\nAssigment pembagian (/=)")
    print("Hasil =", hasil)
    # Operator Tambahan
    hasil = angka1_3017
    hasil //= angka2_3017
    print("\nAssigment pembagian bulat (//=)")
    print("Hasil =", hasil)
    hasil = angka1_3017
    hasil %= angka2_3017
    print("\nAssigment sisa bagi (%=)")
    print("Hasil =", hasil)
else: 
    print("\nPembagian tidak dapat dilakukan.")
    print("Angka kedua tidak boleh bernilai 0.")

# Operator tambahan: assigment perpangkatan
hasil = angka1_3017
hasil **= angka2_3017
print("\nAssigment perpangkatan (**=)")
print("Hasil =", hasil)