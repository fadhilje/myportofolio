Nama : Nurfadhil Kurniawan
NPM  : 2506540765
Kelas : PBP E

UPDATE!!!

# Pertanyaan Relatif

## Tugas 1

### 1. Penggunaan Elemen Semantik HTML5
Saat merancang struktur HTML, saya memutuskan untuk menggunakan elemen semantik HTML5 seperti `<section>` , `<article>`, dan `<nav>`. Hal ini sangat membantu saya dalam mengorganisasi tata letak dibandingkan jika hanya menggunakan tag `<div>` secara berulang (div soup).

Saya menggunakan `<section>` untuk memisahkan area utama seperti bagian 'Tentang Saya', 'Education', 'Experience', dan 'Skills'. Sementara itu, untuk setiap kartu atau item proyek di dalam portofolio, saya membungkusnya dengan `<article>`. Pendekatan ini membuat kode saya jauh lebih rapi, mudah ditelusuri ketika ada bug, dan secara struktur lebih masuk akal untuk dibaca baik oleh developer lain maupun oleh mesin pencari (SEO friendly).

### 2. Tantangan CSS Responsive dan Tata Letak
Tantangan terbesar saat mengatur CSS agar responsive adalah menangani bagian grid atau flexbox pada daftar proyek. Di tampilan desktop, elemen bisa dengan mudah disejajarkan ke samping (misalnya 3 kolom). Namun, saat diakses dari mobile, elemen tersebut menjadi sangat sempit dan teksnya terpotong.

Untuk mengevaluasi posisi dan ukuran, saya menggunakan pendekatan mobile-first mindset. Saya memprioritaskan keterbacaan konten utama. Keputusan yang saya ambil saat menggunakan media queries untuk berpindah ke tampilan mobile meliputi:
a. Mengubah alur arah (flex-direction): Elemen yang tadinya berjejer ke samping (row) saya ubah menjadi bertumpuk ke bawah (column).
b. Hierarki visual: Saya memastikan gambar thumbnail proyek muncul lebih dulu di atas teks deskripsi agar pengguna langsung mendapatkan konteks visual saat men- scroll.
c. Penyesuaian ukuran: Padding dan margin yang besar di desktop saya kurangi, dan ukuran font judul (`<h1>`, `<h2>`) saya perkecil agar proporsional di layar HP.

### 3. Batasan Web Statis & Rencana Fungsionalitas Dinamis
Sejauh ini, karena website yang saya buat masih murni statis, hal yang baru bisa saya lakukan hanyalah menyajikan informasi dengan membaginya ke dalam beberapa section, seperti Education, Experience, dan Skills. Batasan yang paling saya rasakan adalah web ini terasa kurang hidup dan interaktif, ditambah lagi terbatasnya pemahaman saya saat ini tentang coding web yang lebih advanced.

Untuk iterasi proyek selanjutnya, jujur ada beberapa fitur dinamis yang pengen banget saya tambahkan:
a. Fitur Unduh CV: Saya ingin sekali menambahkan tombol interaktif yang memungkinkan pengunjung untuk langsung mendownload file CV saya.
b. Custom Cursor (Dot & Ring): Saya pengen banget bikin kursornya jadi unik (model titik dan lingkaran yang mengikuti gerakan mouse) supaya tampilan webnya jadi lebih estetik dan nggak membosankan.
c. Sayangnya, karena saya belum memahami betul cara membuatnya (terutama pengimplementasiannya yang mungkin butuh JavaScript), kedua fitur tersebut belum bisa saya masukkan di tugas kali ini. Ini bakal jadi target utama saya untuk dipelajari dan ditambahkan ke depannya!

## Tugas 2

## 1. Alur saat user buka halaman portofolio baru

Jadi ceritanya gini: waktu user ngetik URL atau klik link menuju halaman portofolio, request itu pertama kali nyampe ke `urls.py` level proyek (yang di folder project utama). File ini kayak resepsionis, tugasnya cuma ngecek awalan URL terus lempar ke `urls.py` punya aplikasi yang sesuai pakai `include()`. Nah dari situ, `urls.py` aplikasi bakal cocokin path yang lebih spesifik dan nentuin view mana yang harus dipanggil.

Setelah nyampe di view, di situlah logikanya jalan — view bakal query data portofolio dari model (misal manggil `Portofolio.objects.all()` atau `.filter()` kalau butuh yang spesifik). Model ini yang megang tanggung jawab buat komunikasi ke database, jadi view nggak perlu tau gimana caranya data diambil, cukup minta lewat ORM Django.

Data yang udah didapat dari model itu terus dikirim ke template pakai context (bentuknya dictionary). Template nanti yang ngerender data itu jadi HTML, biasanya pake tag `{{ }}` atau `{% for %}` kalau datanya banyak. Baru deh HTML hasil render ini yang dikirim balik sebagai response ke browser, dan user bisa liat halaman portofolionya.

Intinya: request → urls.py proyek → urls.py app → view → model (ambil data) → template (render tampilan) → response ke browser.

## 2. Kenapa data portofolio baru sebaiknya di model, bukan hardcode di template

Kalau datanya ditulis langsung di template, tiap kali ada portofolio baru yang mau ditambahin, kita harus buka file HTML-nya terus edit manual satu-satu. Itu ribet banget apalagi kalau datanya udah puluhan atau ratusan, dan gampang banget salah ketik atau kelewat update di satu tempat.

Dengan naruh data di model, kita cuma perlu nambahin row baru di database (bisa lewat admin panel Django atau form), terus otomatis muncul di halaman tanpa perlu nyentuh kode template sama sekali. Ini bikin aplikasi jauh lebih gampang di-maintain karena logic tampilan (template) dan data (model) jadi kepisah rapi, kalau mau ubah tampilan, cukup edit template; kalau mau ubah/tambah data, cukup di model/database. Konsepnya mirip separation of concern yang emang jadi dasar arsitektur MVT di Django.

## 3. Perbedaan `makemigrations` dan `migrate`

`makemigrations` itu fungsinya buat "nyatet" perubahan yang kita bikin di model, dia bakal bikin file migration baru yang isinya semacam instruksi perubahan struktur tabel, tapi belum benar-benar dieksekusi ke database. Sedangkan `migrate` itu yang benar-benar nerapin instruksi dari file migration tadi ke database, jadi struktur tabelnya beneran berubah.

Contohnya, misal awalnya di model `Portofolio` cuma ada field `judul` dan `deskripsi`, terus aku nambahin field baru `tanggal_dibuat = models.DateField()`. Setelah nambahin field itu di model, aku harus jalanin `python manage.py makemigrations` dulu supaya Django bikin file migration yang nyatet ada kolom baru `tanggal_dibuat`. Habis itu baru jalanin `python manage.py migrate` supaya kolom itu beneran ditambahin ke tabel di database. Kalau cuma `makemigrations` doang tanpa `migrate`, perubahannya belum keapply ke database beneran.

## Deklarasi AI

Dalam proses pengerjaan proyek ini, saya sempat mengalami error saat melakukan redeploy setelah menambahkan satu halaman/fitur baru pada aplikasi. Untuk membantu mendiagnosis dan menyelesaikan error tersebut, saya meminta bantuan AI Claude untuk membantu menelusuri penyebab error dan memberikan saran perbaikan. Penggunaan AI di sini terbatas pada proses debugging error deployment, sementara pemahaman konsep dan implementasi utama tetap saya kerjakan sendiri.