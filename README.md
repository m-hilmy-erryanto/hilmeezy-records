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
    2. JSON
    3. XML
    4. JSON by ID
    5. XML by ID