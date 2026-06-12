{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP17vEn0hUynJjf/Ls4u1Mn",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/avonafebrary/KELOMPOK-C-ALGORITMA-PEMROGRAMAN-KELAS-A/blob/main/05_cluster_3d.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "wRNmLaYBf0-g",
        "outputId": "3f9ad5e1-e882-49d8-8a69-ecc229255d99"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan x1: 1\n",
            "Masukkan x2: 5\n",
            "Masukkan x3: 10\n",
            "Jarak ke Cluster A = 8.12\n",
            "Jarak ke Cluster B = 9.85\n",
            "Jarak ke Cluster C = 12.53\n",
            "Titik U termasuk Cluster A\n"
          ]
        }
      ],
      "source": [
        "#soal nomor 5\n",
        "import math\n",
        "\n",
        "# Fungsi untuk menghitung jarak Euclidean 3 dimensi\n",
        "def hitung_jarak(titik1, titik2):\n",
        "    return math.sqrt(\n",
        "        (titik1[0] - titik2[0]) ** 2 +\n",
        "        (titik1[1] - titik2[1]) ** 2 +\n",
        "        (titik1[2] - titik2[2]) ** 2\n",
        "    )\n",
        "\n",
        "# Fungsi untuk menentukan cluster\n",
        "def tentukan_cluster(titik_u):\n",
        "    cluster_a = (2, 1, 3)\n",
        "    cluster_b = (1, -4, 6)\n",
        "    cluster_c = (-2, 3, -2)\n",
        "\n",
        "    jarak_a = hitung_jarak(titik_u, cluster_a)\n",
        "    jarak_b = hitung_jarak(titik_u, cluster_b)\n",
        "    jarak_c = hitung_jarak(titik_u, cluster_c)\n",
        "\n",
        "    print(f\"Jarak ke Cluster A = {jarak_a:.2f}\")\n",
        "    print(f\"Jarak ke Cluster B = {jarak_b:.2f}\")\n",
        "    print(f\"Jarak ke Cluster C = {jarak_c:.2f}\")\n",
        "\n",
        "    if jarak_a <= jarak_b and jarak_a <= jarak_c:\n",
        "        return \"A\"\n",
        "    elif jarak_b <= jarak_a and jarak_b <= jarak_c:\n",
        "        return \"B\"\n",
        "    else:\n",
        "        return \"C\"\n",
        "\n",
        "# Program utama\n",
        "x1 = float(input(\"Masukkan x1: \"))\n",
        "x2 = float(input(\"Masukkan x2: \"))\n",
        "x3 = float(input(\"Masukkan x3: \"))\n",
        "\n",
        "titik_u = (x1, x2, x3)\n",
        "\n",
        "hasil_cluster = tentukan_cluster(titik_u)\n",
        "\n",
        "print(\"Titik U termasuk Cluster\", hasil_cluster)"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#soal nomor 5\n",
        "import math\n",
        "\n",
        "# Fungsi untuk menghitung jarak Euclidean 3 dimensi\n",
        "def hitung_jarak(titik1, titik2):\n",
        "    return math.sqrt(\n",
        "        (titik1[0] - titik2[0]) ** 2 +\n",
        "        (titik1[1] - titik2[1]) ** 2 +\n",
        "        (titik1[2] - titik2[2]) ** 2\n",
        "    )\n",
        "\n",
        "# Fungsi untuk menentukan cluster\n",
        "def tentukan_cluster(titik_u):\n",
        "    cluster_a = (2, 1, 3)\n",
        "    cluster_b = (1, -4, 6)\n",
        "    cluster_c = (-2, 3, -2)\n",
        "\n",
        "    jarak_a = hitung_jarak(titik_u, cluster_a)\n",
        "    jarak_b = hitung_jarak(titik_u, cluster_b)\n",
        "    jarak_c = hitung_jarak(titik_u, cluster_c)\n",
        "\n",
        "    print(f\"Jarak ke Cluster A = {jarak_a:.2f}\")\n",
        "    print(f\"Jarak ke Cluster B = {jarak_b:.2f}\")\n",
        "    print(f\"Jarak ke Cluster C = {jarak_c:.2f}\")\n",
        "\n",
        "    if jarak_a <= jarak_b and jarak_a <= jarak_c:\n",
        "        return \"A\"\n",
        "    elif jarak_b <= jarak_a and jarak_b <= jarak_c:\n",
        "        return \"B\"\n",
        "    else:\n",
        "        return \"C\"\n",
        "\n",
        "# Program utama\n",
        "x1 = float(input(\"Masukkan x1: \"))\n",
        "x2 = float(input(\"Masukkan x2: \"))\n",
        "x3 = float(input(\"Masukkan x3: \"))\n",
        "\n",
        "titik_u = (x1, x2, x3)\n",
        "\n",
        "hasil_cluster = tentukan_cluster(titik_u)\n",
        "\n",
        "print(\"Titik U termasuk Cluster\", hasil_cluster)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "Mi_5XAwvgFnm",
        "outputId": "e1d6e072-585d-4f7a-92c2-298ed9748436"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan x1: 5\n",
            "Masukkan x2: -6\n",
            "Masukkan x3: 6\n",
            "Jarak ke Cluster A = 8.19\n",
            "Jarak ke Cluster B = 4.47\n",
            "Jarak ke Cluster C = 13.93\n",
            "Titik U termasuk Cluster B\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#soal nomor 5\n",
        "import math\n",
        "\n",
        "# Fungsi untuk menghitung jarak Euclidean 3 dimensi\n",
        "def hitung_jarak(titik1, titik2):\n",
        "    return math.sqrt(\n",
        "        (titik1[0] - titik2[0]) ** 2 +\n",
        "        (titik1[1] - titik2[1]) ** 2 +\n",
        "        (titik1[2] - titik2[2]) ** 2\n",
        "    )\n",
        "\n",
        "# Fungsi untuk menentukan cluster\n",
        "def tentukan_cluster(titik_u):\n",
        "    cluster_a = (2, 1, 3)\n",
        "    cluster_b = (1, -4, 6)\n",
        "    cluster_c = (-2, 3, -2)\n",
        "\n",
        "    jarak_a = hitung_jarak(titik_u, cluster_a)\n",
        "    jarak_b = hitung_jarak(titik_u, cluster_b)\n",
        "    jarak_c = hitung_jarak(titik_u, cluster_c)\n",
        "\n",
        "    print(f\"Jarak ke Cluster A = {jarak_a:.2f}\")\n",
        "    print(f\"Jarak ke Cluster B = {jarak_b:.2f}\")\n",
        "    print(f\"Jarak ke Cluster C = {jarak_c:.2f}\")\n",
        "\n",
        "    if jarak_a <= jarak_b and jarak_a <= jarak_c:\n",
        "        return \"A\"\n",
        "    elif jarak_b <= jarak_a and jarak_b <= jarak_c:\n",
        "        return \"B\"\n",
        "    else:\n",
        "        return \"C\"\n",
        "\n",
        "# Program utama\n",
        "x1 = float(input(\"Masukkan x1: \"))\n",
        "x2 = float(input(\"Masukkan x2: \"))\n",
        "x3 = float(input(\"Masukkan x3: \"))\n",
        "\n",
        "titik_u = (x1, x2, x3)\n",
        "\n",
        "hasil_cluster = tentukan_cluster(titik_u)\n",
        "\n",
        "print(\"Titik U termasuk Cluster\", hasil_cluster)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 0
        },
        "id": "MqigB_NggJj_",
        "outputId": "461ee927-378d-44f9-e2ab-b0e6b5cd1376"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan x1: -5\n",
            "Masukkan x2: 7\n",
            "Masukkan x3: -9\n",
            "Jarak ke Cluster A = 15.13\n",
            "Jarak ke Cluster B = 19.54\n",
            "Jarak ke Cluster C = 8.60\n",
            "Titik U termasuk Cluster C\n"
          ]
        }
      ]
    }
  ]
}