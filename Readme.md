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

## Tugas 3
 
### 1. Kenapa pakai `ModelForm` dan kenapa wajib `{% csrf_token %}`
 
Kalau bikin form HTML secara manual, aku harus nulis ulang semua field satu-satu di template, terus nulis sendiri validasinya di view (misal cek judul nggak kosong, cek panjang maksimal, cek format URL valid). Padahal semua aturan itu udah aku definisin di model. Nah `ModelForm` itu langsung "baca" model-nya, jadi field, tipe input, dan validasinya otomatis ngikutin model (contohnya `max_length=255` di `title` atau `URLField` di `project_url`). Jadi aku nggak perlu nulis hal yang sama dua kali (prinsip DRY), dan kalau nanti model berubah, form-nya ikut menyesuaikan tanpa harus diedit manual, jadi kecil kemungkinan form dan model nggak sinkron.
 
Selain itu, `ModelForm` juga ngasih `form.is_valid()` buat validasi sekaligus ngumpulin pesan error per field, `form.save()` buat langsung nyimpen ke database, dan parameter `instance=` supaya form yang sama bisa dipakai buat edit data yang udah ada. Di project ini, `ExperienceForm` dan `ProjectForm` dipakai buat halaman tambah dan edit sekaligus, jadi satu form cukup buat dua fungsi.
 
Untuk `{% csrf_token %}`, ini dipakai buat ngelindungin dari serangan CSRF (Cross-Site Request Forgery). Bayangin user lagi login di website kita, terus dia buka website jahat. Website jahat itu bisa diam-diam bikin browser user ngirim request POST ke website kita (misalnya buat hapus data), dan browser otomatis nyertain cookie session user, jadi server ngira itu request yang sah. Dengan `{% csrf_token %}`, Django nyelipin token acak yang unik ke dalam form, dan pas form di-submit, `CsrfViewMiddleware` ngecek token itu cocok atau nggak. Website jahat nggak tau token-nya, jadi request palsunya ditolak dengan error 403. Makanya form yang method-nya POST wajib ada token ini, kalau nggak ada Django bakal nolak request-nya.
 
### 2. Kenapa JSON lebih disukai dibanding XML
 
Format XML itu verbose karena setiap data harus dibungkus tag pembuka dan penutup, jadi ukurannya lebih gede dan lebih susah dibaca. JSON lebih ringkas karena cuma pakai pasangan `key: value`, jadi datanya lebih kecil, lebih cepat dikirim lewat jaringan, dan lebih gampang dibaca manusia.
 
Alasan lain, JSON itu struktur aslinya udah mirip object di JavaScript, jadi di sisi frontend bisa langsung diubah pakai `JSON.parse()` atau `response.json()` pada `fetch`, tanpa perlu parser XML yang lebih ribet buat menelusuri tree-nya. JSON juga punya tipe data dasar yang jelas (string, number, boolean, null, array, object), sedangkan di XML semuanya pada dasarnya teks. Di sisi lain, XML masih punya kelebihan seperti dukungan schema, namespace, dan atribut, makanya masih dipakai di sistem lama atau enterprise. Tapi buat pengembangan web modern yang butuh pertukaran data cepat dan sederhana antara server dan browser (REST API), JSON jadi pilihan utama.
 
### 3. Alur view mengembalikan data JSON dan kenapa perlu serialization
 
Ambil contoh `get_experience_json` di project ini. Alurnya:
 
1. Browser (atau client lain) ngirim request `GET /api/experience/`.
2. Django cocokin URL-nya di `urls.py` proyek, diteruskan ke `urls.py` app `main`, lalu ketemu path `api/experience/` yang manggil view `get_experience_json`.
3. Di dalam view, data diambil dari database lewat model: `Experience.objects.all()`. Hasilnya berupa `QuerySet`.
4. `QuerySet` itu diubah jadi string JSON pakai `serializers.serialize("json", experiences)`.
5. String JSON tadi dibungkus `HttpResponse(..., content_type="application/json")`, lalu dikirim balik ke client sebagai response.
Proses serialization diperlukan karena `QuerySet` dan object model itu cuma object Python yang hidup di memori server, sedangkan HTTP cuma bisa ngirim teks atau bytes. Jadi datanya harus diterjemahin dulu ke format yang bisa ditransfer dan dimengerti client lain, yaitu JSON. Selain itu, tipe data di model nggak selalu langsung bisa jadi JSON, contohnya `UUIDField` dan `DateTimeField` di model `Experience`, jadi serializer Django yang ngurusin konversinya. Hasilnya berupa struktur berisi `model`, `pk`, dan `fields` untuk tiap data. Dengan begini, data portofolio bisa dipakai oleh JavaScript, aplikasi mobile, atau layanan lain, nggak cuma template HTML Django.

