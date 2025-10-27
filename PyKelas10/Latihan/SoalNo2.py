class Kalkulator:
  def __init__(self):
    self.__bilangan1 = 0
    self.__bilangan2 = 0
    
  def setbilangan(self, b1, b2):
    self.__bilangan1 = b1
    self.__bilangan2 = b2
    
  def getbilangan1(self):
    return self.__bilangan1
    
  def getbilangan2(self):
    return self.__bilangan2
    
  def konversi(self):
    print("ini method dasar")
    
class kalkulatorpenjumlahan(Kalkulator):
  def konversi(self):
    hasil = self.getbilangan1() + self.getbilangan2()
    print(f"Hasil penjumlahan adalah {hasil}")
    
class kalkulatorpengurangan(Kalkulator):
  def konversi(self):
    hasil = self.getbilangan1() - self.getbilangan2()
    print(f"Hasil pengurangan adalah {hasil}")
    
class main:
  def mulai(self):
    print("== Kalkulator ==")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    pilihan = input("Pilih operasi (1/2): ")
    
    b1 = int(input("Masukan Angka Ke 1 :"))
    b2 = int(input("Masukan Angka ke 2 :"))
    
    if pilihan == '1':
      kalkulator = kalkulatorpenjumlahan()
    elif pilihan == '2':
      kalkulator = kalkulatorpengurangan()
    else:
      print("Pilihan tidak valid.")
      return
    
    kalkulator.setbilangan(b1, b2)
    kalkulator.konversi()
    
main1 = main()

main1.mulai()
