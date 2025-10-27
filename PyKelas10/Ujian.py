#super class
class KonversiMataUang:
    def __init__(self, jumlah):
        self.__jumlah = jumlah
        self.__hasil = 0

    #getter untuk jumlah
    def get_jumlah(self):
        return self.__jumlah
    
    #getter untuk hasil
    def get_hasil(self):
        return self.__hasil
      
    #getter untuk IDR
    def get_IDR(self):
        return self.IDR
      
    #getter untuk USD
    def get_USD(self):
        return self.USD

    #setter untuk jumlah
    def set_jumlah(self, jumlah):
        self.__jumlah = jumlah

    #setter untuk hasil
    def set_hasil(self, hasil):
        self.__hasil = hasil

    #setter untuk IDR
    def set_IDR(self, nilai):
        self.IDR = nilai

    #setter untuk USD
    def set_USD(self, nilai):
        self.USD = nilai

    def info(self):
        return "ini adalah method class induk konversi mata uang"

#subclass
class IDRkeUSD(KonversiMataUang):
    def konversi(self):
        self.set_IDR(self.get_jumlah())
        return self.get_IDR() / 15000

    def info(self):
        return "ini adalah konversi IDR to USD"

#subclass
class USDkeIDR(KonversiMataUang):
    def konversi(self):
        self.set_USD(self.get_jumlah())
        return self.get_USD() * 15000

    def info(self):
        return "ini adalah konversi USD ke IDR"

#class program
class Mainprogram:
    def jalankan(self):
      #pengulangan
      while(True):
        print("Program Konversi Uang")
        print("1. IDR ke USD")
        print("2. USD ke IDR")
        pilihan = input("Masukan angka pilihan anda : ")

        #pilihan untuk memilih USD/IDR
        if pilihan == '1':
            print("Ini Konversi IDR ke USD")
            jumlah = int(input("Masukan jumlah mata uang IDR : "))
            konvert = IDRkeUSD(jumlah)
            hasil = konvert.konversi()
            print(f"Hasil Konversi : {hasil} USD")
        elif pilihan == '2':
            print("Ini konversi USD ke IDR")
            jumlah = int(input("Masukan jumlah mata uang USD : "))
            konvert = USDkeIDR(jumlah)
            hasil = konvert.konversi()
            print(f"Hasil Konversi : {hasil} IDR")
        else:
            print("pilihan tidak ada")
            
        #pilihan untuk pengulangan
        pengulangan = input("apakah anda ingin mengulang kembali? (y/n) : ")
        if pengulangan.lower() == 'y':
            pass
        elif pengulangan.lower() == 'n':
            print("Terimakasih telah menggunakan program ini...")
            break

#pemanggilan class Mainprogram
if __name__ == "__main__":
    program = Mainprogram()
    program.jalankan()