## Deklarasi AI
Pada Tugas 3, saya meminta bantuan AI Claude untuk men-debug error yang muncul saat proses **create, update, dan delete** (Experience dan Project). Gejalanya: saat menambah data, form malah mengirim request ke URL update dengan UUID acak sehingga muncul halaman 404 (`No Experience matches the given query` / `No Project matches the given query`), serta notifikasi berhasil/gagal (termasuk pesan secret key salah) tidak tampil sesuai yang saya harapkan. Dari hasil debugging tersebut, penyebabnya adalah pengecekan `{% if form.instance.pk %}` di template form yang selalu bernilai true, karena primary key model memakai `UUIDField(default=uuid.uuid4)` sehingga instance baru pun sudah punya `pk`. Perbaikannya memakai flag `is_edit` dari view, serta menampilkan `messages` di `base.html`.

Prompt yang saya gunakan, "Saya mengalami kendala berupa error seperti pada gambar (Page not found 404, `No Experience matches the given query` saat POST ke `/experience/<uuid>/update/`). Berikut seluruh file proyek saya. Kira-kira untuk error ini, di bagian mana saya membuat kesalahannya?"


## Tugas 4

### Username Pengunjung biasa dan Editor
| Username | Password | Status |
| --- | --- | --- |
| kalel | zor_el1229 | editor |
| avengers | assemble | pengunjung biasa |

### Deskripsi Setup

**1. Akses editor untuk Experience**

Pada tugas ini saya memilih memberikan akses **edit Experience** kepada editor. Alasannya, menambah dan menghapus Experience adalah keputusan yang mengubah struktur riwayat portofolio, jadi saya biarkan hanya admin (superuser) yang bisa melakukannya. Editor cukup bisa memperbaiki data yang sudah ada, misalnya merevisi deskripsi atau tanggal.

Pembagian aksesnya:

| Aksi | Pengunjung biasa | Editor | Admin |
| --- | --- | --- | --- |
| Lihat Experience / Project | ✅ | ✅ | ✅ |
| Edit Experience | ❌ | ✅ | ✅ |
| Tambah / Hapus Experience | ❌ | ❌ | ✅ |
| Tambah / Edit Project | ❌ | ✅ | ✅ |
| Hapus Project | ❌ | ❌ | ✅ |

Editor dibuat dengan membuat group **Editor** di Django admin (*Authentication and Authorization > Groups*), lalu memberi permission `main | experience | Can change experience`, `main | project | Can add project`, dan `main | project | Can change project`. Setelah itu user `kalel` dimasukkan ke group tersebut lewat halaman edit user. Di sisi view, akses dijaga dengan `@login_required` dan `@permission_required(..., raise_exception=True)`, sedangkan di template tombol hanya muncul jika `perms.main.change_experience` (dan sejenisnya) bernilai true. Setiap perubahan tetap memerlukan secret key.

**2. Fitur filter "Favorit saya" pada Project**

Fitur tambahan yang saya pilih adalah filter **★ Favorit saya** di halaman Project. Saya memilih fitur ini karena setiap project sudah punya tombol star (relasi `starred_by` ke user), sehingga pengguna yang login bisa langsung menyaring project yang pernah mereka star.

Cara kerjanya:
- Checkbox "Favorit saya" ditambahkan di dalam form pencarian, hanya tampil untuk user yang sudah login, dan otomatis submit saat dicentang (`?starred=1`).
- `get_projects_json` memfilter dengan `projects.filter(starred_by=request.user)` bila `starred=1` dan user terautentikasi. Filter ini bisa dikombinasikan dengan pencarian judul.
- Pesan pada kondisi kosong dibedakan: "Belum ada proyek yang kamu star" untuk filter favorit, "Tidak ada proyek dengan nama tersebut" untuk pencarian judul.
- Pada `toggle_star`, redirect memakai `HTTP_REFERER` yang divalidasi dengan `url_has_allowed_host_and_scheme`, sehingga setelah star/unstar pengguna kembali ke halaman dengan filter yang sama dan tidak terjadi open redirect. Jika referer tidak valid, fallback ke `main:show_projects`.

## Deklarasi AI

Pada Tugas 4, saya menggunakan AI Claude untuk membantu proses menambahkan user yang terdaftar di web saya sebagai editor, yaitu memasukkan user tersebut ke group dan permission Django.

Prompt yang saya gunakan: "saya memiliki tugas untuk menambah kan user yg terdaftar di web saya sebagai editor dengan memasukkan editor tersebut ke group permission, bantu saya untuk melakukan hal tersebut"


