# 1. INPUT DATA PELANGGAN DAN TRANSAKSI

print("=== SISTEM TRANSAKSI TOKO ===")
nama_3017 = input("Masukkan Nama Pelanggan : ")
status_3017 = input("Masukkan Status Pelanggan (member/nonmember) : ").strip().lower()
total_belanja_3017 = float(input("Masukkan Total Belanja : "))
jumlah_barang_3017 = int(input("Masukkan Jumlah Barang : "))
kode_promo_3017 = input("Masukkan Kode Promo : ").strip().upper()

# Daftar promo resmi
daftar_promo_3017 = ["HEMAT77", "HEMAT17", "IF HEBAT", "IF KUAT"]

# 2. OPERATOR KEANGGOTAAN (MEMBERSHIP)

# Memeriksa keberadaan kode promo dalam daftar promo
promo_tersedia_3017 = kode_promo_3017 in daftar_promo_3017
promo_tidak_tersedia_3017 = kode_promo_3017 not in daftar_promo_3017

# 3. OPERATOR PERBANDINGAN & LOGIKA

# Operator Perbandingan
min_belanja_3017 = total_belanja_3017 >= 200000
min_barang_3017 = jumlah_barang_3017 >= 3
is_member_3017 = status_3017 == "member"

# Operator Logika (and, or, not)
dapat_diskon_3017 = is_member_3017 and min_belanja_3017
dapat_promo_3017 = promo_tersedia_3017 or (min_barang_3017 and not (status_3017 == "nonmember"))

# 4. OPERATOR ARITMATIKA & PENUGASAN (AUGMENTED ASSIGNMENT)

# Menghitung besarnya diskon (10% jika dapat diskon)
diskon_3017 = total_belanja_3017 * 0.10 if dapat_diskon_3017 else 0.0

# Perhitungan Total Pembayaran
total_pembayaran_3017 = total_belanja_3017
total_pembayaran_3017 -= diskon_3017  

# Perhitungan Rata-rata Harga Barang
rata_harga_3017 = total_belanja_3017 / jumlah_barang_3017

# Sisa pembagian (Operator Aritmatika %)
sisa_barang_3017 = jumlah_barang_3017 % 3

# 5. OPERATOR IDENTITAS (IDENTITY)

objek_a_3017 = "member"
objek_b_3017 = input_status_temp = "mem" + "ber"


is_sama_nilai_3017 = (objek_a_3017 == objek_b_3017)
is_sama_identitas_3017 = (objek_a_3017 is objek_b_3017)
is_beda_identitas_3017 = (objek_a_3017 is not status_3017)

# 6. OPERATOR BITWISE

BIT_MEMBER_3017 = 0b0001
BIT_BELANJA_3017 = 0b0010
BIT_BARANG_3017 = 0b0100
BIT_PROMO_3017 = 0b1000

# Penggabungan kondisi menggunakan Bitwise OR (|)
kode_status_3017 = 0b0000
if is_member_3017:
    kode_status_3017 |= BIT_MEMBER_3017
if min_belanja_3017:
    kode_status_3017 |= BIT_BELANJA_3017
if min_barang_3017:
    kode_status_3017 |= BIT_BARANG_3017
if promo_tersedia_3017:
    kode_status_3017 |= BIT_PROMO_3017

# Pemeriksaan kondisi menggunakan Bitwise AND (&)
cek_member_3017 = kode_status_3017 & BIT_MEMBER_3017
cek_promo_3017 = kode_status_3017 & BIT_PROMO_3017

# Perbandingan status menggunakan Bitwise XOR (^)
kode_referensi_3017 = 0b1011  
beda_status_3017 = kode_status_3017 ^ kode_referensi_3017

# Bitwise geser kiri (<<)
shift_status_3017 = kode_status_3017 << 1

# 7. MENAMPILKAN OUTPUT SESUAI FORMAT KETENTUAN 
print("\n=== DATA TRANSAKSI ===")
print(f"Nama Pelanggan        : {nama_3017}")
print(f"Status Pelanggan      : {status_3017}")
print(f"Total Belanja         : Rp{int(total_belanja_3017)}")
print(f"Jumlah Barang         : {jumlah_barang_3017}")
print(f"Kode Promo            : {kode_promo_3017}")

print("\n=== HASIL VALIDASI ===")
print(f"Belanja >= Rp200000   : {min_belanja_3017}")
print(f"Jumlah Barang >= 3    : {min_barang_3017}")
print(f"Status Member         : {is_member_3017}")
print(f"Kode Promo Tersedia   : {promo_tersedia_3017}")
print(f"Mendapatkan Diskon    : {dapat_diskon_3017}")
print(f"Mendapatkan Promo     : {dapat_promo_3017}")

print("\n=== HASIL PERHITUNGAN ===")
print(f"Diskon                : Rp{int(diskon_3017)}")
print(f"Total Pembayaran      : Rp{int(total_pembayaran_3017)}")
print(f"Rata-rata Harga Barang: Rp{rata_harga_3017:.2f}")

print("\n=== HAK AKSES PELANGGAN ===")
print(f"Kode Hak Akses        : {bin(kode_status_3017)[2:].zfill(4)}")
print(f"Member Access         : {bool(cek_member_3017)}")
print(f"Promo Access          : {bool(cek_promo_3017)}")
print(f"Free Shipping Access  : {kode_promo_3017 == 'GRATISONGKIR'}")

print("\n=== OPERASI BITWISE ===")
print("=== Kode Status Transaksi ===")
print("0001 | 0010 | 0100 | 1000")
print(f"Kode Biner    : {bin(kode_status_3017)[2:].zfill(4)}")
print(f"Kode Desimal  : {kode_status_3017}")

print("\n=== Pemeriksaan Status ===")
print("Cek Member")
print(f"{bin(kode_status_3017)[2:].zfill(4)} & 0001")
print(f"Hasil Biner   : {bin(cek_member_3017)[2:].zfill(4)}")
print(f"Hasil Desimal : {cek_member_3017}")

print("\nCek Promo")
print(f"{bin(kode_status_3017)[2:].zfill(4)} & 1000")
print(f"Hasil Biner   : {bin(cek_promo_3017)[2:].zfill(4)}")
print(f"Hasil Desimal : {cek_promo_3017}")

print("\n=== Perbandingan Status ===")
print(f"Kode Transaksi : {bin(kode_status_3017)[2:].zfill(4)}")
print(f"Kode Referensi : {bin(kode_referensi_3017)[2:].zfill(4)}")
print(f"{bin(kode_status_3017)[2:].zfill(4)} ^ {bin(kode_referensi_3017)[2:].zfill(4)}")
print(f"Hasil Biner   : {bin(beda_status_3017)[2:].zfill(4)}")
print(f"Hasil Desimal : {beda_status_3017}")

print("\n=== Shift ===")
print(f"{bin(kode_status_3017)[2:].zfill(4)} << 1")
print(f"Hasil Biner   : {bin(shift_status_3017)[2:].zfill(5)}")
print(f"Hasil Desimal : {shift_status_3017}")

print("\n=== SELESAI ===")