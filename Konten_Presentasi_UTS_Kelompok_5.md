# KONTEN PRESENTASI UTS — KELOMPOK 5
## Network Programming & Administration
### Durasi Target: 15 Menit (Termasuk Demo Praktik)

---

> **Petunjuk Penggunaan File Ini:**
> - Total **15 slide** + **2 sesi demo praktik** = target **~15 menit**.
> - Setiap slide memiliki **isi visual** dan **narasi** (🎤) yang dibacakan presenter.
> - Simbol 🎬 menandai **sesi demo praktik langsung** (screen recording).
> - Narasi ditulis natural dan ringkas — jangan dibaca kata per kata, gunakan sebagai panduan.
> - Estimasi waktu diberikan per bagian.
> - ✅ Seluruh poin dari Soal 1–5 sudah tercakup.

---

## SLIDE 1: HALAMAN JUDUL & ANGGOTA KELOMPOK
**⏱ Estimasi: 30 detik**
**📋 Mencakup: Identitas kelompok & kontribusi anggota**

### Isi Visual Slide:
```
UJIAN TENGAH SEMESTER
Network Programming & Administration

"Implementasi Komunikasi Client-Server Aman
dengan Enkripsi AES-128-GCM pada Jaringan LAN"

Kelompok 5 — Kelas IFN41 | Informatika PJJ S1
Universitas Siber Asia
Dosen: Abdul Azzam Ajhari, S.Kom., M.Kom.

┌───────────────────────────────────────────────────────────┐
│ Marsani (230401010282)          → Perancangan jaringan    │
│ Muhammad Saifulloh (220401010207) → Implementasi awal     │
│ Kristian Hananiel Hura (220401010289) → Analisis Wireshark│
│ Sukandar (240401020175)         → Enkripsi AES-128-GCM    │
└───────────────────────────────────────────────────────────┘
```

### 🎤 Narasi:
> "Assalamualaikum warahmatullahi wabarakatuh. Perkenalkan kami dari Kelompok 5 kelas IFN41, Universitas Siber Asia. Kami akan mempresentasikan proyek UTS Network Programming and Administration tentang implementasi komunikasi client-server aman dengan enkripsi AES-128-GCM. Anggota kami: Marsani — perancangan jaringan, Muhammad Saifulloh — implementasi awal, Kristian — analisis Wireshark, dan Sukandar — implementasi enkripsi."

---

## SLIDE 2: LATAR BELAKANG & TUJUAN
**⏱ Estimasi: 40 detik**
**📋 Mencakup: Pendahuluan & permasalahan**

### Isi Visual Slide:
```
LATAR BELAKANG & TUJUAN

📌 Skenario:
   Unit administrasi akademik mengirim pesan sensitif
   (jadwal rapat, kode verifikasi) melalui jaringan LAN

⚠️ Masalah:
   Data dikirim sebagai PLAINTEXT → mudah disadap Wireshark

🎯 Tujuan:
   ┌──────────────────────────────────────────────────┐
   │ Versi 1: Client-server TANPA enkripsi            │
   │          → Buktikan adanya kerentanan            │
   │ Versi 2: Client-server DENGAN AES-128-GCM        │
   │          → Amankan komunikasi data               │
   └──────────────────────────────────────────────────┘
```

### 🎤 Narasi:
> "Bayangkan unit administrasi kampus mengirim pesan sensitif melalui jaringan LAN. Jika pesan dikirim tanpa perlindungan — sebagai plaintext — siapa pun di jaringan bisa membacanya dengan Wireshark. Maka kami membuat dua versi aplikasi: tanpa enkripsi untuk membuktikan kerentanan, lalu dengan AES-128-GCM untuk mengamankan komunikasi."

---

## SLIDE 3: KLASIFIKASI JARINGAN & PEMILIHAN LAN
**⏱ Estimasi: 45 detik**
**📋 Mencakup: Soal 1.1 (PAN/LAN/MAN/WAN) + Soal 1.2 (alasan LAN)**

### Isi Visual Slide:
```
KLASIFIKASI JARINGAN

┌──────────┬──────────────────┬──────────────────────────┐
│ Jenis    │ Cakupan          │ Contoh                   │
├──────────┼──────────────────┼──────────────────────────┤
│ PAN      │ 1 – 10 meter     │ Bluetooth, USB           │
│ LAN ✅   │ 10 m – 1 km      │ Lab kampus, kantor       │
│ MAN      │ 1 – 50 km        │ Antar-gedung satu kota   │
│ WAN      │ > 50 km          │ Internet                 │
└──────────┴──────────────────┴──────────────────────────┘

MENGAPA LAN?
  ✓ Sesuai skenario komunikasi internal kampus
  ✓ Kecepatan tinggi & latensi rendah
  ✓ Mudah dikonfigurasi dan diuji
  ✓ Kontrol penuh terhadap perangkat
```

