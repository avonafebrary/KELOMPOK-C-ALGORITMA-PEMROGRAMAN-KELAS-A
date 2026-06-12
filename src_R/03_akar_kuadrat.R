#Soal program 3
#Input
a <- as.numeric(readline("Masukkan nilai a: "))  #Membaca input dari pengguna (readline) lalu mengkonversi ke tipe numerik dengan as.numeric()
b <- as.numeric(readline("Masukkan nilai b: "))  #Membaca input dari pengguna (readline) lalu mengkonversi ke tipe numerik dengan as.numeric()
c <- as.numeric(readline("Masukkan nilai c: "))  #Membaca input dari pengguna (readline) lalu mengkonversi ke tipe numerik dengan as.numeric()
#Proses
D <- b^2 - 4*a*c           #Menghitung determinan
#Output
if (D >= 0) {             #Percabangan: blok { } dijalankan jika D ≥ 0
  x1 <- (-b + sqrt(D)) / (2*a)  #Menghitung x1; fungsi sqrt() sudah tersedia langsung di R tanpa import tambahan
  x2 <- (-b - sqrt(D)) / (2*a)  #Menghitung x2; fungsi sqrt() sudah tersedia langsung di R tanpa import tambahan
  cat("Akar-akar real:\n")      #Menampilkan "Akar-akar real :"
  cat(sprintf("  x1 = %.3f\n", x1))  #Menampilkan output; sprintf("%.3f", x1) memformat angka menjadi 3 desimal; \n adalah newline
  cat(sprintf("  x2 = %.3f\n", x2))  #Menampilkan output; sprintf("%.3f", x1) memformat angka menjadi 3 desimal; \n adalah newline
} else {    #Jika kondisi if tidak terpenuhi (D < 0)
  cat("Persamaan ini hanya memiliki akar-akar imajiner.\n")  #Menampilkan pesan bahwa akar bersifat imajiner
}
