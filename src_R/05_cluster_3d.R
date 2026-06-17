#Program 5

#Fungsi menghitung jarak Euclidean
hitungJarak <- function(titik1, titik2) {
  jarak <- sqrt(sum((titik1 - titik2)^2))
  return(jarak)
}

#Pusat cluster
A <- c(2, 1, 3)
B <- c(1, -4, 6)
C <- c(-2, 3, -2)

#Input titik U
U <- as.numeric(strsplit(
  readline("Masukkan x1 x2 x3: "),
  " "
)[[1]])

# Validasi input
if (length(U) != 3 || any(is.na(U))) {

  cat("Input tidak valid! Masukkan tepat 3 angka.")

} else {

  #Memanggil fungsi
  jarakA <- hitungJarak(U, A)
  jarakB <- hitungJarak(U, B)
  jarakC <- hitungJarak(U, C)

  #Menentukan cluster
  if (jarakA <= jarakB && jarakA <= jarakC) {
    cluster <- "A"
  } else if (jarakB <= jarakA && jarakB <= jarakC) {
    cluster <- "B"
  } else {
    cluster <- "C"
  }

  cat("Titik U berada pada Cluster", cluster)
}
