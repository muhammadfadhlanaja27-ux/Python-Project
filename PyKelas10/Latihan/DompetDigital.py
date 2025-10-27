class DompetDigital:

    def __init__(self, nama, saldo_awal):
        self.nama = nama
        self.__saldo = saldo_awal

    def isi_saldo(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah
        else:
            print("Jumlah harus lebih dari 0")

    def tarik_saldo(self, jumlah):
        if 0 < jumlah <= self.__saldo:
            self.__saldo -= jumlah
        else:
            print("Saldo tidak mencukupi atau jumlah tidak valid")

    def tampilkan_saldo(self):
        print(f"Saldo {self.nama} saat ini: Rp {self.__saldo}")

nadila = DompetDigital("Nadila", 1000000)
nadila.isi_saldo(500000)
nadila.tarik_saldo(200000)
nadila.tampilkan_saldo()
