#soal nomor 5
import math

# Fungsi untuk menghitung jarak Euclidean 3 dimensi
def hitung_jarak(titik1, titik2):
    return math.sqrt(
        (titik1[0] - titik2[0]) ** 2 +
        (titik1[1] - titik2[1]) ** 2 +
        (titik1[2] - titik2[2]) ** 2
    )

# Fungsi untuk menentukan cluster
def tentukan_cluster(titik_u):
    cluster_a = (2, 1, 3)
    cluster_b = (1, -4, 6)
    cluster_c = (-2, 3, -2)

    jarak_a = hitung_jarak(titik_u, cluster_a)
    jarak_b = hitung_jarak(titik_u, cluster_b)
    jarak_c = hitung_jarak(titik_u, cluster_c)

    print(f"Jarak ke Cluster A = {jarak_a:}")
    print(f"Jarak ke Cluster B = {jarak_b:}")
    print(f"Jarak ke Cluster C = {jarak_c:}")

    if jarak_a < jarak_b and jarak_a < jarak_c:
        return "A"
    elif jarak_b < jarak_a and jarak_b < jarak_c:
        return "B"
    else:
        return "C"

# Program utama
x1 = float(input("Masukkan x1: "))
x2 = float(input("Masukkan x2: "))
x3 = float(input("Masukkan x3: "))

titik_u = (x1, x2, x3)

hasil_cluster = tentukan_cluster(titik_u)

print("Titik U termasuk Cluster", hasil_cluster)
