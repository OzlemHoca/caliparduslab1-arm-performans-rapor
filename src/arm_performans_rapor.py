#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ARM Performans Raporlayıcı
ÇalıPardusLab1 / Pardus Hata Yakalama ve Öneri Yarışması 2026
"""

import os
import time


def baslik():
    print("=" * 60)
    print("PARDUS ARM PERFORMANS RAPORLAYICI")
    print("=" * 60)


def cpu_yuku():
    load = os.getloadavg()
    print("\nCPU Load Average")
    print(f"1 dakika  : {load[0]}")
    print(f"5 dakika  : {load[1]}")
    print(f"15 dakika : {load[2]}")


def bellek():
    print("\nBellek Bilgisi")

    with open("/proc/meminfo") as f:
        for i in range(3):
            print(f.readline().strip())


def sistem_ozeti():
    cpu_yuku()
    bellek()


def menu():
    print("\nSeçim yapın:")
    print("1 - Sistem performans özeti")
    print("2 - CPU yükü")
    print("3 - Bellek durumu")
    print("4 - Çıkış")


def main():

    baslik()

    while True:

        menu()

        secim = input("Seçim: ")

        if secim == "1":
            sistem_ozeti()

        elif secim == "2":
            cpu_yuku()

        elif secim == "3":
            bellek()

        elif secim == "4":
            print("Program kapatıldı")
            break

        else:
            print("Geçersiz seçim")


if __name__ == "__main__":
    main()
