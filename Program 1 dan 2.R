# Program Menghitung Jumlah Kata dan Jumlah Kalimat

# Membaca teks dari pengguna
teks <- readline("Masukkan teks: ")

# Memisahkan teks menjadi kata-kata berdasarkan spasi
kata <- strsplit(teks, " ")[[1]]

# Menghitung jumlah kata
jumlah_kata <- length(kata)

# Menghitung jumlah tanda titik sebagai jumlah kalimat
jumlah_kalimat <- lengths(regmatches(teks, gregexpr("\\.", teks)))

# Menampilkan hasil
cat("\nHasil Perhitungan\n")
cat("Jumlah kata :", jumlah_kata, "\n")
cat("Jumlah kalimat :", jumlah_kalimat)

#Soal Nomor 2
# Program 2 - Membuat objek string K1 sampai K4

# String yang mengandung tanda petik tunggal
K1 = "Saya tak 'kan menyerah."

# String yang mengandung tanda petik ganda
K2 = 'Ia berkata, "Aku menyayangimu."'

# String yang mengandung petik tunggal dan ganda
K3 = "\"Coba jelaskan pengertian 'cross-validation' dalam Machine Learning!\""

# String biasa
K4 = "Surat keputusan itu bernomor 62/UN.34/19/2023."

# Menampilkan isi string
print(K1)
print(K2)
print(K3)
print(K4)
