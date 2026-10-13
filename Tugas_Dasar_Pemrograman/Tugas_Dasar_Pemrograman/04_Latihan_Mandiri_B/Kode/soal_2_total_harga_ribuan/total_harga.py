# Latihan B - Soal 2: Total harga dengan pemisah ribuan
# Format f"{angka:,}" memberi pemisah ribuan berupa koma (1,500,000).
# Di Indonesia pemisah ribuan memakai titik, jadi koma diganti titik.

print("=== Total Pembelian ===")
harga = int(input("Harga barang (Rp)  : "))
jumlah = int(input("Jumlah pembelian   : "))

total = harga * jumlah
total_format = f"{total:,}".replace(",", ".")

print("Total bayar        : Rp", total_format)
