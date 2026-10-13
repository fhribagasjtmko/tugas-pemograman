# Latihan B - Soal 3: Perbedaan 10 dan "10" dalam Python
# 10   -> integer (bilangan bulat, bisa dihitung)
# "10" -> string (teks, hanya berisi karakter '1' dan '0')

a = 10
b = "10"

print("type(a) :", type(a))
print("type(b) :", type(b))

print("a + 5      =", a + 5)          # penjumlahan angka
print('b + "5"    =', b + "5")        # penggabungan teks
print("a * 3      =", a * 3)          # perkalian angka
print("b * 3      =", b * 3)          # pengulangan teks

# Mencampur int dan str akan error:
try:
    print(a + b)
except TypeError as e:
    print("a + b -> TypeError:", e)
