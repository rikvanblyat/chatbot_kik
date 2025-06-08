# 📦 Changelog – Chatbot KIK PTJ 2025
Semua perubahan penting projek ini direkodkan dalam fail ini.
Versi mengikut format: major.minor.patch-build

---

## [1.0.0-RC1] – 2025-04-15
### ✅ Calon Versi Akhir (Release Candidate)
- Integrasi penuh antara modul FAQ dan carian dokumen (PDF, DOCX, XLSX).
- Satu kotak input disediakan untuk semua pertanyaan; mengutamakan carian dalam FAQ, kemudian dokumen.
- Penambahbaikan paparan jawapan kepada format berstruktur (Isi – Huraian – Contoh).
- Tema visual direka semula menggunakan palet warna korporat (emerald green) dan kesan visual animasi cursor.
- Ujian pelbagai pelayar selesai; aplikasi stabil dan bersedia untuk pembentangan.

---

## [0.2.3] – 2024-12-15
### 🎨 Penambahbaikan Antara Muka (Responsif)
- Penyesuaian reka bentuk untuk paparan pada skrin tablet dan komputer riba.
- Penetapan semula nilai saiz fon, margin, dan susun atur supaya lebih kemas.
- Pembetulan isu teks melebihi ruang apabila jawapan terlalu panjang.

---

## [0.2.2] – 2024-11-05
### 🧠 Penambahbaikan Gaya Jawapan & Fallback
- Paparan jawapan kini menggunakan ayat penuh yang lebih natural dan mudah difahami.
- Muktamadkan mesej fallback: “Sila hubungi Pegawai JANM untuk maklumat lanjut.”
- Semakan semula struktur output untuk menyeragamkan gaya jawapan.

---

## [0.2.1] – 2024-10-20
### 🔁 Penggabungan Input & Pembetulan Parser
- Fungsi carian FAQ dan dokumen digabungkan ke dalam satu input.
- Pembetulan pada modul parser Excel yang mengalami ralat apabila membaca helaian berganda.
- Pengujian terhadap kesesuaian fallback yang lebih fleksibel dan tersusun.

---

## [0.2.0] – 2024-10-05
### 📁 Sokongan Carian Pelbagai Fail
- Tambahan fungsi carian merentas fail PDF, DOCX, dan XLSX.
- Logik fallback dimasukkan bagi memastikan aplikasi sentiasa memberikan maklum balas kepada pengguna.
- Penambahbaikan awal terhadap reka bentuk visual dan keperluan reka letak.

---

## [0.1.5] – 2024-09-10
### 📄 Format Jawapan Berstruktur & Kesan Visual
- Jawapan dipaparkan dalam format berstruktur: Isi – Huraian – Contoh.
- Penambahan animasi cursor berkedip pada ruangan input sebagai penambah elemen visual.
- Pembetulan susunan elemen teks yang tidak selaras dalam versi sebelumnya.

---

## [0.1.4] – 2024-08-20
### 🔍 Padanan Kata Kunci Fleksibel & Mesej Asas
- Tambahan logik padanan separa (fuzzy matching) menggunakan regular expressions.
- Pengenalan awal sistem fallback jika tiada padanan ditemui.
- Isu padanan berlebihan dikesan; akan diperhalusi dalam versi akan datang.

---

## [0.1.3] – 2024-08-05
### 📄 Carian Fail PDF – Padanan Tepat
- Integrasi modul PyPDF2 untuk pembacaan dan carian teks dalam fail PDF.
- Penggunaan padanan kata kunci asas (case-insensitive).
- Pembetulan isu pengekodan aksara (encoding) untuk fail PDF tertentu.

---

## [0.1.2] – 2024-07-15
### 📋 Pembangunan Asas FAQ Engine
- Fail `faq.json` dibina untuk menyimpan soalan lazim dan jawapan dalam format struktur JSON.
- Integrasi ke dalam Streamlit untuk membolehkan paparan automatik jawapan.
- Pengendalian isu pengekodan aksara UTF-8 semasa memuatkan fail teks.

---

## [0.1.1] – 2024-07-01
### 🚀 Komit Permulaan (Initial Commit)
- Penetapan struktur asas projek: `app.py`, `faq.json`, `dokumen/`.
- Penentuan skop fungsi: enjin soal jawab, carian pekeliling, dan antara muka mesra pengguna.
- Semua konfigurasi awal dijalankan dalam persekitaran pembangunan setempat.
