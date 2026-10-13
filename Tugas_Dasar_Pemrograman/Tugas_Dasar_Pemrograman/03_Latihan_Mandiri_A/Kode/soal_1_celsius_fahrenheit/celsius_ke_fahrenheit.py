# Latihan A - Soal 1: Mengubah suhu Celsius menjadi Fahrenheit
# Rumus: F = (C x 9/5) + 32

print("=== Konversi Celsius ke Fahrenheit ===")
celsius = float(input("Masukkan suhu (Celsius) : "))
fahrenheit = (celsius * 9 / 5) + 32
# round(..., 2) membulatkan ke 2 angka di belakang koma
print("Suhu dalam Fahrenheit  :", round(fahrenheit, 2))
