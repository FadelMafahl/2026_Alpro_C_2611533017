presensi = input("Masukkan Nomor:").split()
submit = input("Masukkan Submit Tugas: ").split()

set_presensi = set(presensi)
set_submit = set(submit)
jumlah_submit = len(set_submit)

tugas_yang_belum = set_presensi - set_submit

jumlah_not_submit = len(tugas_yang_belum)

print(f"Submitted: {jumlah_submit} students")
print(f"Not submitted: {jumlah_not_submit} students")

for nomor in presensi:
  if nomor not in set_submit:
    print(nomor)