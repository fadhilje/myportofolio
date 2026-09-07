Nama : Nurfadhil Kurniawan
NPM  : 2506540765
Kelas : PBP E

UPDATE!!!

## Pertanyaan Relatif

### 1. Penggunaan Elemen Semantik HTML5
Saat merancang struktur HTML, saya memutuskan untuk menggunakan elemen semantik HTML5 seperti '<section>' , '<article>', dan <nav>. Hal ini sangat membantu saya dalam mengorganisasi tata letak dibandingkan jika hanya menggunakan tag '<div>' secara berulang (div soup).

Saya menggunakan '<section>' untuk memisahkan area utama seperti bagian 'Tentang Saya', 'Education', 'Experience', dan 'Skills'. Sementara itu, untuk setiap kartu atau item proyek di dalam portofolio, saya membungkusnya dengan '<article>'. Pendekatan ini membuat kode saya jauh lebih rapi, mudah ditelusuri ketika ada bug, dan secara struktur lebih masuk akal untuk dibaca baik oleh developer lain maupun oleh mesin pencari (SEO friendly).

### 2. Tantangan CSS Responsive dan Tata Letak
Tantangan terbesar saat mengatur CSS agar responsive adalah menangani bagian grid atau flexbox pada daftar proyek. Di tampilan desktop, elemen bisa dengan mudah disejajarkan ke samping (misalnya 3 kolom). Namun, saat diakses dari mobile, elemen tersebut menjadi sangat sempit dan teksnya terpotong.

Untuk mengevaluasi posisi dan ukuran, saya menggunakan pendekatan mobile-first mindset. Saya memprioritaskan keterbacaan konten utama. Keputusan yang saya ambil saat menggunakan media queries untuk berpindah ke tampilan mobile meliputi:
a. Mengubah alur arah (flex-direction): Elemen yang tadinya berjejer ke samping (row) saya ubah menjadi bertumpuk ke bawah (column).
b. Hierarki visual: Saya memastikan gambar thumbnail proyek muncul lebih dulu di atas teks deskripsi agar pengguna langsung mendapatkan konteks visual saat men- scroll.
c. Penyesuaian ukuran: Padding dan margin yang besar di desktop saya kurangi, dan ukuran font judul ('<h1>', '<h2>') saya perkecil agar proporsional di layar HP.

### 3. Batasan Web Statis & Rencana Fungsionalitas Dinamis
Sejauh ini, karena website yang saya buat masih murni statis, hal yang baru bisa saya lakukan hanyalah menyajikan informasi dengan membaginya ke dalam beberapa section, seperti Education, Experience, dan Skills. Batasan yang paling saya rasakan adalah web ini terasa kurang hidup dan interaktif, ditambah lagi terbatasnya pemahaman saya saat ini tentang coding web yang lebih advanced.

Untuk iterasi proyek selanjutnya, jujur ada beberapa fitur dinamis yang pengen banget saya tambahkan:
a. Fitur Unduh CV: Saya ingin sekali menambahkan tombol interaktif yang memungkinkan pengunjung untuk langsung mendownload file CV saya.
b. Custom Cursor (Dot & Ring): Saya pengen banget bikin kursornya jadi unik (model titik dan lingkaran yang mengikuti gerakan mouse) supaya tampilan webnya jadi lebih estetik dan nggak membosankan.
c. Sayangnya, karena saya belum memahami betul cara membuatnya (terutama pengimplementasiannya yang mungkin butuh JavaScript), kedua fitur tersebut belum bisa saya masukkan di tugas kali ini. Ini bakal jadi target utama saya untuk dipelajari dan ditambahkan ke depannya!