### 🎤 Narasi:
> "Ada empat klasifikasi jaringan berdasarkan cakupan: PAN untuk jangkauan personal seperti Bluetooth, LAN untuk satu gedung atau kampus, MAN untuk satu kota, dan WAN untuk skala global seperti internet. Kami memilih LAN karena sesuai skenario kampus, kecepatannya tinggi, mudah dikonfigurasi, dan kami punya kontrol penuh atas perangkat."

---

## SLIDE 4: TOPOLOGI & PARAMETER JARINGAN
**⏱ Estimasi: 40 detik**
**📋 Mencakup: Soal 1.3 (topologi) + Soal 1.4 (IP, port, protokol, arah)**

### Isi Visual Slide:
```
TOPOLOGI JARINGAN (Star — LAN)

              ┌──────────────────────┐
              │   Switch / Router    │
              │   192.168.1.1/24     │
              └────┬────────────┬────┘
                   │            │
         ┌─────────┴───┐  ┌─────┴──────────┐
         │  SERVER     │  │    CLIENT      │
         │ 192.168.1.10│  │ 192.168.1.20   │
         │ Port: 12345 │  │ Port: Dinamis  │
         └─────────────┘  └────────────────┘

  • Protokol : TCP (reliable, connection-oriented)
  • Subnet   : 192.168.1.0/24
  • Arah     : Client → Server (pesan)
               Server → Client (balasan)
```

### 🎤 Narasi:
> "Topologi star sederhana: server di IP 192.168.1.10 port 12345, client di 192.168.1.20 dengan port dinamis, terhubung melalui switch. Protokol TCP dipilih karena menjamin data sampai utuh dan berurutan. Client mengirim pesan ke server, server membalas konfirmasi."

---

## SLIDE 5: OSI LAYER, ALUR TCP & DIAGRAM ALIR
**⏱ Estimasi: 50 detik**
**📋 Mencakup: Soal 1.5 (OSI Layer) + Soal 1.6 (diagram alir)**

### Isi Visual Slide:
```
PEMETAAN OSI LAYER                 DIAGRAM ALIR
                                   ════════════════
Layer 7 Application  → Python     CLIENT:
Layer 6 Presentation → UTF-8/AES  Mulai → Buat socket → Connect
Layer 5 Session      → TCP conn         → Input pesan → [Enkripsi?]
Layer 4 Transport    → TCP:12345        → Kirim → Terima balasan
Layer 3 Network      → IPv4             → Tutup → Selesai
Layer 2 Data Link    → Ethernet
Layer 1 Physical     → Kabel/WiFi  SERVER:
                                   Mulai → Buat socket → Bind
ALUR KONEKSI TCP:                    → Listen → Accept koneksi
CLIENT         SERVER                → Terima data → [Dekripsi?]
│── SYN ──────→│                     → Tampilkan → Kirim balasan
│←─ SYN-ACK ───│                     → Tutup koneksi client
│── ACK ──────→│                     → Kembali ke Accept (loop)
│── DATA ─────→│
│←─ BALASAN ───│
│── FIN ──────→│
```

### 🎤 Narasi:
> "Komunikasi dipetakan ke tujuh layer OSI: Layer 7 adalah program Python, Layer 6 menangani encoding UTF-8 dan enkripsi AES, Layer 5 mengelola sesi TCP, Layer 4 adalah protokol TCP pada port 12345 dengan three-way handshake SYN, SYN-ACK, ACK. Layer 3 ke bawah menangani routing IP, framing Ethernet, dan transmisi fisik.
>
> Diagram alir di sisi client: buat socket, connect ke server, input pesan, kirim, terima balasan, tutup. Di sisi server: buat socket, bind, listen, accept koneksi, terima data, tampilkan, kirim balasan, lalu kembali menunggu koneksi baru."

---

## SLIDE 6: IMPLEMENTASI TANPA ENKRIPSI
**⏱ Estimasi: 40 detik**
**📋 Mencakup: Soal 2.1–2.5 (kode + penjelasan fungsi)**

