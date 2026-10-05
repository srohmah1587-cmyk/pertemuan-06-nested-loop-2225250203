# Pertemuan 06 Nested Loop Python

**Nama:** Siti Rohmah
**NIM:** 2225250203
**Kelas:** 3A

## Tujuan

Menggunakan nested loop, pola, akumulasi, dan pencacahan dalam program Python. Program yang dibuat berupa tabel perkalian dan statistik sederhana berdasarkan nilai `n` yang dimasukkan oleh pengguna.

## Cara Menjalankan

Program dapat dijalankan menggunakan perintah berikut:

```bash
python3 tugas/tabel_perkalian_dan_statistik.py
```

## Algoritma Tugas 3

Algoritma program adalah sebagai berikut:

1. Menampilkan judul **Tabel Perkalian dan Statistik**.
2. Meminta pengguna memasukkan nilai `n`.
3. Melakukan validasi nilai `n` menggunakan `while`. Jika `n` kurang dari atau sama dengan 0, pengguna diminta memasukkan nilai kembali.
4. Menginisialisasi `total_keseluruhan` dengan nilai `0`.
5. Menginisialisasi `counter_genap` dengan nilai `0`.
6. Menggunakan loop luar untuk mengatur baris tabel dari `1` sampai `n`.
7. Menginisialisasi `total_baris` dengan nilai `0` pada setiap baris.
8. Menggunakan loop dalam untuk mengatur kolom dari `1` sampai `n`.
9. Menghitung hasil perkalian antara baris dan kolom.
10. Menambahkan hasil perkalian ke `total_baris`.
11. Menambahkan hasil perkalian ke `total_keseluruhan`.
12. Memeriksa apakah hasil perkalian merupakan bilangan genap. Jika genap, `counter_genap` ditambah `1`.
13. Menampilkan total dari setiap baris.
14. Menampilkan total keseluruhan dan jumlah bilangan genap setelah semua perulangan selesai.

### Peran Komponen Program

| Komponen            | Peran                                                            |
| ------------------- | ---------------------------------------------------------------- |
| Loop luar           | Mengatur setiap baris pada tabel perkalian.                      |
| Loop dalam          | Mengatur setiap kolom pada tabel perkalian.                      |
| `total_baris`       | Menjumlahkan seluruh hasil perkalian pada satu baris.            |
| `total_keseluruhan` | Menjumlahkan seluruh hasil perkalian dalam tabel.                |
| `counter_genap`     | Menghitung jumlah hasil perkalian yang merupakan bilangan genap. |
| `while`             | Memvalidasi agar nilai `n` lebih besar dari 0.                   |

## Hasil Pengujian

### Pengujian 1

| Input   | Hasil yang Diharapkan                                                | Keluaran Aktual                                            | Status   |
| ------- | -------------------------------------------------------------------- | ---------------------------------------------------------- | -------- |
| `n = 3` | Tabel perkalian 3 × 3, total keseluruhan 36, jumlah bilangan genap 5 | Tabel 3 × 3, total keseluruhan 36, jumlah bilangan genap 5 | Berhasil |

Keluaran:

```text
Tabel Perkalian dan Statistik
n: 3
   1    2    3 | Total baris = 6
   2    4    6 | Total baris = 12
   3    6    9 | Total baris = 18

Statistik:
Total keseluruhan = 36
Jumlah bilangan genap = 5
```

### Pengujian 2

| Input   | Hasil yang Diharapkan                                               | Keluaran Aktual                                           | Status   |
| ------- | ------------------------------------------------------------------- | --------------------------------------------------------- | -------- |
| `n = 2` | Tabel perkalian 2 × 2, total keseluruhan 9, jumlah bilangan genap 3 | Tabel 2 × 2, total keseluruhan 9, jumlah bilangan genap 3 | Berhasil |

### Pengujian 3

| Input   | Hasil yang Diharapkan                                          | Keluaran Aktual                                       | Status   |
| ------- | -------------------------------------------------------------- | ----------------------------------------------------- | -------- |
| `n = 0` | Program menolak input dan meminta nilai `n` lebih besar dari 0 | Program meminta pengguna memasukkan nilai `n` kembali | Berhasil |

## Analisis Efisiensi

Program menggunakan dua `for` yang berada di dalam satu sama lain atau disebut **nested loop**.

Loop luar berjalan sebanyak `n` kali. Pada setiap satu kali perulangan loop luar, loop dalam juga berjalan sebanyak `n` kali.

Jadi, jumlah eksekusi badan loop dalam adalah:

```text
n × n = n²
```

Contoh:

| Nilai `n` | Jumlah eksekusi loop dalam |
| --------: | -------------------------: |
|         2 |                          4 |
|         3 |                          9 |
|         5 |                         25 |
|        10 |                        100 |

Dengan demikian, kompleksitas waktu bagian nested loop pada program ini adalah **O(n²)**. Artinya, semakin besar nilai `n`, semakin banyak perulangan yang harus dilakukan oleh program.

## Refleksi

Salah satu kesalahan yang dapat terjadi pada nested loop adalah meletakkan `total_baris = 0` di luar loop luar. Jika hal tersebut dilakukan, nilai total dari baris sebelumnya akan ikut terbawa ke baris berikutnya sehingga hasil total setiap baris menjadi tidak sesuai.

Kesalahan tersebut dapat diperbaiki dengan meletakkan:

```python
total_baris = 0
```

di dalam loop luar dan sebelum loop dalam dimulai. Dengan begitu, setiap baris akan memulai perhitungan total dari nilai `0`.

Selain itu, `total_keseluruhan` dan `counter_genap` harus diinisialisasi sebelum nested loop agar keduanya dapat digunakan untuk menghitung seluruh hasil perkalian dari tabel.
