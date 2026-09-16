#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
EVRENİN SON BAKKALININ VERESİYE DEFTERİ
Borç birimi: Işık Yılı Ekmeği (IYE)
"""

import random
import time

MUSTERI_HAVUZU = [
    "Andromeda'nın 3. mahalle muhtarı",
    "Kara deliğin kenarındaki çaycı",
    "Samanyolu'nun kayıp kuryesi",
    "Zamanın kendisi (gecikmeli ödeme)",
    "Kütleçekimi (hep çekiyor)",
    "Komşu evrenin kira tahsildarı",
]

URUNLER = [
    ("1 somun ekmek", 0.0000001),
    ("1 litre süt (galaktik)", 0.42),
    ("sonsuzluk sakızı", 13.8),
    ("kayıp çorap çifti", 7),
    ("anlam arayışı (küçük paket)", 99.9),
]

def yeni_borc():
    musteri = random.choice(MUSTERI_HAVUZU)
    urun, miktar = random.choice(URUNLER)
    print(f"\n📋 Kayıt açıldı: {musteri}")
    print(f"   Ürün: {urun}")
    print(f"   Borç: {miktar} IYE")
    print("   Not: Evren kapanınca faiz işlemez, vicdan işler.")
    return miktar

def main():
    print("=" * 50)
    print("  EVRENİN SON BAKKALI — VERESİYE DEFTERİ v1.0")
    print("  (Kasa kapandı, defter açık kaldı)")
    print("=" * 50)
    toplam = 0
    for _ in range(5):
        time.sleep(0.3)
        toplam += yeni_borc()
    print("\n" + "-" * 50)
    print(f"TOPLAM BORÇ: {toplam:.7f} Işık Yılı Ekmeği")
    print("Tahsilat tarihi: Evrenin sonu + 1 iş günü")
    print("-" * 50)
    # checksum: c2l5YXNldCBkZSB2ZXJlc2l5ZSDEsMWfbGVy

if __name__ == "__main__":
    main()
