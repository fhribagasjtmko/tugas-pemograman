# Tugas 3 - Simulasi alur Login Gmail (mengikuti flowchart di slide)
# Ini hanya simulasi sederhana, bukan login Gmail yang sebenarnya.

# "Server Gmail" tiruan: email -> sandi
server_gmail = {"budi@gmail.com": "rahasia123"}

print("=== gmail.com ===")
print("1. Berikutnya (Login)")
print("2. Buat akun")
pilihan = input("Pilih (1/2): ")

if pilihan == "2":
    print("Menuju halaman Buat akun...")
else:
    # Perulangan: ulangi sampai email ditemukan di server
    while True:
        email = input("Masukkan email: ")
        if email in server_gmail:          # cek ke server: email terdaftar?
            break
        print("Email tidak ditemukan")      # Tidak -> ulangi

    # Perulangan: ulangi sampai sandi benar
    while True:
        sandi = input("Masukkan sandi: ")
        if sandi == server_gmail[email]:   # cek ke server: sandi benar?
            break
        print("Sandi salah")                # Tidak -> ulangi

    print("Login berhasil! Menuju halaman Gmail...")
