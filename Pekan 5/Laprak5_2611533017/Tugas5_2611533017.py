print("=== PROGRAM JAM PASIR KRISTAL PALINDROMIK ===")
n_3017 = int(input("Masukkan ukuran skala jam pasir: "))

# ===== Bingkai atas =====
print("#", end="")
for b_3017 in range(4 * n_3017 + 5):
    print("=", end="")
print("#")

# ===== Fase 1: Jam pasir atas (N turun sampai 1) =====
for baris_3017 in range(n_3017, 0, -1):
    print("| ", end="")

    # spasi penyeimbang kiri
    for spasi_3017 in range(2 * (n_3017 - baris_3017)):
        print(" ", end="")

    # deret angka mundur
    for angka_3017 in range(baris_3017, 0, -1):
        print(angka_3017, end=" ")

    # poros kristal
    print("<M>", end="")

    # deret angka maju
    for angka_3017 in range(1, baris_3017 + 1):
        print(" ", angka_3017, sep="", end="")

    # spasi penyeimbang kanan
    for spasi_3017 in range(2 * (n_3017 - baris_3017)):
        print(" ", end="")

    print(" |", end="")
    print()

# ===== Fase 2: Poros titik pusat =====
print("|", end="")
for spasi_3017 in range(2 * n_3017 + 1):
    print(" ", end="")
print("<X>", end="")
for spasi_3017 in range(2 * n_3017 + 1):
    print(" ", end="")
print("|", end="")
print()

# ===== Fase 3: Jam pasir bawah (1 naik sampai N) =====
for baris_3017 in range(1, n_3017 + 1):
    print("| ", end="")

    # spasi penyeimbang kiri
    for spasi_3017 in range(2 * (n_3017 - baris_3017)):
        print(" ", end="")

    # deret angka mundur
    for angka_3017 in range(baris_3017, 0, -1):
        print(angka_3017, end=" ")

    # poros kristal
    print("<M>", end="")

    # deret angka maju
    for angka_3017 in range(1, baris_3017 + 1):
        print(" ", angka_3017, sep="", end="")

    # spasi penyeimbang kanan
    for spasi_3017 in range(2 * (n_3017 - baris_3017)):
        print(" ", end="")

    print(" |", end="")
    print()

# ===== Bingkai bawah =====
print("#", end="")
for b_3017 in range(4 * n_3017 + 5):
    print("=", end="")
print("#")