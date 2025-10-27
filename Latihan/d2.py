#KALKULATOR SEDERHANA
'''
def tambah(x, y):
    return x + y
def kurang(x, y):
    return x - y
def kali(x, y):
    return x * y
def bagi(x, y):
    return x / y
def modulus(x, y):
    return x % y
print("Pilih Operasi.")
print("1.Tambah")
print("2.Kurang")
print("3.Kali")
print("4.Bagi")
choice = input("Masukkan pilihan(1/2/3/4): ")
num1 = float(input("Masukkan angka pertama: "))
num2 = float(input("Masukkan angka kedua: "))

if choice =='1':
    print(num1,"+",num2,"=", tambah(num1,num2))
elif choice =='2':
    print(num1,"-",num2,"=", kurang(num1,num2))
elif choice =='3':
    print(num1,"*",num2,"=", kali(num1,num2))
elif choice =='4':
    print(num1,"/",num2,"=", bagi(num1,num2))
elif choice =='5':
    print(num1,"%",num2,"=", modulus(num1,num2))    
else:
    print("Input Salah")
'''

#Tebak Tebakan
import random
angka = random.randint(1, 1000)

tebakan = 0

while tebakan != angka:
    tebakan = int(input("Masukkan Tebakan Angka 1-1000: "))
    if tebakan < angka:
        print("Tebakan Terlalu Rendah")
    elif tebakan > angka:
        print("Tebakan Terlalu Tinggi")
    else:
        print("Selamat, Tebakan Anda Benar!")