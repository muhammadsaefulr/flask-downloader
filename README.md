# Downloader Instagram dan YouTube

Repositori ini menyediakan program REST API yang dibangun dengan Flask untuk mengunduh konten dari Instagram dan YouTube. Program ini menggunakan `instaloader` untuk mengambil konten Instagram dan `pytube` untuk video YouTube. Program Rest API ini juga mendukung Cross-Origin Resource Sharing (CORS) menggunakan `flask-cors`.

## Fitur

- Mengunduh gambar dan video dari Instagram
- Mengunduh video dari YouTube
- Dukungan CORS untuk akses lintas domain

## Instalasi

1. **Clone repositori ini**

   ```sh
   git clone https://github.com/username/downloader-insta-youtube.git
   cd downloader-insta-youtubeI
   ```

2. **Buat virtual environtment nya**

```sh
python3 -m venv venv
source venv/bin/activate
```

3. **Install library/framework yang dibutuhkan**

```sh
pip install -r requirements.txt
```

### Menjalankan Programnya

1. **Aktifkan virtual environment**

```sh
source venv/bin/activate
```

2. **Jalankan Flask**

```sh
python app.py
```

### Akses API di

http://127.0.0.1:5000/api/v1
http://127.0.0.1:5000/api/v1/{servicename}/?url=
