Muhammad Hilmy Erryanto - 2206025905
PBP F
Link Adaptable : https://hilmeezy-records.adaptable.app/

Tugas 2
- Pengimplementasian Checklist
    1. Membuat proyek Django baru:
        Diawali dengan membuat direktori baru (Tugas 2) dan menginisiasi git di direktori tersebut. Lalu, saya membuat repository baru di github (hilmeezy-records) dan menghubungkan direktori lokal dengan repository baru. Lalu setelahnya saya membuat virtual environment di direktori tersebut dan mengaktifkannya. Lalu saya membuat file requirements.txt yang berisi semua dependensi dan menginstallnya dengan menjalankan "pip install -r requirements.txt". Terakhir, saya menjalankan perintah "django-admin startproject hilmeezy_records ."

    2. Membuat aplikasi main pada proyek:
        Diawali dengan mengaktifkan virtual environment pada direktori proyek. Lalu saya menjalankan "python manage.py startapp main".

    3. Melakukan routing pada proyek:
        Saya membuka file setting.py di direktori proyek dan memasukan string "main" ke dalam list "INSTALLED_APPS"

    4. Membuat model Item pada aplikasi main:
        Pada file models.py di direktori main, saya membuat class bernama item. Karena saya berencana membuat toko jualan album musik, maka item ini memiliki atribut name (CharField), amount (IntegerField), description (TextField), category (TextField), dan price (IntegerField).

    5. Membuat fungsi pada views.py:
        Pada file views.py, saya membuat fungsi show_main yang berisi dictionary dengan value berupa nama aplikasi, nama, dan kelas saya, yang akan ditampilkan di main.html. Setelahnya saya melakukan migrasi model.

    6. Membuat routing pada urls.py aplikasi main:
        Saya mengisi urls.py pada direktori main dengan membuat list "urlpatterns" sebagai definisi-definisi untuk aplikasi ini dan mengisi definisi utamanya dengan "path('', show_main, name='show_main')"

    7. Melakukan deployment ke Adaptable:
        Sebelum melakukan deployment ke adaptable saya memastikan telah push semua yang diperlukan lalu saya memulai deploy dengan menghubungkan repository hilmeezy-records ke adaptable dan memilih main, lalu memilih Python template dan PostgreSQL database. Terakhir saya memasukan start command yang sesuai.


- Bagan Request Client

