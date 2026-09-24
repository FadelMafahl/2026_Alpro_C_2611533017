total_belanja_3017 = float(input("Masukkan total belanja (Rp): "))

input_member_3017 = input("Apakah anda member? (y/t): ").strip().lower()
is_member_3017 = input_member_3017 in ["y", "yes"]

input_promo_3017 = input("Apakah kode promo valid? (y/t): ").strip().lower()
kode_promo_valid_3017 = input_promo_3017 in ["y", "yes"]

total_diskon_3017 = 0

if total_belanja_3017 > 1000000:
    total_diskon_3017 += 10 # Diskon belanja besar

if is_member_3017:
    total_diskon_3017 += 5 # Diskon member

if kode_promo_valid_3017:
    total_diskon_3017 += 15 # Diskon voucher

nominal_diskon_3017 = total_belanja_3017 * (total_diskon_3017 / 100)
total_bayar_3017 = total_belanja_3017 - nominal_diskon_3017

print("\n--- Rincian pembayaran ---")
print(f"Total diskon: {total_diskon_3017}% (Rp {nominal_diskon_3017:,.0f})")
print(f"Total bayar : Rp {total_bayar_3017:,.0f}")

print(f"Total diskon yang anda dapatkan: {total_diskon_3017}%")
# output total diskon yang anda dapatkan: 30% jika belanja > 1 juta, member, dan kode promo valid