## Tugas 5

### 1. **Apa itu *debouncing* dan kenapa penting di pencarian AJAX**
*Debouncing* adalah teknik menunda eksekusi sebuah fungsi sampai pemicunya berhenti selama waktu tertentu. Setiap kali event baru muncul, timer yang lama dibatalkan dan dimulai lagi dari awal, jadi fungsinya cuma jalan sekali setelah jeda. Di project ini, event `input` pada kolom cari memakai `clearTimeout` lalu `setTimeout` dengan jeda 300 ms, jadi `fetch()` baru dikirim setelah pengguna berhenti mengetik.

Tanpa debouncing, setiap karakter yang diketik langsung jadi satu request. Mengetik "backend" saja sudah menghasilkan 7 request, padahal cuma hasil terakhir yang dibutuhkan. Dampaknya:
   - Beban server dan database naik tanpa perlu, karena tiap request menjalankan query `icontains`.
   - Bandwidth terbuang dan UI bisa berkedip karena daftar dirender ulang berkali-kali.
   - Ada risiko *race condition*. Response request lama bisa saja tiba setelah response request baru, sehingga hasil pencarian yang sudah usang menimpa hasil yang benar.
   
Selain debouncing, aku juga memakai `AbortController` untuk membatalkan request sebelumnya yang belum selesai, jadi hasil yang tampil selalu berasal dari pencarian paling baru.

### 2. **Fungsi `await` pada `fetch()` dan apa yang terjadi kalau tidak dipakai**
`fetch()` itu asinkron dan tidak langsung mengembalikan data, tapi sebuah `Promise` yang menjanjikan `Response` di masa depan. Kata kunci `await` (di dalam fungsi `async`) menjeda jalannya fungsi itu sampai Promise-nya selesai, lalu mengembalikan nilai `Response`-nya. Halaman tetap tidak membeku karena yang berhenti sementara hanya fungsi tersebut, bukan seluruh browser. Hal yang sama berlaku untuk `response.json()` yang juga mengembalikan Promise.

Kalau `await` tidak dipakai, variabel `response` isinya masih Promise yang berstatus *pending*, bukan `Response`. Akibatnya:
   - `response.ok` bernilai `undefined` dan `response.json()` memicu `TypeError`, karena Promise tidak punya method itu.
   - Baris di bawahnya langsung jalan sebelum data dari server datang, jadi daftar bisa kosong atau tidak pernah dirender.
   - Error jaringan tidak tertangkap oleh `try/catch`, karena penolakan Promise terjadi setelah blok `try` selesai. Pesan error di UI pun tidak muncul.

Alternatifnya adalah rantai `.then()`, tapi `async/await` lebih mudah dibaca dan penanganan errornya bisa dengan `try/catch` biasa.

### 3. **Apa itu serangan XSS dan kenapa data via AJAX/JavaScript lebih rentan dibanding template Django**
*Cross-Site Scripting* (XSS) adalah serangan di mana penyerang menyisipkan kode berbahaya (biasanya JavaScript) ke dalam data yang nanti ditampilkan di halaman, sehingga kode itu dijalankan di browser pengunjung lain dengan hak akses origin website kita. Contoh *stored XSS*: penyerang mengisi judul dengan `<img src=x onerror="...">`. Kalau data itu dirender mentah, setiap orang yang membuka halaman akan menjalankan skrip tersebut. Dampaknya bisa berupa pengiriman request atas nama korban yang sedang login, pembacaan token atau data di halaman, pengubahan tampilan, sampai pengalihan ke situs palsu.

Template Django aman secara bawaan karena `{{ variable }}` otomatis di-*escape*, jadi `<` menjadi `&lt;` dan ditampilkan sebagai teks biasa. Pada AJAX, alurnya beda. Server mengirim JSON yang berisi teks apa adanya, lalu JavaScript yang membangun HTML sendiri, misalnya lewat template literal yang dimasukkan ke `innerHTML`. Di sini tidak ada *auto-escape*, jadi kalau nilai dari JSON langsung disisipkan, string `<img onerror=...>` akan diperlakukan browser sebagai HTML sungguhan dan dieksekusi. Escape juga harus ditulis manual untuk setiap field, jadi satu field yang terlewat saja sudah cukup jadi celah.

Karena itu di project ini aku memakai pertahanan berlapis:
   - **Sisi client:** semua nilai teks yang disisipkan ke HTML lewat JavaScript di-*escape* dengan fungsi `escapeHtml()`, atau memakai `textContent` untuk teks biasa.
   - **Sisi server:** input dibersihkan dengan `strip_tags` di method `clean_title` dan `clean_description` pada `ExperienceForm`, jadi tag HTML tidak ikut tersimpan ke database

