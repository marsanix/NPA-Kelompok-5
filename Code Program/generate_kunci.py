# ============================================================
# Generator Kunci AES-128
# Script untuk membuat file kunci_rahasia.key yang dibutuhkan
# oleh server_dengan_enkripsi.py dan client_dengan_enkripsi.py
# ============================================================

import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KUNCI_FILE = 'kunci_rahasia.key'

def generate_kunci():
    """
    Membuat kunci AES-128 (16 byte) secara acak menggunakan
    Cryptographically Secure Pseudo-Random Number Generator (CSPRNG)
    dan menyimpannya ke file kunci_rahasia.key.
    """
    # Cek apakah file kunci sudah ada
    if os.path.exists(KUNCI_FILE):
        jawaban = input(f"[PERINGATAN] File '{KUNCI_FILE}' sudah ada. Timpa? (y/n): ")
        if jawaban.lower() != 'y':
            print("[INFO] Pembuatan kunci dibatalkan.")
            return

    # Generate kunci AES-128 (128 bit = 16 byte)
    kunci = AESGCM.generate_key(bit_length=128)

    # Simpan kunci ke file
    with open(KUNCI_FILE, 'wb') as f:
        f.write(kunci)

    print(f"[SUKSES] Kunci AES-128 berhasil dibuat!")
    print(f"  File   : {KUNCI_FILE}")
    print(f"  Ukuran : {len(kunci)} byte (128 bit)")
    print(f"\n[INFO] Pastikan file ini tersedia di direktori server DAN client.")
    print(f"[INFO] Jangan bagikan kunci ini melalui jaringan yang tidak aman.")

if __name__ == "__main__":
    generate_kunci()
