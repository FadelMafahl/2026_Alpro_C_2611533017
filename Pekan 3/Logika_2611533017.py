a1_3017 = input("Input nilai boolean-1 (true/false): ").strip().lower() == "true"
a2_3017 = input("Input nilai boolean-2 (true/false): ").strip().lower() == "true"

print("\nA1 =", a1_3017)
print("A2 =", a2_3017)

# Konjungsi bernilai True jika keduanya True
hasil = a1_3017 and a2_3017
print("\nKonjungsi (AND)")
print("A1 and A2 =", hasil)

# Disjungsi bernilai True jika salah satunya True
hasil = a1_3017 or a2_3017
print("\nDisjungsi (OR)")
print("A1 or A2 =", hasil)

# Negasi A1: membalik nilat A1
hasil = not a1_3017
print("\nNegasi A1 (NOT)")
print("not A1", hasil)

# Negasi A2: membalik nilat A2
hasil = not a2_3017
print("\nNegasi A2 (NOT)")
print("not A2", hasil)

#XOR bernilai True jika kedua nilai berbeda
# Negasi A1: membalik nilat A1
hasil = a1_3017 != a2_3017
print("\nDisjungsi Eksklusif (XOR)")
print("A1 XOR A2", hasil)