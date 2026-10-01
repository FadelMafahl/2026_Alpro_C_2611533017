ulang_3017 = int(input("Masukkan jumlah perulangan: "))

jumlah_3017 = 0
for i_3017 in range(1, ulang_3017 + 1):
    print(i_3017, end=" ")
    jumlah_3017 = jumlah_3017 + i_3017

    if i_3017 < ulang_3017:
        print(" + ", end="")
    else:
        print(" + ", jumlah_3017, end="")
print()
print("jumlah =", jumlah_3017)