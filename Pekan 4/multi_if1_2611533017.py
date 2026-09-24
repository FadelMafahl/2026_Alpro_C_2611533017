umur_3017 = int(input("Masukkan umur anda: "))
sim_3017 = input("Apakah anda sudah punya sim C (y/t): ")[0]

if umur_3017 >= 17 and sim_3017 == 'y':
    print("Anda sudah dewasa dan boleh bawa motor")

if umur_3017 >= 17 and sim_3017 != 'y':
    print("Anda sudah dewasa tetapi tidak boleh bawa motor")

if umur_3017 < 17 and sim_3017 == 'y':
    print("Anda belum cukup umur punya sim")

if umur_3017 < 17 and sim_3017 != 'y':
    print("Anda belum cukup umur bawa motor")