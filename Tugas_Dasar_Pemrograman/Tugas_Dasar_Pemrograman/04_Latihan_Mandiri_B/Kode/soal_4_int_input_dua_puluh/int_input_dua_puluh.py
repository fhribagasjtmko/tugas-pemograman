# Latihan B - Soal 4: Apa yang terjadi jika pengguna mengetik "dua puluh"
# saat program memakai int(input(...))?
# Jawaban: terjadi ValueError karena "dua puluh" bukan angka (digit).

# Versi 1: tanpa penanganan error (program akan berhenti / crash)
# umur = int(input("Masukkan umur: "))

# Versi 2: dengan try-except agar program tidak crash
try:
    umur = int(input("Masukkan umur (angka): "))
    print("Umur Anda", umur, "tahun")
except ValueError:
    print("Input harus berupa angka, misalnya 20 (bukan 'dua puluh').")
