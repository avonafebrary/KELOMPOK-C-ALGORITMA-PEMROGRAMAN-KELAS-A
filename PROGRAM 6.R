# soal nomor 6 (valid)
p_hat <- as.numeric(
  readline("Masukkan proporsi sampel (p̂): ")
)

n <- as.numeric(
  readline("Masukkan ukuran sampel (n): ")
)

alpha <- as.numeric(
  readline("Masukkan alpha (0.05 atau 0.10): ")
)

if (p_hat < 0 || p_hat > 1) {
  
  cat("Error: proporsi harus antara 0 dan 1")
  
} else {
  
  if (alpha == 0.10) {
    
    z <- 1.645
    
  } else if (alpha == 0.05) {
    
    z <- 1.96
    
  } else {
    
    cat("Alpha tidak valid")
    quit()
    
  }
  
  se <- sqrt((p_hat * (1 - p_hat)) / n)
  
  batas_bawah <- p_hat - z * se
  batas_atas <- p_hat + z * se
  
  cat("\nInterval Kepercayaan:\n")
  cat(round(batas_bawah, 4),
      "< p <",
      round(batas_atas, 4))
}


# soal nomor 6 (tidak valid)
p_hat <- as.numeric(
  readline("Masukkan proporsi sampel (p̂): ")
)

n <- as.numeric(
  readline("Masukkan ukuran sampel (n): ")
)

alpha <- as.numeric(
  readline("Masukkan alpha (0.05 atau 0.10): ")
)

if (p_hat < 0 || p_hat > 1) {
  
  cat("Error: proporsi harus antara 0 dan 1")
  
} else {
  
  if (alpha == 0.10) {
    
    z <- 1.645
    
  } else if (alpha == 0.05) {
    
    z <- 1.96
    
  } else {
    
    cat("Alpha tidak valid")
    quit()
    
  }
  
  se <- sqrt((p_hat * (1 - p_hat)) / n)
  
  batas_bawah <- p_hat - z * se
  batas_atas <- p_hat + z * se
  
  cat("\nInterval Kepercayaan:\n")
  cat(round(batas_bawah, 4),
      "< p <",
      round(batas_atas, 4))
}
