# Latihan B - Soal 5: Tiga contoh nama variabel yang salah + aturan yang dilanggar
# Kode salah dijalankan lewat exec() agar pesan error tampil.

contoh = [
    ("2nilai = 10",          "Diawali angka (harus diawali huruf)"),
    ("nama mahasiswa = 'Budi'", "Mengandung spasi (gunakan underscore: nama_mahasiswa)"),
    ("harga-barang = 5000",  "Mengandung simbol '-' (gunakan underscore: harga_barang)"),
]

for kode, alasan in contoh:
    print("Kode   :", kode)
    print("Alasan :", alasan)
    try:
        exec(kode)
    except SyntaxError as e:
        print("Error  : SyntaxError:", e.msg)
    print()