### Isi Visual Slide:
```
IMPLEMENTASI TANPA ENKRIPSI

📄 SERVER:                          📄 CLIENT:
socket()     → Buat socket TCP     socket()    → Buat socket TCP
bind()       → Ikat ke 0.0.0.0:    connect()   → Hubungkan ke server
               12345               input()     → Minta pesan user
listen(5)    → Dengarkan (max 5)   encode()    → Konversi ke byte
accept()     → Terima koneksi      send()      → Kirim ke server
recv(4096)   → Terima data         recv(4096)  → Terima balasan
decode()     → Konversi ke string  decode()    → Konversi ke string
send()       → Kirim balasan       close()     → Tutup koneksi
close()      → Tutup koneksi

⚠️ MASALAH: pesan.encode('utf-8') = HANYA konversi teks ke byte
   → TIDAK ADA pengacakan → Data di jaringan = PLAINTEXT!
```

### 🎤 Narasi:
> "Implementasi tanpa enkripsi menggunakan fungsi-fungsi socket standar. Server: socket untuk membuat koneksi TCP, bind untuk mengikat ke port, listen untuk mendengarkan, accept untuk menerima koneksi, recv untuk terima data, lalu decode UTF-8. Client: socket, connect, input pesan, encode UTF-8, send, terima balasan.
>
> Masalah kritis: encode UTF-8 hanya mengkonversi teks ke byte tanpa pengacakan apapun. Data di jaringan sama persis dengan pesan asli. Mari kita buktikan."

---

## 🎬 DEMO PRAKTIK 1: TANPA ENKRIPSI + WIRESHARK
**⏱ Estimasi: 1 menit 45 detik**
**📋 Mencakup: Soal 2 (bukti program) + Soal 3.1–3.4 (Wireshark)**

### Skenario Demo:
```
LANGKAH-LANGKAH DEMO:

  1. [Terminal 1] Jalankan server:
     > docker exec -it server python server_tanpa_enkripsi.py

  2. [Terminal 2] Buka Sniffer ke Wireshark (via CMD):
     > docker exec sniffer tcpdump -i eth0 -U -w - tcp port 12345 | "C:\Program Files\Wireshark\Wireshark.exe" -k -i -

  3. [Terminal 3] Jalankan client:
     > docker exec -it client python client_tanpa_enkripsi.py
     Kirim pesan: "Rapat dosen pukul 10:00 di Ruang Utama"

  4. Tunjukkan:
     • Server menampilkan pesan + info koneksi (IP, port, waktu)
     • Client menampilkan balasan server

  5. [Wireshark] Tunjukkan jendela Wireshark yang terbuka otomatis
     → Klik Kanan → Follow TCP Stream
     → TUNJUKKAN pesan TERBACA JELAS!
```

### 🎤 Narasi Selama Demo:
> "Wireshark sudah berjalan dengan filter tcp.port 12345. Saya jalankan server, lalu client. Pesan yang dikirim: 'Rapat dosen pukul 10:00 di Ruang Utama'. Server berhasil menampilkan pesan beserta IP client, port, dan waktu penerimaan.
>
> Sekarang lihat Wireshark — Follow TCP Stream — dan pesan terbaca jelas secara utuh! Tidak ada perlindungan apapun. Inilah bukti nyata bahwa komunikasi tanpa enkripsi sangat rentan."

---

## SLIDE 7: RISIKO KEAMANAN & SOLUSI
**⏱ Estimasi: 40 detik**
**📋 Mencakup: Soal 2.6 (risiko) + Soal 3.5 (5 risiko) + Soal 3.6 (solusi)**

### Isi Visual Slide:
```
5 RISIKO KEAMANAN TERIDENTIFIKASI

  ❌ 1. PENYADAPAN (Eavesdropping)  → Pesan terbaca di Wireshark
  ❌ 2. KEBOCORAN INFORMASI         → Data sensitif bocor
  ❌ 3. MANIPULASI PESAN (MitM)     → Pesan diubah tanpa terdeteksi
  ❌ 4. IMPERSONASI CLIENT          → Pesan palsu ke server
  ❌ 5. SERANGAN REPLAY             → Paket sah dikirim ulang

SOLUSI YANG DIPERLUKAN:
  🔐 Enkripsi data (AES-128)
  🔐 Authenticated encryption (AES-GCM) → verifikasi integritas
  🔐 Pertukaran kunci aman (Diffie-Hellman / TLS)
  🔐 Nonce / timestamp untuk cegah replay
  🔐 Autentikasi client (sertifikat / token)
```

