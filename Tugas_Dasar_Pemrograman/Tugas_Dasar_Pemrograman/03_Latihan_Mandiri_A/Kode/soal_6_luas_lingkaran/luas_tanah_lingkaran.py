# Latihan A - Soal 6: Menghitung luas tanah berbentuk lingkaran
# Rumus: L = pi x r x r  (pi = 3.14159...)

import math   # modul matematika, berisi nilai pi

print("=== Luas Tanah Berbentuk Lingkaran ===")
jari_jari = float(input("Masukkan jari-jari (meter) : "))
luas = math.pi * jari_jari ** 2
print("Luas tanah :", round(luas, 2), "meter persegi")