## Penjelasan Setup Tugas 5

**1. Implementasi Asinkronus Data Experience & Pencarian (Fetch API & Debouncing)**
Pada tugas ini, halaman daftar Experience diubah menjadi berbasis AJAX/asinkronus untuk meningkatkan user experience agar pengolahan data berjalan tanpa me-reload seluruh halaman.
    **Cara kerjanya:**
    - Render Kerangka: View show_experience hanya bertugas merender kerangka HTML utama *(experience.html)*.
    - Fetch Data JSON: JavaScript memanggil endpoint API `get_experience_json` menggunakan `fetch()`. Endpoint ini mengambil data dari database, memfilter berdasarkan parameter query title jika ada pencarian, lalu menyusun serta mengembalikan respons array JSON secara manual menggunakan JsonResponse.
    - Manajemen State: Pada *experience.html*, status tampilan (loading, error, empty, dan grid) dikontrol secara dinamis dengan menyembunyikan atau menampilkan elemen DOM terkait menggunakan kelas CSS. Digunakan pula AbortController untuk membatalkan request Fetch sebelumnya jika ada permintaan baru yang dikirim berurutan.   
    - Pencarian dengan Debouncing: Input pencarian dilengkapi event listener input yang menerapkan *fungsi debouncing (300 ms)* menggunakan `setTimeout` dan `clearTimeout`. Hal ini memastikan request AJAX baru dikirim setelah pengguna berhenti mengetik, sehingga menghemat beban lalu lintas jaringan ke server.

**2. Penambahan Data Asinkronus via Modal Form & Kontrol Akses Backend**
Fitur penambahan Experience dibuat berbasis modal dan AJAX agar pengguna (admin) tidak perlu berpindah ke halaman terpisah saat menambahkan data baru.
    **Cara kerjanya:**
    - Modal Native: Form penambahan diletakkan dalam modal *(experience_form_modal.html)* memanfaatkan HTML Popover API `(popover="auto")`.
    - Pengiriman AJAX & CSRF: Event pengiriman form ditangani oleh JavaScript `(addExperience)`. Pengiriman data dilakukan menggunakan `FormData` via metode `POST` dengan menyertakan token CSRF pada header X-CSRFToken yang diambil dari cookie `csrftoken`.
    - Pemeriksaan Hak Akses di View: Di sisi backend, view create_experience_ajax memeriksa autentikasi dan peran pengguna secara ketat `(is_superuser dan has_perm("main.add_experience"))`. View ini tidak mengembalikan HTML/redirect, melainkan respon JSON dengan kode status HTTP yang sesuai: 201 untuk sukses, 400 untuk kesalahan validasi form, dan 403 jika pengguna tidak memiliki hak akses.
    - Pembaruan Otomatis: Setelah data berhasil disimpan di server, modal ditutup, isi form di-reset, dan daftar Experience langsung diperbarui secara otomatis melalui pemanggilan ulang fungsi `fetchExperiences()` tanpa reload halaman.\

**3. Sistem Notifikasi Toast & Perlindungan Keamanan (XSS & CSRF)**
Untuk memberikan feedback langsung kepada pengguna serta menjaga keamanan aplikasi dari serangan Cross-Site Scripting (XSS), diterapkan sistem notifikasi toast dan sanitasi data ganda.
    **Cara kerjanya:**
    - Komponen Toast: Dibuat komponen terpisah *(toast.html & toast.js)* yang memanfaatkan Popover API `(popover="manual")`. Fungsi `showToast(title, message, type, duration)` mengatur warna/tipe toast `(toast-success, toast-error, toast-normal)`, animasi kemunculan, serta timer otomatis untuk menyembunyikannya kembali. Jika validasi backend gagal, pesan kesalahan dari result.errors di-extract dan ditampilkan ke dalam toast error.
    - Sanitasi Sisi Client (Front-end XSS Protection): Semua nilai teks dinamis dari server disaring menggunakan fungsi `escapeHtml()` sebelum disisipkan ke dalam struktur HTML. Selain itu, pengisian teks judul dan pesan pada toast menggunakan properti .`textConten`t` untuk memastikan input dirender sebagai string murni, bukan elemen HTML yang dapat dieksekusi.
    - Sanitasi Sisi Server (Back-end XSS Protection): Pada *forms.py*, kelas `ExperienceForm` mengimplementasikan method `clean_title()` dan `clean_description()` yang memanfaatkan fungsi `strip_tags()` dari Django. Ini memastikan semua tag HTML dibuang dari string sebelum diselesaikan oleh proses validasi dan disimpan ke database.
