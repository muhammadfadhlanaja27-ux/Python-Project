class Mahasiswa:
  def __init__(self, nama, nim, nilai):
    self.nama = nama
    self._nim = nim
    self.__nilai = nilai
    
  def get_nilai(self):
    return self.__nilai
  
  def set_nilai(self, nilai):
    if 0 <= nilai <= 100:
      self.__nilai = nilai
    else :
      print("Nilai harus antara 0 - 100")
      
mhs = Mahasiswa("Lan", "2027512", 96)
print(f"Nama : {mhs.nama}")
print(f"Nim : {mhs._nim}")
print(f"Nilai : {mhs.get_nilai()}") 