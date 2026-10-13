# Latihan A - Soal 5: Demo case-sensitive dan indentasi yang tidak konsisten
# Kode yang salah dijalankan lewat exec() agar error-nya bisa ditampilkan
# tanpa menghentikan program ini.

def coba(judul, kode):
    print("-" * 60)
    print(judul)
    print(kode)
    try:
        exec(kode)
    except Exception as e:
        print(">>", type(e).__name__ + ":", e)

# 1. Case-sensitive: nama dan Nama dianggap dua variabel yang berbeda
coba("1. Huruf besar/kecil berbeda", 'nama = "Budi"\nprint(Nama)')

# 2. Case-sensitive pada perintah: print bukan Print
coba("2. print tidak sama dengan Print", 'Print("Halo")')

# 3. Indentasi berlebih tanpa blok
coba("3. Indentasi tiba-tiba menjorok", 'x = 5\n    print(x)')

# 4. Indentasi tidak sejajar dalam satu blok
coba("4. Indentasi tidak konsisten dalam satu blok",
     'angka = 12\nif angka > 10:\n        print("besar")\n    print("selesai")')

# 5. Blok if tanpa isi yang menjorok
coba("5. Blok if tanpa indentasi", 'angka = 12\nif angka > 10:\nprint("besar")')
