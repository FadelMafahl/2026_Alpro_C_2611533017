tinggi_3017 = int(input("Masukkan tinggi pola (bilangan genap, misal 10): "))

if tinggi_3017 % 2 != 0:
    print("Tinggi harus bilangan genap!")
else:
    a_3017 = tinggi_3017
    c_3017 = a_3017
    lebar_3017 = (2 * tinggi_3017) - 2

    for i_3017 in range(1, tinggi_3017 + 1):
        b_3017 = c_3017 + 1

        for j_3017 in range(1, lebar_3017 + 1):

            # Baris atas dan bawah
            if i_3017 == 1 or i_3017 == tinggi_3017:
                if j_3017 == 1 or j_3017 == lebar_3017:
                    print("#", end="")
                else:
                    print("=", end="")
            # Baris isi
            else:
                if j_3017 == 1 or j_3017 == lebar_3017:
                    print("|", end="")
                else:
                    if j_3017 == c_3017:
                        print("<", end="")
                    elif j_3017 == b_3017:
                        print(">", end="")
                    elif j_3017 == (lebar_3017 - c_3017):
                        print("<", end="")
                    elif j_3017 == (lebar_3017 - c_3017 + 1):
                        print(">", end="")
                    elif j_3017 > b_3017 and j_3017 < (lebar_3017 - c_3017):
                        print(".", end="")
                    else:
                        print(" ", end="")

        print()

        #Logika asli java
        a_3017 -= 2

        if a_3017 <= 0:
            c_3017 = (-a_3017) + 2
        else:
            c_3017 = a_3017