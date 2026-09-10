is_lulus = True
is_cumlaude = True

nilai_3017 = 85
batas_lulus = 75

status_kelulusan = nilai_3017 >= batas_lulus #Hasilnya akan True

print("=== Check Kelulusan ===")
print("nilai:", nilai_3017)
print("Apakah lulus?:", status_kelulusan)
if is_lulus and is_cumlaude:
    print("Selamat, Anda lulus dengan predikat cumlaude")