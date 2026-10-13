# Latihan B - Soal 1: Konversi menit menjadi jam dan sisa menit
# // = pembagian bulat (hasil tanpa koma)
# %  = sisa bagi (modulus)

print("=== Konversi Menit ke Jam ===")
total_menit = int(input("Masukkan jumlah menit : "))

jam = total_menit // 60
sisa_menit = total_menit % 60

print(total_menit, "menit =", jam, "jam", sisa_menit, "menit")
