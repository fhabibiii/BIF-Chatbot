# BIF Chatbot

BIF Chatbot adalah aplikasi berbasis web yang dirancang untuk membantu mahasiswa Universitas Telkom Bandung dalam mengakses informasi terkait layanan akademik. Proyek ini merupakan bagian dari Tugas Akhir oleh **Faqihuddin Habibi** dengan pembimbing utama **Dr. Arie Ardiyanti Suryani, S.T., M.T.**, dan dilisensikan di bawah **GNU GPL v3**.

## Deskripsi Proyek
Website ini dibangun menggunakan **Flask** untuk mengelola backend. Model yang digunakan adalah **IndoBERT**, yang telah saya fine-tune menggunakan dataset yang saya buat. IndoBERT adalah model pre-trained berbasis arsitektur transformer yang dirancang untuk bahasa Indonesia, seperti dijelaskan dalam penelitian oleh Koto et al. (2020) [1]. Sistem ini dirancang untuk memberikan jawaban yang relevan dan kontekstual berdasarkan pertanyaan pengguna terkait layanan akademik. Aplikasi ini telah dideploy dan dapat diakses melalui [http://bif-chatbot.my.id/](http://bif-chatbot.my.id/).

## Fitur Utama
1. **Chatbot Interaktif**: Menjawab pertanyaan pengguna terkait informasi akademik.
2. **Model Berbasis IndoBERT**: Memahami konteks bahasa Indonesia dengan lebih baik.
3. **Dukungan untuk Pertanyaan Kontekstual**: Menyediakan informasi akademik seperti jadwal kuliah, persyaratan yudisium, dan lainnya.
4. **Antarmuka Web yang Responsif**: Memudahkan pengguna untuk mengakses layanan dari berbagai perangkat.

## Teknologi yang Digunakan
1. **Flask**: Framework backend untuk mengelola logika server.
2. **IndoBERT**: Model pre-trained untuk pemrosesan bahasa alami (NLP) dalam bahasa Indonesia.
3. **HTML/CSS**: Untuk membangun antarmuka pengguna yang interaktif.
4. **Bootstrap**: Library CSS untuk desain responsif.
5. **PyTorch**: Library machine learning untuk mengintegrasikan model IndoBERT.

## Struktur Proyek
- `app.py`: File utama aplikasi yang mencakup backend Flask.
- `templates/`: Berisi file HTML untuk frontend.
- `static/`: Berisi aset statis seperti CSS dan gambar.
- `chatbot/`: Berisi model IndoBERT yang telah dilatih.
- `dataset/`: Berisi dataset yang digunakan.

## Cara Menjalankan Proyek
1. Clone repository ini:
   ```bash
   git clone https://github.com/fhabibiii/BIF-Chatbot.git
   ```
2. Masuk ke direktori proyek:
   ```bash
   cd BIF-Chatbot
   ```
3. Buat lingkungan virtual dan instal dependensi:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Untuk pengguna Linux/Mac
   venv\Scripts\activate   # Untuk pengguna Windows
   pip install -r requirements.txt
   ```
4. Jalankan server Flask:
   ```bash
   python app.py
   ```
5. Akses aplikasi di browser pada `http://localhost:5000`.

## Cara Menggunakan
1. Buka aplikasi pada browser.
2. Ketik pertanyaan terkait layanan akademik, seperti:
   - "Bagaimana cara mendaftar yudisium?"
   - "Apa syarat keringanan biaya kuliah?"
3. Chatbot akan memberikan jawaban yang relevan.

### Langkah-Langkah Fine-Tuning
1. **Persiapan Dataset**: Dataset di-split menjadi 75% data latih dan 25% data uji. Tokenisasi dilakukan menggunakan tokenizer IndoBERT.
2. **Pengaturan Hyperparameter dan Pelatihan Model**: Batch size 128 dan epoch 125 dipilih berdasarkan pengujian untuk hasil optimal.
4. **Evaluasi Model**: Performa model diukur menggunakan akurasi, precision, recall, dan F1-score. Akurasi pada data uji mencapai 97.78%.

### Evaluasi
Evaluasi menunjukkan bahwa model mampu menjawab pertanyaan kontekstual dengan baik. Namun, terdapat kesalahan pada pertanyaan ambigu karena ketidakkonsistenan pola dalam dataset. Untuk pengembangan lebih lanjut, disarankan memperkaya variasi pola dalam dataset.

## Kesimpulan
Chatbot berbasis IndoBERT berhasil memberikan jawaban relevan dan kontekstual. Konfigurasi batch size 128 dan epoch 125 terbukti optimal. Namun, pengembangan lebih lanjut pada dataset diperlukan untuk meningkatkan akurasi pada pertanyaan ambigu.

## Lisensi
Program ini dilisensikan di bawah [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html). Anda bebas untuk menggunakan, memodifikasi, dan mendistribusikan ulang program ini selama mengikuti ketentuan lisensi.

## Kontributor
- **Faqihuddin Habibi** - Mahasiswa Program Studi S1 Informatika, Universitas Telkom Bandung.
- **Pembimbing**: **Dr. Arie Ardiyanti Suryani, S.T., M.T.**

## Referensi
[1] Fajri Koto, Afshin, Rahimi, Jey Han Lau, and Timothy Baldwin. [IndoLEM and IndoBERT: A Benchmark Dataset and Pre-trained Language Model for Indonesian NLP](https://www.aclweb.org/anthology/2020.coling-main.66.pdf). In Proceedings of the 28th COLING, December 2020

---
Dibuat dengan ❤ oleh **Faqihuddin Habibi**