![bagan_request_client](https://github.com/m-hilmy-erryanto/hilmeezy-records/assets/118323734/448bed1d-9fb1-425c-aa9f-e2510aa6f04d)

    1. Client melakukan http request ke url
    2. Server menjalankan fungsi Views sesuai request client
    3. Views mengakses Models
    4. Models mengambil data dari database dan memberikan hasilnya ke Views
    5. Views mengakses templates/main.html
    6. Views mengirim hasil jadi main.html kepada client


- Alasan Penggunaan Virtual Environment
    Penggunaan virtuan environment berguna untuk mengisolasi tiap proyek Django sehingga kita bisa mengelola dependensi tiap proyek Django tanpa khawatir adanya konflik antar proyek akibat perbedaan dependensi. Kita bisa saja tidak menggunakan virtual environment, tapi bisa saja ada potensi masalah karena konflik perbedaan versi-versi dependensi proyek dan ketidakstabilan proyek.


- MVC, MVT, MVVM, dan Perbedaan Ketiganya
    - MVC: MVC adalah singkatan dari Model, View, and Controller
        - Model: Komponen yang mengatur dan mengelola data dari aplikasi
        - View: Komponen yang menampilkan daya kepada pengguna dan menangani interaksi pengguna
        - Controller: Komponen yang mengontrol aliran data antara Model dan View
    - MVC digunakan untuk software system development.

    - MVT: MVT adalah singkatan dari Model, View, and Template
        - Model: Komponen yang mengatur dan mengelola data dari aplikasi
        - View: Komponen yang mengatur logika presentasi, menghubungkan model dan template.
        - Template: Komponen yang mengatur tampilan website ke pengguna
    - MVT penggunaannya seperti MVC tapi khusus untuk Django

    - MVVM: MVVM adalah singkatan dari Model, View, and ViewModel
        - Model: Komponen yang mengatur dan mengelola data dari aplikasi
        - View: Komponen yang menampilkan data ke pengguna dan menangani tampilan
        - ViewModel: Komponen yang mempersiapkan data yang akan ditampilan di View dan menghubungkannya dengan Model
    - MVVM digunakan dalam application development bagian UI (User Interface)

Tugas 3
- Pengimplementasian Checklist
    (note: saya mengganti semua kata Item pada proyek saya dengan Record agar lebih spesifik dengan konteks toko record saya. )
    1. Membuat input form:
        Sebelumnya saya membuat forms.py yang berisi class RecordForm pada direktori main sebagai struktur dari form. Lalu saya menambahkan fungsi create_record pada views.py direktori main yang akan menambahkan data saat kita mensubmit form. Saya juga menambahkan variabel records di fungsi show_main yang digunakan untuk mengambil seluruh object Record dari database. Setelahnya saya mengurusi html. Saya membuat create_record.html sebagai laman untuk kita menambah record dan mengimplementasikan fungsi create_record. Lalu saya membuat penambahan di main.html, yakni menambahkan tabel yang berisi data record yang sudah ditambahkan dan membuat button Add New Record untuk menambahkan record, button ini akan mengarahkan kita ke create_product.html yang sudah dibuat sebelumnya.
    2. Menambahkan 5 fungsi views:
        fungsi yang ditambahkan untuk melihat objek yang ditambahkan adalah fungsi show_main (dalam bentuk html), show_xml, show_json, show_xml_by_id, dan show_json_by_id. Semua fungsi tersebut menerima parameter request. Fungsi-fungsi tersebut mengambil data dari model Record. Mengambil datanya bisa semua data (dengan Record.objects.all()) atau data dengan id tertentu saja (seperti pada show_json_by_id dan show_xml_by_id dengan Record.objects.filter(pk=id)). Lalu mengirimkan data-datanya sebagai respons dalam masing-masing format yang sesuai (bisa html, json, xml). 

    3. Membuat routing URL untuk masing-masing fungsi views:
        Membuat routingnya dengan cara membuka urls.py di main dan mengimport kelima fungsi tersebut. Lalu kita menambahkan masing-masing tipe path url ke dalam urlpatterns, misal: path('json/', show_json, name='show_json')


- Apa perbedaan antara form POST dan form GET dalam Django?
    Perbedaannya bisa dilihat dari segi metode pengiriman, kemampuan, dan keamanannya. Dari segi metode pengiriman, GET akan menambahkan data yang dikirim ke url dan bisa dilihat oleh orang-orang, sedangkan POST tidak. Lalu, karena GET ditambahkan ke url, maka dari segi kemampuan GET lebih cocok untuk mengirim data kecil karena ada batasan data di url, sedangkan POST digunakan untuk mengirim data yang lebih besar. Dari segi keamanan, karena GET ditambahkan ke url, apabila datanya sensitif orang lain juga bisa melihat, sedangkan data yang dikirim dengan POST cenderung lebih aman.


- Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
    HTML berbeda dengan dua lainnya. HTML sendiri lebih digunakan untuk kepentingan penggambaran data serta membuat dan mengatur tampilan web, sedangkan XML dan JSON digunakan untuk mengirimkan data. Perbedaan XML dengan JSON adalah XML bisa digunakan untuk pertukaran data antar sistem, konfigurasi, dan penyimpana data yang kompleks, sedangkan JSON lebih digunakan untuk pertukaran data antara klien dan server dalam pengempangan web dan API.


- Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
    JSON lebih sering digunakan karena dibandingkan dengan XML, JSON lebih sederhana dan mudah dibaca oleh manusia. Lalu, JSON juga mempunyai format data yang lebih ringan sehingga pertukaran datanya lebih efisien. Terakhir, JSON cocok digunakan bersama JavaScript dimana JavaScript mendominasi web development sehingga developer lebih memilih menggunakan JSON dibanding tipe lain.


- Screenshot Postman
    1. HTML
    ![HTML](https://github.com/m-hilmy-erryanto/hilmeezy-records/blob/main/images/HTML.png)
    2. JSON
    ![JSON](https://github.com/m-hilmy-erryanto/hilmeezy-records/blob/main/images/JSON.png)
    3. XML
    ![XML](https://github.com/m-hilmy-erryanto/hilmeezy-records/blob/main/images/XML.png)
    4. JSON by ID
    ![JSON by ID](https://github.com/m-hilmy-erryanto/hilmeezy-records/blob/main/images/JSON%20by%20ID.png)
    5. XML by ID
    ![XML by ID](https://github.com/m-hilmy-erryanto/hilmeezy-records/blob/main/images/XML%20by%20ID.png)

- Bonus:
    Saya berhasil menambahkan pesan dan menampilkannya di atas tabel data. Pesan yang ditampilkan adalah "You have stored x records in this application". Hal ini diimplementasikan dengan menambahkan line <span>You have stored {{ records|length }} records in this application</span> di main.html dengan {{ records|length}} untuk mencari banyak data dalam tabel.

Tugas 4
- Pengimplementasian Checklist
    1. Mengimplementasikan fungsi registrasi, login, dan logout:
        Sebelumnya saya mengubah main.html menjadi restricted agar pengguna yang sudah login saja yang bisa mengaksesnya.
        - Registrasi:
            Registrasi dilakukan dengan membuat register.html dan fungsi register pada views. register.html akan menjadi halaman untuk user meregister akun. Pada register.html, user diminta untuk memasukan username dan password yang mereka mau.
        - Login:
            Login dilakukan dengan membuat login.html dan fungsi login_user pada views. login.html akan menjadi halamn untuk user login. User tidak akan bisa pindah ke main.html jika belum berhasil login.
        - Logout:
            Logout dilakukan dengan membuat fungsi logout_user pada views. Fungsi logout_user ini akan dipanggil saat user menekan tombol Logout yang sudah saya buat di main.html.

    2. Membuat dua akun pengguna dengan masing-masing tiga dummy data:
        Saya membuat akun pengguna dengan melakukan registrasi sebanyak dua kali. Lalu setelah berhasil registrasi saya login pada masing-masing akun, pada halaman main, saya menambahkan record sebanyak 3 kali. Berikut gambarnya:
        ![USER1](https://github.com/m-hilmy-erryanto/hilmeezy-records/blob/main/images/User%201.png)
        ![USER2](https://github.com/m-hilmy-erryanto/hilmeezy-records/blob/main/images/User%202.png)

    3. Menghubungkan model Record dengan User:
        Cara saya menghubungkan model Record dengan user adalah dengan menambahkan atribut user sebagai foreign key di Record. Lalu, saya mengubah fungsi show_main dan create_record di views agar penggunaan dua fungsi tersebut hanya bisa diakses oleh user yang sedang login.

    4. Menampilkan username pengguna yang sedang logged in seperti username dan menerapkan last login:
        Cara saya menampilkan username pengguna yang sedang login adalah dengan menambahkan line "<span>Welcome back, {{ name }}!<span>". Lalu untuk last login saya menambahkan line "<h5>Sesi terakhir login: {{ last_login }}</h5>" di main.html dengan last_login dipanggil dari context yang ada di fungsi show_main. name dan last_login merupakan context yang ada di show_main. Kedua penambahan dilakukan di main.html

- Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
    Django UserCreationForm adalah formulir yang ada di Django yang bisa digunakan untuk membuat akun baru di aplikasi web. Kelebihan dari UserCreationForm adalah sudah terintegrasi dengan Django User Model dan adanya keamanan untuk serangan seperti CSRF (Cross-Site Request Forgery) dan XSS (Cross-Site Scripting). Kekurangan dari UserCreationForm adalah tampilan defaultnya kurang bagus.

- Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
    Autentikasi adalah proses untuk memastikan siapa yang sedang login. Otorisasi adalah proses untuk memastikan apakah user memiliki akses untuk melakukan suatu hal. Keduanya penting untuk memastikan keamanan aplikasi kita agar tidak ada orang asing yang menggunakan aplikasi kita.

- Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
    Cookies adalah data yang disimpan oleh server web pada device pengguna. pada perangkat pengguna. Django menggunakannya dengan membuat cookies dan menyimpannya di awal, lalu selama pengguna menggunakan web, data sesi akan diperbarui sesuai aktivitas pengguna. Saat pengguna logout, cookies akan dihapus.

- Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
    Penggunaan cookies secara default belum aman. Contoh risiko potensialnya adalah serangan CSRF dan XSS, serta penyalahgunaan cookies.

- Bonus:
    1. Tombol dan fungsi untuk menambahkan dan mengurangi jumlah objek:
        Saya membuat tombol "+1" dan "-1" yang terletak di kolom action. Kedua tombol ini menjalankan fungsi yang sesuai dengan masing-masing, +1 menjalankan fungsi add_one, -1 menjalankan remove_one.
    2. Tombol dan fungsi untuk menghapus objek:
        Sama juga seperti +1 dan -1, tombol Del yang terletak di kolom action bisa meremove object. Tombol ini menjalankan fungsi delete_record.

Tugas 5
- Pengimplementasian Checklist
    - Kustomisasi desain pada template HTML:
        1. Kustomisasi halaman login, register, dan tambah inventori
            Saya menggunakan card pada halaman login dan register, saya buat tampilan keduanya mirip, untuk edit dan add record saya merapikannya agar ada di tengah
        2. Kustomisasi halaman daftar inventori
            Saya menambahkan navbar, memindahkan tombol-tombol, dan mengganti tabel records dengan container berisi card dengan display flex dan flex-wrap agar lebih rapi
            ![inventori]https://github.com/m-hilmy-erryanto/hilmeezy-records/blob/main/images/Screenshot%20(544).png

- Jelaskan manfaat dari setiap selector dan kapan waktu yang tepat untuk menggunakannya.
    Selector dalam CSS ada tiga yakni Element Selector, Class Selector, dan ID Selector.
        1. Element Selector
            Element selector digunakan untuk mengubah properti dengan tag HTML yang sama. Element selector digunakan apabila kita ingin membuat karakteristik yang sama untuk elemen tertentu. 
        2. Class Selector
            Class selector digunakan untuk mengelompokkan elemen dengan karakteristik yang sama. Class selector digunakan apabila kita ingin mengubah properti dari kelompok-kelompok elemen dengan ubahan yang sama.
        3. ID Selector
            ID selector digunakan untuk mengubah properti yang memiliki ID unik. ID Selector kita gunakan apabila kita ingin merubah 1 properti saja.

- Jelaskan HTML5 Tag yang kamu ketahui.
    Berikut beberapa HTML5 Tag yang saya ketahui:
        1. `<head>`
            Tag ini berisi informasi seperti title halaman, dan informasi meta lainnya.
        2. `<body>`
            Tag ini berisi konten yang mau ditampilkan ke pengguna.
        3. `<h1>` hingga `<h6>`
            Tag ini merupakan heading. Tag ini digunakan untuk menandai judul. `<h1>` merupakan jenis yang paling tinggi.
        4. `<p>`
            Tag ini menandai teks paragraf.
        5. `<a>`
            Tag ini menandai hyperlink.

- Jelaskan perbedaan antara margin dan padding.
    Margin digunakan untuk mengatur area di sekitar border, sedangkan padding digunakan mengatur area di sekitar konten

- Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan salah satunya?
    Berikut perbedaan antara Tailwind dan Bootstrap:
        1. Tailwind cenderung lebih fleksibel dan memberikan developer kontrol yang lebih banyak dibandingkan bootstrap karena bootstrap komponen-komponennya sudah dibuat sebelumnya
        2. Tailwind ukuran filenya lebih ringan dibandingkan bootstrap
        3. Bootstrap lebih ramah pemula untuk dipelajari dibanding Tailwind karena komponen di bootstrap sudah dibuat terlebih dahulu
        
    Pemilihan penggunaan Tailwind dan Bootstrap tergantung kebutuhan kita. Apabila kita masih pemula dan memiliki waktu terbatas, disarankan menggunakan Bootstrap. Apabila kita menginginkan kustomisasi tinggi dan kode yang ringan, disarankan menggunakan Tailwind