### 🎤 Narasi:
> "Lima risiko teridentifikasi: penyadapan, kebocoran informasi, manipulasi pesan, impersonasi client, dan serangan replay. Solusinya mencakup enkripsi AES-128, authenticated encryption seperti AES-GCM yang sekaligus memverifikasi integritas, pertukaran kunci yang aman, penggunaan nonce, dan autentikasi client. Selanjutnya kita implementasikan solusi ini."

---

## SLIDE 8: KONSEP AES-128-GCM & PENGELOLAAN KUNCI
**⏱ Estimasi: 45 detik**
**📋 Mencakup: Soal 4.4 (plaintext/ciphertext/key/nonce) + Soal 4.5 (pengelolaan kunci)**

### Isi Visual Slide:
```
AES-128-GCM — AUTHENTICATED ENCRYPTION

┌─────────────┬──────────────────────────────────────────┐
│ Plaintext   │ Pesan asli, bisa dibaca siapa saja       │
│ Ciphertext  │ Pesan teracak, tidak bisa dibaca         │
│ Key (Kunci) │ Nilai rahasia 128-bit (16 byte)          │
│ Nonce / IV  │ Nilai acak 12 byte, unik tiap pengiriman │
│ Auth Tag    │ "Sidik jari" 16 byte, verifikasi         │
└─────────────┴──────────────────────────────────────────┘

KEUNGGULAN:                     PENGELOLAAN KUNCI:
✅ Kerahasiaan (enkripsi)       • Generate otomatis (CSPRNG)
✅ Integritas (auth tag)        • Disimpan di kunci_rahasia.key
✅ Autentikasi (kunci valid)    • Terpisah dari source code
                                • Distribusi manual (flash drive)
→ Mengatasi 3/5 risiko!         • TIDAK dikirim via jaringan
```

### 🎤 Narasi:
> "AES-128-GCM menggunakan beberapa komponen: plaintext — pesan asli, ciphertext — pesan teracak, key — kunci rahasia 128-bit, nonce — nilai acak 12 byte unik tiap pengiriman, dan authentication tag — sidik jari 16 byte untuk verifikasi.
>
> Keunggulannya: kerahasiaan, integritas, dan autentikasi sekaligus — mengatasi tiga dari lima risiko. Kunci di-generate secara acak, disimpan di file terpisah dari source code, dan didistribusikan manual via flash drive — tidak pernah dikirim melalui jaringan."

---

## SLIDE 9: ALUR ENKRIPSI/DEKRIPSI & HIGHLIGHT KODE
**⏱ Estimasi: 45 detik**
**📋 Mencakup: Soal 4.1–4.3 (enkripsi/dekripsi) + Soal 4.6 (kunci tidak terbuka)**

### Isi Visual Slide:
```
ALUR ENKRIPSI (Client)           ALUR DEKRIPSI (Server)
══════════════════════           ══════════════════════
"Rapat dosen pukul 10:00"       "mjvy8kL2n5..."
     │                                │
[1] Buat nonce 12 byte           [1] Decode Base64
[2] Enkripsi AES-GCM             [2] Pisahkan nonce + ciphertext
[3] Gabung: nonce+cipher+tag     [3] Dekripsi + verifikasi tag ✓
[4] Encode Base64                     (tag salah = TOLAK ❌)
     │                           [4] Decode UTF-8
     ▼                                ▼
"mjvy8kL2n5..." ── TCP ──→      "Rapat dosen pukul 10:00" ✅

INTI KODE:
┌────────────────────────────────────────────────────────┐
│ # Enkripsi (client)                                    │
│ nonce = os.urandom(12)                                 │
│ ciphertext = aesgcm.encrypt(nonce, plaintext, None)    │
│ return base64.b64encode(nonce + ciphertext)            │
│                                                        │
│ # Dekripsi (server)                                    │
│ nonce = data[:12]; cipher = data[12:]                  │
│ plaintext = aesgcm.decrypt(nonce, cipher, None)        │
└────────────────────────────────────────────────────────┘
  ⚠️ Kunci dimuat dari file, TIDAK tampil di kode/video
```

### 🎤 Narasi:
> "Di client: buat nonce acak, enkripsi pesan dengan AES-GCM menghasilkan ciphertext plus auth tag, gabungkan dengan nonce, encode Base64, kirim via TCP. Di server: decode Base64, pisahkan nonce dari ciphertext, lalu dekripsi. GCM memverifikasi auth tag dulu — jika pesan dimanipulasi, tag tidak cocok dan dekripsi gagal.
>
> Perhatikan bahwa kunci dimuat dari file terpisah dan tidak pernah ditampilkan secara terbuka di kode maupun video. Sekarang mari kita buktikan perbedaannya."

