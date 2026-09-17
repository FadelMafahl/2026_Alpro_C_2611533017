print("===================================")
print("1. OPERATOR KEANGGOTAAN")
print("===================================")

# Input beberapa data yang dipisahkan dengan koma
input_data = input ("Masukkan beberapa angka, pisahkan dengan koma: ")

# Mengubah Input menjadi list interger
data_3017 = [int(angka.strip()) for angka in input_data.split(",")]

nilai_dicari = int(input("Masukkan angka yang ingin dicari: "))

# Operator in
hasil = nilai_dicari in data_3017
print("\n0perator keanggotaan IN")
print(nilai_dicari, "in", data_3017, "=", hasil)

# Operator not in
hasil = nilai_dicari not in data_3017
print("\n0perator keanggotaan NOT IN")
print(nilai_dicari, "not in", data_3017, "=", hasil)

print("\n===================================")
print("2. OPERATOR IDENTITAS")
print("===================================")

# Objek1 menggunakan list dari input pengguna
objek1_3017 = data_3017

# Objek2 merujuk pada objek yang sama dengan objek1
objek2_3017 = objek1_3017

# Objek3 memiliki isi sama, tetapi merupakan objek baru
objek3_3017 = data_3017.copy()

print("objek1 =", objek1_3017)
print("objek2 =", objek2_3017)
print("objek3 =", objek3_3017)

# Operator is
hasil = objek1_3017 is objek2_3017
print("\n0perator identitas IS")
print("objek1 is objek2 =", hasil)

# Operator is not
hasil = objek1_3017 is not objek3_3017
print("\n0perator identitas IS NOT")
print("objek1 is objek3 =", hasil)

# Membandingkan indentitas dan nilai
print("\nPerbandingan identitas dan nilai")
print("objek1 is objek3 =", objek1_3017 is objek3_3017)
print("objek1 == objek3 =", objek1_3017 == objek3_3017)