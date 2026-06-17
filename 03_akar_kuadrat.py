{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPk8z4ckK7d99LVPGBnRaZp",
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
        "<a href=\"https://colab.research.google.com/github/avonafebrary/KELOMPOK-C-ALGORITMA-PEMROGRAMAN-KELAS-A/blob/PHYTON/03_akar_kuadrat.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "gwp1sv5DaE0y",
        "outputId": "8340d21e-8799-46d7-9c90-f96d75b1a6f0"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Masukkan nilai a : 1\n",
            "Masukkan nilai b : 4\n",
            "Masukkan nilai c : 4\n",
            "Akar real kembar\n",
            "x1 = x2 = -2.000\n"
          ]
        }
      ],
      "source": [
        "# Program Mencari Akar Persamaan Kuadrat\n",
        "a = float(input(\"Masukkan nilai a : \"))\n",
        "b = float(input(\"Masukkan nilai b : \"))\n",
        "c = float(input(\"Masukkan nilai c : \"))\n",
        "\n",
        "D = b**2 - 4*a*c\n",
        "\n",
        "if D > 0:\n",
        "    x1 = (-b + (D**0.5)) / (2*a)\n",
        "    x2 = (-b - (D**0.5)) / (2*a)\n",
        "    print(\"Akar real berbeda\")\n",
        "    print(\"x1 = %.3f\" % x1)\n",
        "    print(\"x2 = %.3f\" % x2)\n",
        "\n",
        "elif D == 0:\n",
        "    x = -b / (2*a)\n",
        "    print(\"Akar real kembar\")\n",
        "    print(\"x1 = x2 = %.3f\" % x)\n",
        "\n",
        "else:\n",
        "    print(\"Persamaan memiliki akar-akar imajiner\")"
      ]
    }
  ]
}