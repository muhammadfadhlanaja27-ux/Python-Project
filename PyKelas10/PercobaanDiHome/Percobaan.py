min = int(input("Masukan Nilai Minimal : "))
max = int(input("Masukan Nilai Maksimal : "))

for i in range (min ,max , +1):
    if i % 2 == 0:
        print(i , end=',')