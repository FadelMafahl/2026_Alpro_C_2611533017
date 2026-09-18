print("=== SISTEM REGISTRASI PRAKTIKAN ALPRO 2026 ===")
nama_3017 = input("Masukkan Nama Mahasiswa : ")
kelamin_3017 = input("Masukkan Jenis Kelamin (L/P): ")
umur_3017 = int(input("Masukkan Umur : "))
skor_3017 = float(input("Masukkan Skor Tes Awal : "))

alamat_3017 = """
Kecamatan Nanggalo,
Kota Padang,
Sumatera Barat,
Indonesia
"""
from typing import Final
kkm_3017: Final = 75.0
token_3017 = 100+3j
lulus_3017 = skor_3017 > kkm_3017

print("\n=== DATA PRAKTIKAN & HASIL PEMERIKSAAN ===")
print("Nama Mahasiswa : ",nama_3017," | ",type(nama_3017))
print("Jenis Kelamin : ",kelamin_3017," | ",type(kelamin_3017))
print("Alamat Domisili : ",alamat_3017," | ",type(alamat_3017))
print("Umur : ",umur_3017," tahun | ",type(umur_3017))
print("Skor Tes Awal : ",skor_3017," | ",type(skor_3017))
print("ID Token Sinyal: ",token_3017," | ",type(token_3017))

print("=== STATUS KELULUSAN PRAKTIKUM ===")
print("Batas Minimum Nilai: ",kkm_3017," | ",type(kkm_3017))
print("Apakah Dinyatakan Lulus?: ",lulus_3017," | ",type(lulus_3017))