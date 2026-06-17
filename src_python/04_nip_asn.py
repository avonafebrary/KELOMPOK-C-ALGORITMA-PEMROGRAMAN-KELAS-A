# Program 4

# Input NIP ASN
nip = input("Masukkan NIP ASN: ")

# Validasi panjang NIP
if len(nip) != 18:
    print("NIP harus terdiri dari 18 digit")

else:
    # Mengambil tahun, bulan, dan tanggal lahir
    tahun = nip[0:4]
    bulan = nip[4:6]
    tanggal = nip[6:8]

    bulan_num = int(bulan)
    tanggal_num = int(tanggal)

    # Menentukan nama bulan
    if bulan == "01":
        nama_bulan = "Januari"
    elif bulan == "02":
        nama_bulan = "Februari"
    elif bulan == "03":
        nama_bulan = "Maret"
    elif bulan == "04":
        nama_bulan = "April"
    elif bulan == "05":
        nama_bulan = "Mei"
    elif bulan == "06":
        nama_bulan = "Juni"
    elif bulan == "07":
        nama_bulan = "Juli"
    elif bulan == "08":
        nama_bulan = "Agustus"
    elif bulan == "09":
        nama_bulan = "September"
    elif bulan == "10":
        nama_bulan = "Oktober"
    elif bulan == "11":
        nama_bulan = "November"
    elif bulan == "12":
        nama_bulan = "Desember"
    else:
        nama_bulan = "Tidak Valid"

    # Validasi bulan dan tanggal
    if nama_bulan == "Tidak Valid":
        print("Bulan pada NIP tidak valid")

    elif tanggal_num < 1 or tanggal_num > 31:
        print("Tanggal pada NIP tidak valid")

    else:
        print("Tanggal lahir ASN:", tanggal, nama_bulan, tahun)
