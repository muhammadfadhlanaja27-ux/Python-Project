class PerangkatElektronik:
  def __init__(self,merk):
    self.merk = merk
    
  def nyala(self):
    print (f"perangkat elektronik {self.merk} ini menyala!")
    
  def nyala(self, mode=None):
    if mode is None:
      print("Perangkat elektronik menyala")
    else:
      print(f"Perangkat elektronik menyala dalam mode {mode}")
    
class laptop(PerangkatElektronik):
  def __init__(self, merk):
    super().__init__(merk)
    
  def nyala(self, mode=None):
    if mode is None:
      print("Laptop menyala")
    else:
      print(f"Laptop menyala dalam mode {mode}")
    
  def bukasoftware(self):
     print (f"Laptop {self.merk} membuka software")
    
class smartphone(PerangkatElektronik):
  def __init__(self, merk):
    super().__init__(merk)
    
  def nyala(self, mode=None):
        if mode is None:
            print("Smartphone menyala")
        else:
            print(f"Smartphone menyala dalam mode {mode}")
    
  def bukaaplikasi(self):
    print (f"Smartphone {self.merk} membuka aplikasi")
    
lp = laptop("Lenovo")
sp = smartphone("Xiaomi")

print("Uji Laptop:")
lp.nyala()
lp.nyala("gaming")

print("\nUji Smartphone:")
sp.nyala()
sp.nyala("hemat daya")