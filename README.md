# UJIAN TENGAH SEMESTER
## Implementasi Komunikasi Client-Server Aman dengan Enkripsi AES-128-GCM pada Jaringan LAN

| Informasi                | Keterangan                         |
| ------------------------ | ---------------------------------- |
| **Mata Kuliah**    | Network Programming & Administration |
| **Kelas**          | IFN41                              |
| **Program Studi**  | Informatika PJJ S1                 |
| **Kampus**         | Universitas Siber Asia             |
| **Dosen Pengampu** | Abdul Azzam Ajhari, S.Kom., M.Kom. |
| **Kelompok**       | 5                                  |

### Anggota Kelompok dan Kontribusi

| No | Nama                   | NIM          | Kontribusi                                                                         |
| -- | ---------------------- | ------------ | ---------------------------------------------------------------------------------- |
| 1  | Marsani                | 230401010282 | Perancangan jaringan, diagram topologi, pemetaan OSI Layer, pengujian (Soal 1 & 4) |
| 2  | Muhammad Saifulloh     | 220401010207 | Implementasi program tanpa enkripsi, pengujian fungsional (Soal 2)                 |
| 3  | Kristian Hananiel Hura | 220401010289 | Analisis Wireshark, identifikasi kerentanan (Soal 3)                               |
| 4  | Sukandar               | 240401020175 | Implementasi AES-128-GCM, evaluasi komparatif (Soal 4 & 5)                         |

---

## 📌 Tentang Proyek
Proyek ini adalah bentuk penyelesaian Ujian Tengah Semester (UTS) yang berfokus pada **pentingnya keamanan data pada komunikasi jaringan lokal (LAN)**. 

Kami membangun dua set program Client-Server menggunakan Python Socket:
1. **Versi Tanpa Enkripsi:** Menunjukkan kerentanan di mana data (plaintext) yang melintas di jaringan dapat disadap dengan mudah menggunakan perangkat lunak *packet sniffer* seperti Wireshark.
2. **Versi Dengan Enkripsi (AES-128-GCM):** Mengimplementasikan algoritma *Authenticated Encryption* untuk menjamin Kerahasiaan (Confidentiality), Integritas (Integrity), dan Autentikasi asal data, sehingga paket yang disadap hanya berupa karakter acak (*ciphertext*) yang tidak bermakna.

---

## 📂 Struktur Repositori

Proyek ini tertata dalam struktur file berikut:

* **`/` (Root Folder)**
  * [`Laporan_UTS_Kelompok_5.md`](./Laporan_UTS_Kelompok_5.md) — Dokumen Laporan Resmi UTS yang menjawab Soal 1 hingga 5.
  * [`Konten_Presentasi_UTS_Kelompok_5.md`](./Konten_Presentasi_UTS_Kelompok_5.md) — Naskah presentasi & slide yang digunakan dalam video demo.
  * `UTS_NPA_Kelompok_5.pptx` — File Slide Presentasi.
  * `UTS_Network Programming & Administration_2026.pdf` — File Soal UTS.

* **`/Code Program/`** *(Berisi Source Code dan Environment Demo)*
  * [`server_tanpa_enkripsi.py`](./Code%20Program/server_tanpa_enkripsi.py) & [`client_tanpa_enkripsi.py`](./Code%20Program/client_tanpa_enkripsi.py) — Aplikasi rentan (Plaintext).
  * [`server_dengan_enkripsi.py`](./Code%20Program/server_dengan_enkripsi.py) & [`client_dengan_enkripsi.py`](./Code%20Program/client_dengan_enkripsi.py) — Aplikasi aman (AES-GCM).
  * [`generate_kunci.py`](./Code%20Program/generate_kunci.py) — Script pembuat kunci rahasia (*Key Generator*).
  * `docker-compose.yml` & `Dockerfile` — Arsitektur simulasi LAN terisolasi untuk Server, Client, dan Sniffer.
  * [`PANDUAN_DEMO.md`](./Code%20Program/PANDUAN_DEMO.md) — **Buku Panduan Teknis** untuk menjalankan lingkungan demonstrasi.

---

## 🚀 Panduan Menjalankan Demo Praktik

Bagi Anda (Dosen/Penguji) yang ingin menjalankan, memverifikasi, dan mencoba langsung menangkap paket dengan Wireshark, kami telah menyiapkan arsitektur *Docker Compose* agar simulasi berjalan aman tanpa mengganggu sistem komputer *host*.

Silakan ikuti panduan lengkap *step-by-step* yang telah kami sediakan di dalam file berikut:

👉 **[BACA PANDUAN_DEMO.md DI SINI](./Code%20Program/PANDUAN_DEMO.md)**

---
*Dokumen ini dibuat secara terstruktur untuk memenuhi spesifikasi penilaian Ujian Tengah Semester Network Programming & Administration.*
