# PANDUAN DEMO PRAKTIK - UTS KELOMPOK 5
**Implementasi Komunikasi Client-Server Aman dengan Enkripsi AES-128-GCM pada Jaringan LAN**

Panduan ini berisi langkah-langkah praktis untuk melakukan demonstrasi menggunakan arsitektur Docker yang telah disediakan.

---

## 🏗️ PERSIAPAN AWAL
Pastikan Docker Desktop sudah berjalan di komputer Anda. Buka terminal di dalam folder `Code Program` dan jalankan perintah berikut untuk membangun dan menyalakan semua container:

```bash
docker compose up -d --build
```

---

## 🎬 DEMO 1: Komunikasi TANPA Enkripsi
Pada demo ini, kita akan membuktikan bahwa data yang dikirim tanpa enkripsi (plaintext) dapat dengan mudah disadap menggunakan Wireshark.

*Buka 3 jendela/tab Terminal atau Command Prompt.*

### 1. Jalankan Server (Terminal 1)
Masuk ke container server dan jalankan aplikasi server versi tanpa enkripsi:
```bash
docker exec -it server python server_tanpa_enkripsi.py
```

### 2. Jalankan Penyadapan Real-time Wireshark (Terminal 2 - CMD Windows)
> ⚠️ **PENTING:** Gunakan **Command Prompt (CMD)** biasa untuk terminal ini, **jangan gunakan PowerShell** karena dapat merusak format data biner.

Jalankan perintah berikut untuk menyadap lalu lintas dan menampilkannya langsung di Wireshark Windows Anda:
```cmd
docker exec sniffer tcpdump -i eth0 -U -w - tcp port 12345 | "C:\Program Files\Wireshark\Wireshark.exe" -k -i -
```
*(Jendela Wireshark akan terbuka secara otomatis)*

### 3. Jalankan Client dan Kirim Pesan (Terminal 3)
Masuk ke container client dan jalankan aplikasi client versi tanpa enkripsi:
```bash
docker exec -it client python client_tanpa_enkripsi.py
```
* **Ketikkan sebuah pesan** (misal: "Rapat rahasia pukul 10:00") lalu tekan Enter.
* Perhatikan jendela **Wireshark**. Paket TCP baru akan muncul.
* Di Wireshark, **Klik Kanan** pada salah satu paket tersebut → Pilih **Follow** → **TCP Stream**.
* **Hasil:** Anda akan melihat pesan yang Anda kirim terbaca dengan sangat jelas secara utuh!

*Untuk lanjut ke demo kedua, ketik `exit` di Terminal 3, tekan `Ctrl+C` di Terminal 1 dan Terminal 2, lalu tutup jendela Wireshark.*

---

## 🎬 DEMO 2: Komunikasi DENGAN Enkripsi AES-128-GCM
Pada demo ini, kita akan melihat bagaimana AES-GCM mengamankan data dan mengubahnya menjadi karakter acak yang tidak bisa dibaca oleh penyadap.

### 1. Jalankan Server Enkripsi (Terminal 1)
```bash
docker exec -it server python server_dengan_enkripsi.py
```

### 2. Jalankan Penyadapan Real-time Wireshark (Terminal 2 - CMD Windows)
Sama seperti sebelumnya, gunakan CMD biasa:
```cmd
docker exec sniffer tcpdump -i eth0 -U -w - tcp port 12345 | "C:\Program Files\Wireshark\Wireshark.exe" -k -i -
```

### 3. Jalankan Client Enkripsi dan Kirim Pesan (Terminal 3)
```bash
docker exec -it client python client_dengan_enkripsi.py
```
* **Ketikkan pesan yang sama** (misal: "Rapat rahasia pukul 10:00") lalu tekan Enter.
* Perhatikan jendela **Wireshark** yang terbuka.
* Di Wireshark, **Klik Kanan** pada salah satu paket → Pilih **Follow** → **TCP Stream**.
* **Hasil:** Anda HANYA akan melihat **deretan karakter acak/Base64** yang tidak bermakna! Pesan asli Anda telah sepenuhnya diamankan oleh enkripsi AES-128-GCM.

---

## 🧹 SELESAI (Pembersihan)
Setelah presentasi dan demonstrasi selesai, jangan lupa untuk mematikan dan menghapus environment Docker yang berjalan:

```bash
docker compose down
```
