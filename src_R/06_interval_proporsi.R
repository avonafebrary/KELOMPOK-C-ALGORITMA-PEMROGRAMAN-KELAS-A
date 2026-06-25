# Program 6 : Interval Kepercayaan Proporsi

# Fungsi menentukan nilai z
nilai_z <- function(alpha) {
  if (alpha == 0.10) {
    return(1.645)
  } else if (alpha == 0.05) {
    return(1.96)
  } else {
    return(NA)
  }
}

# Fungsi menghitung interval kepercayaan
interval_kepercayaan <- function(p_hat, n, alpha) {
  z <- nilai_z(alpha)
  
  margin_error <- z * sqrt((p_hat * (1 - p_hat)) / n)
  
  batas_bawah <- p_hat - margin_error
  batas_atas <- p_hat + margin_error
  
  return(c(batas_bawah, batas_atas))
}

# Program utama
main <- function() {
  
  cat("=== Interval Kepercayaan Proporsi ===\n")
  
  p_hat <- as.numeric(readline("Masukkan proporsi sampel (p̂): "))
  n <- as.numeric(readline("Masukkan ukuran sampel (n): "))
  alpha <- as.numeric(readline("Masukkan alpha (0.10 atau 0.05): "))
  
  # Validasi proporsi
  if (p_hat < 0 || p_hat > 1) {
    cat("Error: Proporsi harus berada antara 0 dan 1.\n")
    return()
  }
  
  # Validasi alpha
  if (is.na(nilai_z(alpha))) {
    cat("Error: Alpha harus 0.10 atau 0.05.\n")
    return()
  }
  
  hasil <- interval_kepercayaan(p_hat, n, alpha)
  
  cat("\nInterval Kepercayaan = (",
      round(hasil[1], 4), ", ",
      round(hasil[2], 4), ")\n", sep = "")
}

# Menjalankan program
main()
