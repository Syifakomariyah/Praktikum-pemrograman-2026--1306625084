#Identitas
print("Program Faktor Bilangan")
print("Nama : Syifa Komariyah")
print("NIM  : 1306625084")
print()

#Program 
while True:
    hasil =[]
    n = int(input("Masukan sembarang bilangan < 100 ( selesai=0) = "))
    if n == 0:
        break
    for i in range (1, n+1):
        if n % i == 0:
            hasil.append(i)
    print('bilangan', 1, 'faktornya=', hasil)
print('selesai')