---

## 🎬 DEMO PRAKTIK 2: DENGAN ENKRIPSI + WIRESHARK
**⏱ Estimasi: 2 menit**
**📋 Mencakup: Soal 4.7 (pengujian ulang + perbedaan dengan Soal 3)**

### Skenario Demo:
```
LANGKAH-LANGKAH DEMO:

  1. [Terminal 1] Jalankan server terenkripsi:
     > docker exec -it server python server_dengan_enkripsi.py

  2. [Terminal 2] Buka Sniffer ke Wireshark (via CMD):
     > docker exec sniffer tcpdump -i eth0 -U -w - tcp port 12345 | "C:\Program Files\Wireshark\Wireshark.exe" -k -i -

  3. [Terminal 3] Jalankan client terenkripsi:
     > docker exec -it client python client_dengan_enkripsi.py
     Kirim pesan: "Rapat dosen pukul 10:00 di Ruang Utama"

  4. Tunjukkan di terminal:
     • Client: PLAINTEXT dan CIPHERTEXT
     • Server: CIPHERTEXT diterima → PLAINTEXT hasil dekripsi

  5. [Wireshark] Tunjukkan jendela Wireshark yang terbuka otomatis
     → Klik Kanan → Follow TCP Stream
     → Hanya karakter acak Base64! PESAN TIDAK BISA DIBACA ✅

  6. BANDINGKAN:
     "Tadi plaintext terbaca, sekarang hanya karakter acak"
```

### 🎤 Narasi Selama Demo:
> "Server berjalan dalam mode AES-128-GCM. Saya jalankan client, ketik pesan yang sama: 'Rapat dosen pukul 10:00 di Ruang Utama'. Di terminal terlihat plaintext asli dan ciphertext yang dikirim.
>
> Sekarang Wireshark — Follow TCP Stream — dan bandingkan dengan demo sebelumnya! Tadi pesan terbaca jelas, sekarang hanya deretan karakter acak Base64. Meskipun paket berhasil ditangkap, isinya tidak bisa dibaca tanpa kunci dekripsi."

---

## SLIDE 10: TABEL EVALUASI KOMPARATIF
**⏱ Estimasi: 35 detik**
**📋 Mencakup: Soal 5.1 (tabel perbandingan) + Soal 5.2 (perubahan tingkat keamanan)**

### Isi Visual Slide:
```
EVALUASI KOMPARATIF (Berdasarkan Bukti Wireshark)

┌──────────────────────┬───────────────────┬──────────────────┐
│ Kriteria             │ Tanpa Enkripsi    │ Dengan AES-GCM   │
├──────────────────────┼───────────────────┼──────────────────┤
│ Kerahasiaan          │ ❌ Tidak ada      │ ✅ Terjamin     │
│ Integritas           │ ❌ Tidak ada      │ ✅ Auth tag     │
│ Autentikasi          │ ❌ Tidak ada      │ 🟡 Parsial      │
│ Wireshark            │ ❌ Terbaca jelas  │ ✅ Data acak    │
│ Anti-replay          │ ❌ Tidak ada      │ 🟡 Parsial      │
│ Kompleksitas         │ 🟢 Rendah         │ 🟡 Sedang       │
│ Overhead             │ 🟢 Minimal        │ 🟡 Sedikit naik │
└──────────────────────┴───────────────────┴──────────────────┘

  Bukti Wireshark:
  🔴 Sebelum → "Rapat dosen pukul 10:00" terbaca 100%
  🟢 Sesudah → "mjvy8kL2..." hanya karakter acak
```

### 🎤 Narasi:
> "Dari tabel evaluasi, perubahan keamanannya sangat signifikan. Kerahasiaan dan integritas yang tadinya tidak ada, sekarang terjamin. Data di Wireshark yang tadinya terbaca jelas, sekarang hanya karakter acak. Trade-off hanya pada kompleksitas dan sedikit overhead — sangat worth it untuk keamanan yang jauh lebih baik."

---

## SLIDE 11: RISIKO TERSISA & REKOMENDASI KEAMANAN
**⏱ Estimasi: 45 detik**
**📋 Mencakup: Soal 5.3 (risiko tersisa) + Soal 5.4 (6 rekomendasi administrasi)**

