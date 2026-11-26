schedule = {
    "Monday": ["Algorithms", "Calculus"],
    "Tuesday": ["English"],
    "Wednesday": ["Algorithms", "Physics", "Discrete Math"],
    "Thursday": ["Physics", "Calculus"],
    "Friday": ["Discrete Math"],
}

matkul = {}
matkul_perhari = {}
busy = 0
busy_day = "Monday"
for hari,kelas in schedule.items():
    matkul_perhari[hari] = len(kelas)
    if len(kelas) > busy:
        busy_day = hari
        busy = len(kelas)
    for data in kelas:
        if data not in matkul:
            matkul[data] = 0
        matkul[data] += 1
print(f"Busiest day : {busy_day} ({matkul_perhari[busy_day]} course).")
matkul_input = input("Masukkan nama matkul: ")
if matkul_input not in matkul:
    matkul[matkul_input] = 0
print(f"{matkul_input}: {matkul[matkul_input]} days.")