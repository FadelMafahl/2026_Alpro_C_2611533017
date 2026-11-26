n = int(input("Jumlah Setoran: "))

kas = {}

total = 0

for buku in range (n):
    bayar = input("Masukkan nama dan nominal: ").strip()
    
    nama, nominal_str = bayar.split() 
    nominal = int(nominal_str)

    if nama not in kas :
    
        kas[nama] = 0
    
    
    kas[nama] += nominal
    total += nominal
    
winner = ""
most = 0
for name, uang in kas.items():
    if uang > most:
        winner = name
        most = uang

for nama_kas,uang_kas in kas.items():
    print (f"{nama_kas}: {uang_kas}")

print(f"Total cash: {total}")
print(f"Top contributor: {winner} ({most})")
