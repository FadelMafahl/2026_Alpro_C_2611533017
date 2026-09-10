from typing import Final
PI: Final = 3.14
print("pi: %f" % (PI))
jari_3017 = float(input('Masukkan nilai Jari-Jari: '))
luas_3017 = PI * jari_3017 * jari_3017
print("Luas lingkaran dengan jari-jari %.2f adalah %.2f" % (jari_3017, luas_3017))