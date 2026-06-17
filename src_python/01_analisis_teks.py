{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/avonafebrary/KELOMPOK-C-ALGORITMA-PEMROGRAMAN-KELAS-A/blob/PHYTON/src_python/01_analisis_teks.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Soal Program 1\n",
        "# Program Menghitung Jumlah Kata dan Jumlah Kalimat\n",
        "\n",
        "# Membaca teks yang dimasukkan pengguna\n",
        "teks = input(\"Masukkan teks: \")\n",
        "\n",
        "# Memisahkan teks menjadi kata-kata berdasarkan spasi\n",
        "kata = teks.split()\n",
        "\n",
        "# Menghitung jumlah kata\n",
        "jumlah_kata = len(kata)\n",
        "\n",
        "# Menghitung jumlah tanda titik sebagai jumlah kalimat\n",
        "jumlah_kalimat = teks.count(\".\")\n",
        "\n",
        "# Menampilkan hasil perhitungan\n",
        "print(\"\\nHasil Perhitungan\")\n",
        "print(\"Jumlah kata :\", jumlah_kata)\n",
        "print(\"Jumlah kalimat :\", jumlah_kalimat)"
      ],
      "metadata": {
        "id": "Pddb5_IZ_te1",
        "outputId": "249b5543-7d1a-4508-d118-44aa74cce22b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan teks: Kami suka belajar Algoritma pemrograman bersama ibu lutfiah.\n",
            "\n",
            "Hasil Perhitungan\n",
            "Jumlah kata : 8\n",
            "Jumlah kalimat : 1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Soal Program 1\n",
        "# Program Menghitung Jumlah Kata dan Jumlah Kalimat\n",
        "\n",
        "# Membaca teks yang dimasukkan pengguna\n",
        "teks = input(\"Masukkan teks: \")\n",
        "\n",
        "# Memisahkan teks menjadi kata-kata berdasarkan spasi\n",
        "kata = teks.split()\n",
        "\n",
        "# Menghitung jumlah kata\n",
        "jumlah_kata = len(kata)\n",
        "\n",
        "# Menghitung jumlah tanda titik sebagai jumlah kalimat\n",
        "jumlah_kalimat = teks.count(\".\")\n",
        "\n",
        "# Menampilkan hasil perhitungan\n",
        "print(\"\\nHasil Perhitungan\")\n",
        "print(\"Jumlah kata :\", jumlah_kata)\n",
        "print(\"Jumlah kalimat :\", jumlah_kalimat)"
      ],
      "metadata": {
        "id": "Tq-gWyJVA6fX",
        "outputId": "b8ab0efb-9437-4b52-97e2-d208ef46bb6d",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan teks: Kami belajar algoritma pemograman tentang struktut percabangan, struktur pengulangan, modularisasi, dll. Sekarang kami mendapat projek besar untuk tugas akhir semester yaitu membuat 6 pemrograman. Semoga pembelajaran algoritma pemrograman dapat bermanfaat bagi kedepannya aamiin\n",
            "\n",
            "Hasil Perhitungan\n",
            "Jumlah kata : 33\n",
            "Jumlah kalimat : 2\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Soal Program 1\n",
        "# Program Menghitung Jumlah Kata dan Jumlah Kalimat\n",
        "\n",
        "# Membaca teks yang dimasukkan pengguna\n",
        "teks = input(\"Masukkan teks: \")\n",
        "\n",
        "# Memisahkan teks menjadi kata-kata berdasarkan spasi\n",
        "kata = teks.split()\n",
        "\n",
        "# Menghitung jumlah kata\n",
        "jumlah_kata = len(kata)\n",
        "\n",
        "# Menghitung jumlah tanda titik sebagai jumlah kalimat\n",
        "jumlah_kalimat = teks.count(\".\")\n",
        "\n",
        "# Menampilkan hasil perhitungan\n",
        "print(\"\\nHasil Perhitungan\")\n",
        "print(\"Jumlah kata :\", jumlah_kata)\n",
        "print(\"Jumlah kalimat :\", jumlah_kalimat)"
      ],
      "metadata": {
        "id": "sq2S9TwCCLil",
        "outputId": "7a103f4e-016b-4ca3-a093-8a1f756575b2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan teks: \n",
            "\n",
            "Hasil Perhitungan\n",
            "Jumlah kata : 0\n",
            "Jumlah kalimat : 0\n"
          ]
        }
      ]
    }
  ],
  "metadata": {
    "colab": {
      "name": "Selamat Datang di Colab",
      "toc_visible": true,
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}