# Program konversi suhu Celcius-Reamur-Fahrenheit

# Header dan Input Identitas
print("Program Konversi Suhu")
print("Nama : Syifa Komariyah Septi Ningsih")
print("NIM : 1306625084")
print()

# Input Parameter Suhu
suhu_awal = float(input("Suhu awal = "))
suhu_akhir = float(input("Suhu akhir = "))
selang = float(input("Selang = "))

# Header Tabel 
print("TABEL KONVERSI")
print(f"{'No.':<4} | {'Celcius':<10} | {'Reamur':<10} | {'Fahrenheit':<10}")
print("_" * 45)

# Inisialisasi Variable Perulangan
c = suhu_awal
no = 1

# Perulangan While Untuk Perhitungan & Cetak Format Tabel
while c <= suhu_akhir:
    r = 0.8 * c
    f = (1.8 * c) + 32

    # Cetak Baris Tabel Dengan Format Rapi
    print(f"{no:<4} | {c:<10.1f} | {r:<10.1f} | {f:<10.1f}")

    c += selang
    no += 1

# Tambahan di akhir
print("Selesai")