### Isi Visual Slide:
```
RISIKO TERSISA                     6 REKOMENDASI ADMINISTRASI
═══════════════                    ══════════════════════════

⚠️ Kunci bisa bocor               🔒 1. Access Control
⚠️ Replay attack masih mungkin       MAC filtering, VLAN, firewall
⚠️ Belum ada autentikasi client
⚠️ Metadata masih terlihat         🔑 2. Key Management
⚠️ Kunci statis tanpa rotasi         Rotasi 30 hari, Diffie-Hellman

                                   📋 3. Logging
                                      Catat koneksi & dekripsi

                                   🪪 4. Client Authentication
                                      Token / TLS mutual auth

                                   👁️ 5. Connection Monitoring
                                      IDS, rate limiting

                                   🔄 6. Dependency Updates
                                      Update library, pip-audit
```

### 🎤 Narasi:
> "Meskipun lebih aman, risiko tersisa antara lain: kunci bisa bocor, replay attack masih mungkin, belum ada autentikasi identitas client, metadata masih terlihat, dan kunci statis tanpa rotasi. Untuk itu kami rekomendasikan enam langkah administrasi: pembatasan akses jaringan, rotasi kunci berkala, pencatatan log, autentikasi client, pemantauan koneksi dengan IDS, dan pembaruan library secara rutin."

---

## SLIDE 12: JADWAL PENGERJAAN & PEMBAGIAN TUGAS
**⏱ Estimasi: 30 detik**
**📋 Mencakup: Soal 5.5 (jadwal & pembagian tugas)**

### Isi Visual Slide:
```
JADWAL PENGERJAAN & PEMBAGIAN TUGAS (Total: ~2 Minggu)

┌────┬────────────────────────────────────┬─────────────────────┬────────┐
│ No │ Kegiatan                           │ PIC                 │ Durasi │
├────┼────────────────────────────────────┼─────────────────────┼────────┤
│ 1  │ Analisis kebutuhan & perancangan   │ Marsani             │ 2 hari │
│ 2  │ Diagram topologi & flowchart       │ Marsani             │ 1 hari │
│ 3  │ Implementasi tanpa enkripsi        │ Muhammad Saifulloh  │ 2 hari │
│ 4  │ Pengujian fungsional               │ Muhammad Saifulloh  │ 1 hari │
│ 5  │ Instalasi Wireshark & analisis     │ Kristian H. Hura    │ 2 hari │
│ 6  │ Identifikasi kerentanan & dokumen  │ Kristian H. Hura    │ 1 hari │
│ 7  │ Implementasi AES-128-GCM           │ Sukandar            │ 3 hari │
│ 8  │ Pengujian ulang Wireshark          │ Marsani             │ 1 hari │
│ 9  │ Evaluasi komparatif & rekomendasi  │ Sukandar            │ 1 hari │
│ 10 │ Penyusunan laporan & refleksi      │ Seluruh anggota     │ 2 hari │
└────┴────────────────────────────────────┴─────────────────────┴────────┘
```

### 🎤 Narasi:
> "Pengerjaan proyek dilakukan bertahap selama kurang lebih dua minggu. Marsani mengerjakan analisis dan perancangan di awal. Muhammad Saifulloh mengimplementasikan program awal dan pengujian. Kristian melakukan analisis Wireshark dan identifikasi kerentanan. Sukandar mengimplementasikan AES-GCM dan evaluasi. Tahap akhir — penyusunan laporan — dikerjakan bersama seluruh anggota."

---

## SLIDE 13: REFLEKSI KELOMPOK
**⏱ Estimasi: 35 detik**
**📋 Mencakup: Soal 5.6 (kendala, solusi, peningkatan)**

### Isi Visual Slide:
```
REFLEKSI KELOMPOK

🔴 Kendala:                        🟢 Solusi:
• Pemahaman konsep kriptografi     • Sesi belajar bersama
  (ECB vs CBC vs GCM)               (ref: William Stallings)
• Konfigurasi Windows Firewall     • Panduan konfigurasi
  memblokir port 12345               step-by-step
• Capture paket di localhost       • Instalasi Npcap untuk
  tidak bisa tanpa driver            loopback capture

🔵 Peningkatan Masa Depan:
• Pertukaran kunci otomatis (Diffie-Hellman / TLS)
• Multi-client (threading / asyncio)
• GUI dengan Tkinter / PyQt
• Logging ke file & validasi nonce
```

