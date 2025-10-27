class Tanaman :
  def tumbuh(self):
    print("Tanaman Ini tumbuh dengan baik")
    
class Mawar(Tanaman):
  def tumbuh(self):
    print("Mawar ini tumbuh dengan baik")
    
class Kaktus(Tanaman):
  def tumbuh(self):
    print("Kaktus ini tumbuh dengan baik")
    
class Melati(Tanaman):
  def tumbuh(self):
    print("Melati ini tumbuh dengan baik")
    
taman = [Tanaman(), Mawar(), Kaktus(), Melati()]
for tanaman in taman :
  tanaman.tumbuh()
  
  