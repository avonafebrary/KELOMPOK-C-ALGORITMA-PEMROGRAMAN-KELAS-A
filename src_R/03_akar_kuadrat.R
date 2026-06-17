# Program Mencari Akar Persamaan Kuadrat
a <- as.numeric(readline("Masukkan nilai a : "))
b <- as.numeric(readline("Masukkan nilai b : "))
c <- as.numeric(readline("Masukkan nilai c : "))

D <- b^2 - 4*a*c

if (D > 0) {
  
  x1 <- (-b + sqrt(D)) / (2*a)
  x2 <- (-b - sqrt(D)) / (2*a)
  
  cat("Akar real berbeda\n")
  cat(sprintf("x1 = %.3f\n", x1))
  cat(sprintf("x2 = %.3f\n", x2))
  
} else if (D == 0) {
  
  x <- -b / (2*a)
  
  cat("Akar real kembar\n")
  cat(sprintf("x1 = x2 = %.3f\n", x))
  
} else {
  
  cat("Persamaan memiliki akar-akar imajiner\n")
  
}