### 🎤 Narasi:
> "Kendala utama kami: memahami perbedaan mode AES, Windows Firewall yang memblokir port, dan capture paket di localhost. Kami mengatasinya melalui sesi belajar bersama menggunakan referensi Stallings, membuat panduan konfigurasi firewall, dan menginstal Npcap. Ke depan, kami berencana menambahkan pertukaran kunci otomatis, dukungan multi-client, antarmuka grafis, dan validasi nonce."

---

## SLIDE 14: KESIMPULAN
**⏱ Estimasi: 35 detik**

### Isi Visual Slide:
```
KESIMPULAN

  1️⃣  Komunikasi tanpa enkripsi di LAN SANGAT RENTAN
      → Wireshark membuktikan pesan plaintext mudah dibaca

  2️⃣  AES-128-GCM EFEKTIF lindungi kerahasiaan & integritas
      → Data di Wireshark hanya karakter acak tak bermakna

  3️⃣  Enkripsi BUKAN solusi tunggal
      → Perlu juga: key management, autentikasi,
        monitoring, dan administrasi keamanan

  4️⃣  Implementasi langsung = pemahaman MENDALAM
      → Teori + praktik = pengalaman belajar terbaik

  ══════════════════════════════════════════════════
       🔐 Keamanan bukan fitur tambahan,
          keamanan adalah KEHARUSAN.
  ══════════════════════════════════════════════════
```

### 🎤 Narasi:
> "Kesimpulannya: pertama, komunikasi tanpa enkripsi sangat rentan — sudah kita buktikan langsung. Kedua, AES-128-GCM efektif melindungi kerahasiaan dan integritas. Ketiga, enkripsi bukan solusi tunggal — diperlukan administrasi keamanan menyeluruh. Keempat, implementasi langsung memberikan pemahaman lebih mendalam. Keamanan bukan fitur tambahan — keamanan adalah keharusan."

---

## SLIDE 15: PENUTUP & DAFTAR PUSTAKA
**⏱ Estimasi: 15 detik**

### Isi Visual Slide:
```
TERIMA KASIH 🙏

Kelompok 5 — Kelas IFN41
Universitas Siber Asia

Marsani | Muhammad Saifulloh
Kristian Hananiel Hura | Sukandar

Daftar Pustaka:
• Stallings (2020) — Cryptography and Network Security
• Kurose & Ross (2021) — Computer Networking
• Tanenbaum (2021) — Computer Networks
• NIST SP 800-38D — AES-GCM Specification
• Sanders (2017) — Practical Packet Analysis
• Python Docs — socket module
• Cryptography.io — AEAD Documentation
```

### 🎤 Narasi:
> "Demikian presentasi dari Kelompok 5. Terima kasih atas perhatiannya. Kami terbuka untuk pertanyaan dan masukan. Wassalamualaikum warahmatullahi wabarakatuh."

---

## RINGKASAN DURASI

| No | Bagian | Jenis | Soal | Durasi |
|----|--------|-------|------|--------|
| 1 | Judul & Anggota | Slide | Identitas | 0:30 |
| 2 | Latar Belakang | Slide | Pendahuluan | 0:40 |
| 3 | Klasifikasi Jaringan & LAN | Slide | Soal 1.1–1.2 | 0:45 |
| 4 | Topologi & Parameter | Slide | Soal 1.3–1.4 | 0:40 |
| 5 | OSI Layer & Diagram Alir | Slide | Soal 1.5–1.6 | 0:50 |
| 6 | Implementasi Tanpa Enkripsi | Slide | Soal 2.1–2.5 | 0:40 |
| 7 | **Demo 1: Tanpa Enkripsi + Wireshark** | **🎬** | **Soal 2+3** | **1:45** |
| 8 | Risiko & Solusi | Slide | Soal 3.5–3.6 | 0:40 |
| 9 | Konsep AES-GCM & Kunci | Slide | Soal 4.4–4.5 | 0:45 |
| 10 | Alur & Kode Enkripsi | Slide | Soal 4.1–4.3, 4.6 | 0:45 |
| 11 | **Demo 2: Dengan Enkripsi + Wireshark** | **🎬** | **Soal 4.7** | **2:00** |
| 12 | Evaluasi Komparatif | Slide | Soal 5.1–5.2 | 0:35 |
| 13 | Risiko Tersisa & Rekomendasi | Slide | Soal 5.3–5.4 | 0:45 |
| 14 | Jadwal & Pembagian Tugas | Slide | Soal 5.5 | 0:30 |
| 15 | Refleksi | Slide | Soal 5.6 | 0:35 |
| 16 | Kesimpulan | Slide | Kesimpulan | 0:35 |
| 17 | Penutup | Slide | — | 0:15 |
| | **TOTAL** | | **Soal 1–5 ✅** | **~13:15** |

