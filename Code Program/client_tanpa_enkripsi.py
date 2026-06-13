# ============================================================
# Client Tanpa Enkripsi - Versi Awal
# Aplikasi client sederhana untuk mengirim pesan ke server
# melalui jaringan LAN tanpa perlindungan kriptografi
# ============================================================

import socket
import os

# Konfigurasi koneksi ke server
# Dapat di-override via environment variable SERVER_HOST (untuk Docker/LAN)
SERVER_HOST = os.environ.get('SERVER_HOST', '127.0.0.1')
SERVER_PORT = int(os.environ.get('SERVER_PORT', '12345'))

def jalankan_client():
    """
    Fungsi utama untuk menjalankan client.
    Client akan terhubung ke server, mengirim pesan,
    dan menampilkan balasan dari server.
    Client terus berjalan hingga pengguna mengetik 'exit' atau 'quit'.
    """
    print(f"[CLIENT] Server target: {SERVER_HOST}:{SERVER_PORT}")
    print(f"[CLIENT] Ketik 'exit' atau 'quit' untuk keluar.\n")

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
            # Menghubungkan client ke server
            client_socket.connect((SERVER_HOST, SERVER_PORT))

            # Mengirim pesan ke server dalam bentuk byte (encoding UTF-8)
            client_socket.send(pesan.encode('utf-8'))
            print(f"[CLIENT] Pesan terkirim: {pesan}")

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
