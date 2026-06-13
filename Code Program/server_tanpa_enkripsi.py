# ============================================================
# Server Tanpa Enkripsi - Versi Awal
# Aplikasi server sederhana untuk menerima pesan dari client
# melalui jaringan LAN tanpa perlindungan kriptografi
# ============================================================

import socket
from datetime import datetime

# Konfigurasi server
HOST = '0.0.0.0'   # Menerima koneksi dari semua antarmuka jaringan
PORT = 12345        # Nomor port yang digunakan untuk komunikasi

def jalankan_server():
    """
    Fungsi utama untuk menjalankan server.
    Server akan mendengarkan koneksi masuk dari client,
    menerima pesan, dan menampilkan informasi koneksi.
    """
    # Membuat objek socket dengan protokol TCP (SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Mengatur opsi socket agar port dapat segera digunakan kembali
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Mengikat socket ke alamat dan port yang telah ditentukan
    server_socket.bind((HOST, PORT))

    # Memulai mendengarkan koneksi masuk (maksimal 5 antrian)
    server_socket.listen(5)

    print(f"[SERVER] Berjalan di {HOST}:{PORT}")
    print(f"[SERVER] Menunggu koneksi dari client...\n")

    try:
        while True:
            # Menerima koneksi dari client
            client_socket, alamat_client = server_socket.accept()
            ip_client = alamat_client[0]
            port_client = alamat_client[1]
            waktu_koneksi = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            print(f"[KONEKSI BARU] Client terhubung")
            print(f"  Alamat IP  : {ip_client}")
            print(f"  Port       : {port_client}")
            print(f"  Waktu      : {waktu_koneksi}")

            # Menerima data dari client (maksimal 4096 byte)
            data = client_socket.recv(4096)

            if data:
                pesan = data.decode('utf-8')
                waktu_terima = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                print(f"\n[PESAN DITERIMA]")
                print(f"  Dari       : {ip_client}:{port_client}")
                print(f"  Waktu      : {waktu_terima}")
                print(f"  Isi Pesan  : {pesan}")
                print(f"{'-'*50}")

                # Mengirim konfirmasi ke client
                balasan = f"Pesan diterima oleh server pada {waktu_terima}"
                client_socket.send(balasan.encode('utf-8'))

            # Menutup koneksi dengan client
            client_socket.close()

    except KeyboardInterrupt:
        print("\n[SERVER] Dihentikan oleh pengguna.")
    finally:
        server_socket.close()
        print("[SERVER] Socket ditutup.")

if __name__ == "__main__":
    jalankan_server()
