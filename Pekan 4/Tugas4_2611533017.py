print("=== SISTEM LOKET ALPRO ADVENTURE PARK ===")

# 1. Input Data Pengunjung & String Handling
nama_3017 = input("Masukkan Nama Pengunjung        : ")
umur_3017 = int(input("Input umur anda                 : "))
sim_3017 = input("Apakah Anda Sudah Punya SIM C (y/t): ").strip().lower()

if len(sim_3017) > 0:
    sim_3017 = sim_3017[0]

print("\nPilihan Paket Wahana (1-5):")
print("  1. Safari Rimba         (Rp 50,000)")
print("  2. Arung Jeram          (Rp 75,000)")
print("  3. Motor ATV Ekstrim    (Rp 120,000)")
print("  4. Roller Coaster Kilat (Rp 100,000)")
print("  5. All-Access VIP       (Rp 220,000)")

paket_3017 = int(input("Masukkan nomor paket (1-5)      : "))
jumlah_tiket_3017 = int(input("Masukkan jumlah tiket           : "))

# Validasi if-tunggal untuk jumlah tiket
if jumlah_tiket_3017 <= 0:
    print("Peringatan: Jumlah tiket tidak valid!")
    exit()

is_member_3017 = input("Apakah Anda member? (y/t)       : ").strip().lower()
kode_promo_3017 = input("Apakah kode promo valid? (y/t)  : ").strip().lower()

# 2. Pemilihan Wahana Menggunakan match-case
nama_wahana_3017 = ""
harga_satuan_3017 = 0

match paket_3017:
    case 1:
        nama_wahana_3017 = "Wahana Safari Rimba"
        harga_satuan_3017 = 50000
    case 2:
        nama_wahana_3017 = "Wahana Arung Jeram"
        harga_satuan_3017 = 75000
    case 3:
        nama_wahana_3017 = "Wahana Motor ATV Ekstrim"
        harga_satuan_3017 = 120000
    case 4:
        nama_wahana_3017 = "Wahana Roller Coaster Kilat"
        harga_satuan_3017 = 100000
    case 5:
        nama_wahana_3017 = "Wahana All-Access VIP"
        harga_satuan_3017 = 220000
    case _:
        print("Paket wahana tidak valid!")
        exit()

# 3. Validasi Izin Kendali Wahana Menggunakan if-elif-else dan Operator Logika
print("\n--- KELAYAKAN PENGENDARA WAHANA ---")
status_akses_3017 = ""

if paket_3017 == 3 and umur_3017 >= 17 and sim_3017 == 'y':
    status_akses_3017 = "Anda sudah dewasa dan boleh mengendarai ATV sendiri."
elif paket_3017 == 3 and umur_3017 >= 17 and sim_3017 != 'y':
    status_akses_3017 = "Anda sudah dewasa tetapi tidak boleh bawa motor ATV (wajib didampingi instruktur)."
elif paket_3017 == 3 and umur_3017 < 17 and sim_3017 == 'y':
    status_akses_3017 = "Identitas tidak valid: Belum cukup umur memiliki SIM."
elif paket_3017 == 3 and umur_3017 < 17 and sim_3017 != 'y':
    status_akses_3017 = "Anda belum cukup umur dan tidak boleh bawa motor ATV."
elif paket_3017 != 3 and umur_3017 >= 10:
    status_akses_3017 = "Anda memenuhi syarat umur untuk menikmati wahana ini."
else:
    status_akses_3017 = "Mohon maaf, umur Anda belum memenuhi batas minimal untuk wahana ini."

print(f"Status Akses: {status_akses_3017}")

# 4. Akumulasi Diskon Bertingkat Menggunakan Multi-IF Terpisah
subtotal_3017 = harga_satuan_3017 * jumlah_tiket_3017
total_diskon_persen_3017 = 0

if subtotal_3017 >= 200000:
    total_diskon_persen_3017 += 10

if is_member_3017 in ['y', 'ya']:
    total_diskon_persen_3017 += 5

if kode_promo_3017 in ['y', 'ya']:
    total_diskon_persen_3017 += 15

if jumlah_tiket_3017 >= 5:
    total_diskon_persen_3017 += 5

# 5. Hitung Total dan Evaluasi Audit (if-else)
nominal_diskon_3017 = subtotal_3017 * (total_diskon_persen_3017 / 100)
total_bayar_3017 = subtotal_3017 - nominal_diskon_3017

catatan_layanan_3017 = ""
if total_bayar_3017 > 300000:
    catatan_layanan_3017 = "Selamat! Anda berhak mendapatkan Souvenir Gratis."
else:
    catatan_layanan_3017 = "Terima kasih telah berkunjung."

# Output Rincian Pembayaran
print("\n--- Rincian Pembayaran ---")
print(f"Subtotal Belanja : Rp {subtotal_3017:,.0f}")
print(f"Total Diskon     : {total_diskon_persen_3017}% (Rp {nominal_diskon_3017:,.0f})")
print(f"Total Bayar      : Rp {total_bayar_3017:,.0f}")
print(f"Catatan Layanan  : {catatan_layanan_3017}")
print("Program Selesai")