#Soal program nomor 3
#valid
#Input
a = float(input("Masukkan nilai a: ")) # Membaca input dari pengguna dan mengkonversi ke tipe float
b = float(input("Masukkan nilai b: ")) # Membaca input dari pengguna dan mengkonversi ke tipe float
c = float(input("Masukkan nilai c: ")) # Membaca input dari pengguna dan mengkonversi ke tipe float

#Proses
D = b**2 - 4*a*c          # Menghitung diskriminan; **2 artinya pangkat 2, * artinya perkalian

#Output
if D >= 0:                            # Percabangan: jika diskriminan ≥ 0, akar-akar bersifat real
    x1 = (-b + math.sqrt(D)) / (2*a)  #Menghitung akar pertama dengan rumus x1
    x2 = (-b - math.sqrt(D)) / (2*a)  #Menghitung akar pertama dengan rumus x1
    print(f"Akar-akar real:")         #Menampilkan "Akar-akar real" jika nilainya memenuhi
    print(f"  x1 = {x1:.3f}")         #Menampilkan x1 dengan format f-string; :.3f berarti 3 angka desimal
    print(f"  x2 = {x2:.3f}")         #Menampilkan x2 dengan format f-string; :.3f berarti 3 angka desimal
else:                                 #Jika D < 0, akar-akarnya imajiner
    print("Persamaan ini hanya memiliki akar-akar imajiner.") #Menampilkan pesan bahwa akar tidak real
