import math

# Fungsi menentukan nilai z berdasarkan alpha
def nilai_z(alpha):
    if alpha == 0.10:
        return 1.645
    elif alpha == 0.05:
        return 1.96
    else:
        return None

# Fungsi menghitung interval kepercayaan
def interval_kepercayaan(p_hat, n, alpha):
    z = nilai_z(alpha)

    margin_error = z * math.sqrt((p_hat * (1 - p_hat)) / n)

    batas_bawah = p_hat - margin_error
    batas_atas = p_hat + margin_error

    return batas_bawah, batas_atas

# Program utama
def main():
    print("=== Interval Kepercayaan Proporsi ===")

    p_hat = float(input("Masukkan proporsi sampel (p̂): "))
    n = int(input("Masukkan ukuran sampel (n): "))
    alpha = float(input("Masukkan alpha (0.10 atau 0.05): "))

    # Validasi proporsi
    if p_hat < 0 or p_hat > 1:
        print("Error: Proporsi harus berada antara 0 dan 1.")
        return

    # Validasi alpha
    if nilai_z(alpha) is None:
        print("Error: Alpha harus 0.10 atau 0.05.")
        return

    bawah, atas = interval_kepercayaan(p_hat, n, alpha)

    print(f"\nInterval Kepercayaan = ({bawah:}, {atas:})")

# Menjalankan program
main()
