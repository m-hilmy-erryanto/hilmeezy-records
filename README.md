Muhammad Hilmy Erryanto - 2206025905
PBP F
Link Adaptable : https://hilmeezy-records.adaptable.app/

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