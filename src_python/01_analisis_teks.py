# Soal Program 1
# Program Menghitung Jumlah Kata dan Jumlah Kalimat

# Membaca teks yang dimasukkan pengguna
teks = input("Masukkan teks: ")

# Memisahkan teks menjadi kata-kata berdasarkan spasi
kata = teks.split()

# Menghitung jumlah kata
jumlah_kata = len(kata)

# Menghitung jumlah tanda titik sebagai jumlah kalimat
jumlah_kalimat = teks.count(".")

# Menampilkan hasil perhitungan
print("\nHasil Perhitungan")
print("Jumlah kata :", jumlah_kata)
print("Jumlah kalimat :", jumlah_kalimat)
