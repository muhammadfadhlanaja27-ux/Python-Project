class akunbank:
  def __init__(self, nama, saldo, pin):
    self.nama = nama        #public
    self._saldo = saldo     #protected
    self.__pin = pin        #privat
    
  def ceksaldo(self):
    print(f"Mempilkan saldo akun : {self._saldo}")
    
  def get_pin(self):
    return self.__pin
    
  def set_pin(self, pinbaru):
    self.__pin = pinbaru
    print("Pin berhasil di ubah!")
    
  def tarik_saldo(self,jumlah):
    if jumlah <= self._saldo :
      self._saldo -= jumlah
      print(f"berhasil menarik saldo : Rp.{jumlah}. \nSisa saldo anda : {self._saldo}")
    else :
      print("Maaf saldo anta tidak mencukupi")
      
akun = akunbank("Mut", 100000, 1234)
print(f"Nama Akun : {akun.nama}")
print(f"Pin : {akun.get_pin()}")
akun.set_pin(2705)
akun.tarik_saldo(50000)
akun.ceksaldo()