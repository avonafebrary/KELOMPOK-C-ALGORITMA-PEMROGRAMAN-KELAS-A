nip <- readline("Masukkan NIP ASN: ")

if (nchar(nip) != 18) {
  cat("NIP harus terdiri dari 18 digit\n")
} else {
  
  tahun <- substr(nip, 1, 4)
  bulan <- substr(nip, 5, 6)
  tanggal <- substr(nip, 7, 8)
  
  bulan_num <- as.numeric(bulan)
  tanggal_num <- as.numeric(tanggal)
  
  if (bulan == "01") {
    nama_bulan <- "Januari"
  } else if (bulan == "02") {
    nama_bulan <- "Februari"
  } else if (bulan == "03") {
    nama_bulan <- "Maret"
  } else if (bulan == "04") {
    nama_bulan <- "April"
  } else if (bulan == "05") {
    nama_bulan <- "Mei"
  } else if (bulan == "06") {
    nama_bulan <- "Juni"
  } else if (bulan == "07") {
    nama_bulan <- "Juli"
  } else if (bulan == "08") {
    nama_bulan <- "Agustus"
  } else if (bulan == "09") {
    nama_bulan <- "September"
  } else if (bulan == "10") {
    nama_bulan <- "Oktober"
  } else if (bulan == "11") {
    nama_bulan <- "November"
  } else if (bulan == "12") {
    nama_bulan <- "Desember"
  } else {
    nama_bulan <- "Tidak Valid"
  }
  
  if (nama_bulan == "Tidak Valid") {
    cat("Bulan pada NIP tidak valid\n")
  } else if (tanggal_num < 1 || tanggal_num > 31) {
    cat("Tanggal pada NIP tidak valid\n")
  } else {
    cat("Tanggal lahir ASN:",
        tanggal, nama_bulan, tahun)
  }
}

nip <- readline("Masukkan NIP ASN: ")

if (nchar(nip) != 18) {
  cat("NIP harus terdiri dari 18 digit\n")
} else {
  
  tahun <- substr(nip, 1, 4)
  bulan <- substr(nip, 5, 6)
  tanggal <- substr(nip, 7, 8)
  
  bulan_num <- as.numeric(bulan)
  tanggal_num <- as.numeric(tanggal)
  
  if (bulan == "01") {
    nama_bulan <- "Januari"
  } else if (bulan == "02") {
    nama_bulan <- "Februari"
  } else if (bulan == "03") {
    nama_bulan <- "Maret"
  } else if (bulan == "04") {
    nama_bulan <- "April"
  } else if (bulan == "05") {
    nama_bulan <- "Mei"
  } else if (bulan == "06") {
    nama_bulan <- "Juni"
  } else if (bulan == "07") {
    nama_bulan <- "Juli"
  } else if (bulan == "08") {
    nama_bulan <- "Agustus"
  } else if (bulan == "09") {
    nama_bulan <- "September"
  } else if (bulan == "10") {
    nama_bulan <- "Oktober"
  } else if (bulan == "11") {
    nama_bulan <- "November"
  } else if (bulan == "12") {
    nama_bulan <- "Desember"
  } else {
    nama_bulan <- "Tidak Valid"
  }
  
  if (nama_bulan == "Tidak Valid") {
    cat("Bulan pada NIP tidak valid\n")
  } else if (tanggal_num < 1 || tanggal_num > 31) {
    cat("Tanggal pada NIP tidak valid\n")
  } else {
    cat("Tanggal lahir ASN:",
        tanggal, nama_bulan, tahun)
  }
}