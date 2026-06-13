# Ujian Tengah Semester
- Mata Kuliah: Network Programming & Administration
- Kelas: IFN41 
- Prodi: Informatika PJJ S1
- Kampus: UNIVERSITAS SIBER ASIA    
- Dosen: Abdul Azzam Ajhari, S.Kom., M.Kom.
- Kelompok 5: 
    - Marsani (230401010282)
    - Muhammad Saifulloh (220401010207)
    - Kristian Hananiel Hura (220401010289)
    - Sukandar (240401020175)

### Deskripsi Tugas

Bagaimana merancang aplikasi komunikasi client–server berbasis Python yang dapat digunakan pada jaringan LAN serta mampu mengurangi risiko keterbacaan pesan ketika lalu lintas jaringan dianalisis menggunakan Wireshark? 

Sebuah unit administrasi akademik ingin mengirimkan pesan singkat melalui jaringan LAN, misalnya informasi jadwal rapat, kode verifikasi internal, atau status layanan. Aplikasi awal menggunakan komunikasi client–server biasa sehingga isi pesan berpotensi terbaca ketika lalu lintas jaringan dianalisis menggunakan Wireshark.

Kelompok diminta membuat dua versi aplikasi (sederhana - hanya untuk menjelaskan konsep), fiturnya ada di soal dibawah: 
1. Versi awal: komunikasi client–server tanpa enkripsi
2. Versi perbaikan: komunikasi client–server dengan implementasi AES-128. 

### Soal 1:  Analisis Kebutuhan dan Perancangan Jaringan
Jelaskan rancangan komunikasi jaringan yang akan dibuat oleh kelompok Anda. 

Jawaban wajib memuat: 
1. Perbedaan PAN, LAN, MAN, dan WAN secara ringkas.  
2. Alasan pemilihan LAN sebagai lingkungan implementasi proyek.  
3. Diagram topologi yang menunjukkan minimal satu komputer server dan satu komputer client.  
4. Alamat IP, port, protokol transportasi, serta arah komunikasi data.  
5. Pemetaan proses komunikasi terhadap model OSI Layer.  
6. Diagram alir proses pengiriman dan penerimaan pesan.  

**Bukti yang dilampirkan**: diagram topologi dan flowchart

### Soal 2: Implementasi Program Client–Server Tanpa Enkripsi
Buat aplikasi komunikasi jaringan sederhana menggunakan Python dengan ketentuan:
1. Server dapat menerima koneksi dari client melalui jaringan LAN.  
2. Client dapat mengirimkan pesan teks kepada server.  
3. Server menampilkan pesan yang diterima.  
4. Program menampilkan informasi koneksi, seperti alamat IP client, port, dan waktu penerimaan pesan.  
5. Kelompok menjelaskan fungsi bagian-bagian utama kode program.    

Pada laporan, jelaskan mengapa pesan yang dikirimkan tanpa perlindungan kriptografi memiliki risiko keamanan. 
**Bukti yang dilampirkan**: source code, tangkapan layar program (akan diambil secara manual ketika program dijalankan), dan hasil pengujian.

### Soal 3: Analisis Kerentanan Menggunakan Wireshark
Lakukan analisis lalu lintas jaringan terhadap aplikasi pada Soal 2 menggunakan Wireshark. 

Jawaban wajib memuat:
 1. Tahapan pengambilan paket komunikasi.  
 2. Filter Wireshark yang digunakan, misalnya berdasarkan alamat IP atau nomor port.  
 3. Minimal tiga tangkapan layar paket yang relevan.  
 4. Penjelasan apakah isi pesan masih dapat terbaca.  
 5. Identifikasi minimal tiga risiko, misalnya:  
    - Penyadapan pesan;  
    - Kebocoran informasi;  
    - Manipulasi pesan;  
    - Impersonasi client;  
    - Replay terhadap pesan yang pernah dikirimkan.  
 6. Penjelasan solusi keamanan yang diperlukan.  

 **Bukti yang dilampirkan**: file .pcapng, tangkapan layar Wireshark, dan analisis uraian.

### Soal 4: Implementasi Komunikasi Aman Menggunakan AES-128 
Perbaiki aplikasi sebelumnya dengan mengimplementasikan kriptografi AES-128 pada pesan yang dikirimkan. 

Ketentuan minimal: 
1. Pesan dienkripsi pada sisi client sebelum dikirimkan.  
2. Server menerima ciphertext dan melakukan dekripsi.  
3. Pesan asli hanya ditampilkan setelah proses dekripsi berhasil.  
4. Kelompok menjelaskan perbedaan plaintext, ciphertext, key, dan nonce atau initialization vector.  
5. Kelompok menjelaskan pengelolaan kunci yang digunakan dalam proyek.  
6. Kunci tidak ditampilkan secara terbuka dalam video.  
7. Lakukan pengujian ulang menggunakan Wireshark dan jelaskan perbedaannya dengan hasil pada Soal 3.

Untuk implementasi yang lebih baik, gunakan authenticated encryption, misalnya AES-128-GCM. Apabila menggunakan mode AES lain, jelaskan  mekanisme perlindungan integritas pesannya. 

**Bukti  yang  dilampirkan**:  source code versi aman, tangkapan layar hasil eksekusi, dan file .pcapng setelah enkripsi. 

### Soal 5: Evaluasi, Administrasi, dan Refleksi Proyek
Susun evaluasi komparatif terhadap kedua versi aplikasi. 

Jawaban wajib memuat: 
1. Tabel perbandingan aplikasi sebelum dan sesudah implementasi AES-128.  
2. Penjelasan perubahan tingkat keamanan berdasarkan bukti Wireshark.  
3. Penjelasan risiko yang masih tersisa setelah enkripsi diterapkan.  
4. Minimal empat rekomendasi administrasi keamanan jaringan, misalnya:  
    - pembatasan akses perangkat;
    - pengelolaan kunci;
    - pencatatan log;  
    - validasi client;  
    - pemantauan koneksi;  
    - pembaruan library.
5. Jadwal pengerjaan proyek dan pembagian tugas setiap anggota.  
6. Refleksi kelompok: kendala utama, solusi yang dilakukan, dan peningkatan yang dapat diterapkan.  

**Bukti yang dilampirkan**: tabel komparasi, jadwal proyek, pembagian peran, dan refleksi.

### Sistematika Laporan 
1. Identitas kelompok dan kontribusi anggota.  
2. Pendahuluan dan permasalahan.  
3. Jawaban Soal 1–5.  
4. Source code utama beserta penjelasan.  
5. Bukti pengujian Wireshark sebelum dan sesudah enkripsi.  
6. Kesimpulan dan refleksi.

