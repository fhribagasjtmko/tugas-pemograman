# Latihan A - Soal 3: Program menghitung diskon belanja
# INPUT   : total belanja, persen diskon
# PROSES  : potongan = total * persen / 100 ; bayar = total - potongan
# OUTPUT  : besar potongan dan total yang harus dibayar

print("=== Diskon Belanja ===")
total_belanja = float(input("Total belanja (Rp) : "))      # INPUT
persen_diskon = float(input("Diskon (%)         : "))      # INPUT

potongan = total_belanja * persen_diskon / 100             # PROSES
total_bayar = total_belanja - potongan                     # PROSES

print("Potongan harga     : Rp", potongan)                 # OUTPUT
print("Total bayar        : Rp", total_bayar)              # OUTPUT
