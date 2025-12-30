# ====== LATIHAN 1: Operasi String ======
print("=" * 50)
print("LATIHAN 1: Operasi String")
print("=" * 50)

txt = 'Hello World'

# 1. Hitung jumlah karakternya
print(f"1. Jumlah karakter: {len(txt)}")

# 2. Ambil karakter terakhir
print(f"2. Karakter terakhir: {txt[-1]}")

# 3. Ambil karakter index ke-2 sampai index ke-4 (llo)
print(f"3. Karakter index ke-2 sampai ke-4: {txt[2:5]}")

# 4. Hilangkan spasi pada text tersebut (HelloWorld)
print(f"4. Hilangkan spasi: {txt.replace(' ', '')}")

# 5. Ubah text menjadi huruf besar
print(f"5. Ubah ke huruf besar: {txt.upper()}")

# 6. Ubah text menjadi huruf kecil
print(f"6. Ubah ke huruf kecil: {txt.lower()}")

# 7. Ganti karakter H dengan karakter J
print(f"7. Ganti H dengan J: {txt.replace('H', 'J')}")

print("\n")