> **Buffer tersisa: ~1 menit 45 detik** — untuk transisi antar slide, jeda natural, dan hal tak terduga.
> Total tetap di bawah 15 menit. ✅
> Seluruh poin soal 1–5 tercakup. ✅

---

## CHECKLIST KELENGKAPAN SOAL

### ✅ Soal 1: Analisis Kebutuhan & Perancangan
- [x] 1.1 Perbedaan PAN, LAN, MAN, WAN → **Slide 3**
- [x] 1.2 Alasan pemilihan LAN → **Slide 3**
- [x] 1.3 Diagram topologi → **Slide 4**
- [x] 1.4 IP, port, protokol, arah → **Slide 4**
- [x] 1.5 Pemetaan OSI Layer → **Slide 5**
- [x] 1.6 Diagram alir → **Slide 5**

### ✅ Soal 2: Implementasi Tanpa Enkripsi
- [x] 2.1–2.4 Server/client fungsional + info koneksi → **Slide 6 + Demo 1**
- [x] 2.5 Penjelasan fungsi bagian kode → **Slide 6**
- [x] 2.6 Risiko keamanan tanpa enkripsi → **Slide 6 + 7**

### ✅ Soal 3: Analisis Wireshark
- [x] 3.1 Tahapan pengambilan paket → **Demo 1**
- [x] 3.2 Filter Wireshark → **Demo 1**
- [x] 3.3 Tangkapan layar paket → **Demo 1 (live)**
- [x] 3.4 Keterbacaan pesan → **Demo 1**
- [x] 3.5 Min 3 risiko → **Slide 7 (5 risiko)**
- [x] 3.6 Solusi keamanan → **Slide 7**

### ✅ Soal 4: Implementasi AES-128
- [x] 4.1–4.3 Enkripsi/dekripsi fungsional → **Slide 9 + Demo 2**
- [x] 4.4 Plaintext, ciphertext, key, nonce → **Slide 8**
- [x] 4.5 Pengelolaan kunci → **Slide 8**
- [x] 4.6 Kunci tidak tampil terbuka → **Slide 9**
- [x] 4.7 Pengujian ulang + perbedaan → **Demo 2 + Slide 10**

### ✅ Soal 5: Evaluasi, Administrasi, Refleksi
- [x] 5.1 Tabel perbandingan → **Slide 10**
- [x] 5.2 Perubahan tingkat keamanan → **Slide 10**
- [x] 5.3 Risiko tersisa → **Slide 11**
- [x] 5.4 Min 4 rekomendasi → **Slide 11 (6 rekomendasi)**
- [x] 5.5 Jadwal & pembagian tugas → **Slide 12**
- [x] 5.6 Refleksi kelompok → **Slide 13**

---

## PEMBAGIAN PRESENTER (SARAN)

| Bagian | Slide/Demo | Presenter | Durasi |
|--------|------------|-----------|--------|
| Pembukaan, Latar Belakang, Perancangan | Slide 1–5 | Marsani | ~3:25 |
| Implementasi Tanpa Enkripsi + **Demo 1** | Slide 6 + Demo 1 | Muhammad Saifulloh | ~2:25 |
| Risiko + Konsep AES + Alur Kode | Slide 7–9 | Kristian & Sukandar | ~2:10 |
| **Demo 2** + Evaluasi + Rekomendasi | Demo 2 + Slide 10–11 | Sukandar | ~3:20 |
| Jadwal, Refleksi, Kesimpulan, Penutup | Slide 12–15 | Marsani / bersama | ~1:55 |

---

## TIPS PRESENTASI VIDEO (15 MENIT)

1. **Latihan timing** — Rekam latihan dulu, pastikan di bawah 15 menit.
2. **Demo yang lancar** — Siapkan terminal & Wireshark sebelum rekam. Pastikan program sudah siap jalan.
3. **Jangan membaca** — Narasi adalah panduan, bukan naskah. Bicara natural.
4. **Transisi singkat** — "Selanjutnya...", "Sekarang mari kita buktikan...", "Berikutnya..."
5. **Penekanan saat demo** — Beri jeda saat menunjukkan Wireshark agar penonton melihat perbedaannya.
6. **Backup demo** — Siapkan screenshot Wireshark sebagai cadangan jika demo gagal.
7. **Penutup tegas** — Kesimpulan → Terima kasih → Selesai. Jangan bertele-tele.
