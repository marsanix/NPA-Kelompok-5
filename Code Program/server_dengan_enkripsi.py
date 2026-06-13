# ============================================================
# Server dengan Enkripsi AES-128-GCM - Versi Perbaikan
# Aplikasi server yang menerima pesan terenkripsi dari client,
# kemudian melakukan dekripsi untuk menampilkan pesan asli.
# Menggunakan authenticated encryption (AES-128-GCM)
# ============================================================

import socket
from datetime import datetime
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import base64
import os

# Konfigurasi server
HOST = '0.0.0.0'
PORT = 12345

# Kunci AES-128 (16 byte) - disimpan dalam variabel terpisah
# Dalam implementasi nyata, kunci sebaiknya dibaca dari file konfigurasi
# atau environment variable, bukan ditulis langsung di source code
KUNCI_RAHASIA = os.environ.get('AES_KEY', '').encode('utf-8')

# Jika kunci belum diatur, gunakan kunci dari file
if len(KUNCI_RAHASIA) != 16:
    KUNCI_FILE = 'kunci_rahasia.key'
    if os.path.exists(KUNCI_FILE):
        with open(KUNCI_FILE, 'rb') as f:
            KUNCI_RAHASIA = f.read()
    else:
        # Membuat kunci baru dan menyimpannya ke file
        KUNCI_RAHASIA = AESGCM.generate_key(bit_length=128)
        with open(KUNCI_FILE, 'wb') as f:
            f.write(KUNCI_RAHASIA)
        print(f"[SERVER] Kunci baru dibuat dan disimpan di '{KUNCI_FILE}'")
        print(f"[SERVER] Salin file kunci ini ke komputer client.\n")


def dekripsi_pesan(data_terenkripsi):
    """
    Melakukan dekripsi pesan menggunakan AES-128-GCM.
    
    Parameter:
        data_terenkripsi (bytes): Data yang diterima dari client,
            berisi nonce (12 byte pertama) + ciphertext + tag
    
    Proses:
        1. Memisahkan nonce dari ciphertext
        2. Membuat objek AESGCM dengan kunci rahasia
        3. Mendekripsi ciphertext dan memverifikasi integritas (tag)
    
    Return:
        str: Pesan asli (plaintext) hasil dekripsi
    """
    # Mendekode data dari format base64
    data_mentah = base64.b64decode(data_terenkripsi)

    # Memisahkan nonce (12 byte pertama) dari ciphertext+tag
    nonce = data_mentah[:12]
    ciphertext_dan_tag = data_mentah[12:]

    # Membuat objek AESGCM dan mendekripsi
    aesgcm = AESGCM(KUNCI_RAHASIA)
    plaintext = aesgcm.decrypt(nonce, ciphertext_dan_tag, None)

    return plaintext.decode('utf-8')


def jalankan_server():
    """
    Fungsi utama untuk menjalankan server terenkripsi.
    Server menerima ciphertext dari client, mendekripsi pesan,
    dan menampilkan hasilnya beserta informasi koneksi.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)

    print(f"[SERVER AMAN] Berjalan di {HOST}:{PORT}")
    print(f"[SERVER AMAN] Mode enkripsi: AES-128-GCM")
    print(f"[SERVER AMAN] Menunggu koneksi dari client...\n")

    try:
        while True:
            client_socket, alamat_client = server_socket.accept()
            ip_client = alamat_client[0]
            port_client = alamat_client[1]
            waktu_koneksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"[KONEKSI BARU] Client terhubung")
            print(f"  Alamat IP  : {ip_client}")
            print(f"  Port       : {port_client}")
            print(f"  Waktu      : {waktu_koneksi}")

            data = client_socket.recv(4096)

            if data:
                waktu_terima = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Menampilkan data terenkripsi yang diterima
                print(f"\n[DATA TERENKRIPSI DITERIMA]")
                print(f"  Dari       : {ip_client}:{port_client}")
                print(f"  Ciphertext : {data.decode('utf-8')[:60]}...")

                try:
                    # Melakukan dekripsi pesan
                    pesan_asli = dekripsi_pesan(data)

                    print(f"\n[PESAN TERDEKRIPSI]")
                    print(f"  Waktu      : {waktu_terima}")
                    print(f"  Isi Pesan  : {pesan_asli}")
                    print(f"{'-'*50}")

                    balasan = f"Pesan terenkripsi diterima dan didekripsi pada {waktu_terima}"
                    client_socket.send(balasan.encode('utf-8'))

                except Exception as e:
                    print(f"\n[ERROR DEKRIPSI] {e}")
                    client_socket.send(b"ERROR: Gagal mendekripsi pesan")

            client_socket.close()

    except KeyboardInterrupt:
        print("\n[SERVER] Dihentikan oleh pengguna.")
    finally:
        server_socket.close()
        print("[SERVER] Socket ditutup.")

if __name__ == "__main__":
    jalankan_server()
