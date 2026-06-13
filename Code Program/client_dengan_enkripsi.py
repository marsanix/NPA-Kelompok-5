# ============================================================
# Client dengan Enkripsi AES-128-GCM - Versi Perbaikan
# Aplikasi client yang mengenkripsi pesan sebelum mengirim
# ke server, menggunakan authenticated encryption (AES-128-GCM)
# ============================================================

import socket
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64
import os

# Konfigurasi koneksi ke server
# Dapat di-override via environment variable SERVER_HOST (untuk Docker/LAN)
SERVER_HOST = os.environ.get('SERVER_HOST', '127.0.0.1')
SERVER_PORT = int(os.environ.get('SERVER_PORT', '12345'))

# Membaca kunci AES-128 dari file
KUNCI_FILE = 'kunci_rahasia.key'

def muat_kunci():
    """
    Memuat kunci AES-128 dari file.
    Kunci harus sama persis dengan yang digunakan oleh server.
    
    Return:
        bytes: Kunci AES-128 (16 byte)
    """
    if os.path.exists(KUNCI_FILE):
        with open(KUNCI_FILE, 'rb') as f:
            kunci = f.read()
        if len(kunci) == 16:
            return kunci
    
    print(f"[ERROR] File kunci '{KUNCI_FILE}' tidak ditemukan atau tidak valid.")
    print(f"[INFO] Jalankan server terlebih dahulu untuk membuat kunci,")
    print(f"       lalu salin file '{KUNCI_FILE}' ke direktori client.")
    exit(1)


def enkripsi_pesan(pesan, kunci):
    """
    Mengenkripsi pesan menggunakan AES-128-GCM.
    
    Parameter:
        pesan (str): Pesan asli (plaintext) yang akan dienkripsi
        kunci (bytes): Kunci AES-128 (16 byte)
    
    Proses:
        1. Membuat nonce acak sepanjang 12 byte
        2. Membuat objek AESGCM dengan kunci
        3. Mengenkripsi pesan menjadi ciphertext + authentication tag
        4. Menggabungkan nonce + ciphertext + tag
        5. Mengkodekan hasilnya ke format base64
    
    Return:
        str: Data terenkripsi dalam format base64 (nonce + ciphertext + tag)
    """
    # Membuat nonce acak (12 byte untuk GCM)
    nonce = os.urandom(12)

    # Membuat objek AESGCM dan mengenkripsi pesan
    aesgcm = AESGCM(kunci)
    ciphertext_dan_tag = aesgcm.encrypt(nonce, pesan.encode('utf-8'), None)

    # Menggabungkan nonce + ciphertext + tag, lalu encode ke base64
    data_gabungan = nonce + ciphertext_dan_tag
    data_base64 = base64.b64encode(data_gabungan)

    return data_base64


def jalankan_client():
    """
    Fungsi utama untuk menjalankan client terenkripsi.
    Client mengenkripsi pesan sebelum mengirimkannya ke server.
    Client terus berjalan hingga pengguna mengetik 'exit' atau 'quit'.
    """
    # Memuat kunci enkripsi
    kunci = muat_kunci()

    print(f"[CLIENT AMAN] Mode enkripsi: AES-128-GCM")
    print(f"[CLIENT AMAN] Server target: {SERVER_HOST}:{SERVER_PORT}")
    print(f"[CLIENT AMAN] Ketik 'exit' atau 'quit' untuk keluar.\n")

    while True:
        # Meminta pengguna memasukkan pesan
        pesan = input("Masukkan pesan yang ingin dikirim: ")

        # Cek apakah pengguna ingin keluar
        if pesan.lower() in ('exit', 'quit'):
            print("[CLIENT] Keluar dari program.")
            break

        if not pesan.strip():
            print("[CLIENT] Pesan kosong, silakan masukkan pesan.\n")
            continue

        # Membuat koneksi baru untuk setiap pesan
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            client_socket.connect((SERVER_HOST, SERVER_PORT))

            # Mengenkripsi pesan sebelum dikirim
            data_terenkripsi = enkripsi_pesan(pesan, kunci)

            print(f"[CLIENT] Pesan asli      : {pesan}")
            print(f"[CLIENT] Data terenkripsi: {data_terenkripsi.decode('utf-8')[:60]}...")

            # Mengirim data terenkripsi ke server
            client_socket.send(data_terenkripsi)
            print(f"[CLIENT] Data terenkripsi berhasil dikirim.")

            # Menerima balasan dari server
            balasan = client_socket.recv(4096).decode('utf-8')
            print(f"[CLIENT] Balasan server: {balasan}\n")

        except ConnectionRefusedError:
            print("[ERROR] Tidak dapat terhubung ke server. Pastikan server berjalan.\n")
        except Exception as e:
            print(f"[ERROR] Terjadi kesalahan: {e}\n")
        finally:
            client_socket.close()

if __name__ == "__main__":
    jalankan_client()
