presensi = input("Masukkan Nomor:").split()
submit = input("Masukkan Submit Tugas: ").split()

presensi1 = set(presensi)
submit1 = set(submit)
jumlah_submit = len(submit1)

tugas_yang_belum = presensi1 - submit1

jumlah_not_submit = len(tugas_yang_belum)

print(f"Submitted: {jumlah_submit} students")
print(f"Not submitted: {jumlah_not_submit} students")

for nomor in presensi:
  if nomor not in submit1:
    print(nomor)