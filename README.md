
<div style="display: flex; justify-content: space-between; align-items: center;">
  <img src="https://github.com/Makmurry/Kalbe-DE/blob/main/image/logo%20rakamin.png" alt="rakamin" width="300px">
  <img src="https://github.com/Makmurry/Kalbe-DE/blob/main/image/Kalbe_Nutritionals.png" alt="kalbe" width="300px">
</div>



**Presentasi Proyek dapat Anda akses [disini](https://www.canva.com/design/DAFtXs_YtHQ/MoG_73aEi34qqWuwHEDE5A/view?utm_content=DAFtXs_YtHQ&utm_campaign=designshare&utm_medium=link&utm_source=publishsharelink)**


**Challenge 1**

Create a shell/bash script to check whether a directory exists inside a given path.

**Variables:**
- `path=/hdfs/data/data1`
- `name_of_directory=data1`

**Conditions:**
- If the directory exists inside the path:
  - Echo "There is [Directory Name] Directory Exists!"
- If not:
  - Echo "[Directory Name] Directory Not Exists!"
  - Create a directory inside the path.

**Final Step:**
- Create a crontab syntax to run the script at 07:00 AM Daily.

---
**Membuat direktori bernama source**
```bash
mkdir source
```
**Pindah ke direktori source**
```bash
cd source
```
**Membuat file dengan nama daily_market_price.xlsx**
```bash
touch daily_market_price.xlsx
```

**Kembali ke parent direktori**
```bash
cd /home/project
```
**Membuat file script**
```bash
touch data_management_script.sh
```
**Cek path saat ini menggunakan perintah :**
```bash
pwd
```
- Buka script data_management_script.sh
- lalu masukan skript berikut :

```bash
#!/bin/bash

# Define the variables
path="/home/project"
name_of_directory="data1"

# Check if the directory exists
if [ -d "$path/$name_of_directory" ]; then
  echo "There is $name_of_directory Directory Exists!"
else
  echo "$name_of_directory Directory Not Exists!"
  mkdir "$path/$name_of_directory"
  echo "Created $name_of_directory directory."
fi
```
---
**Memberi izin eksekusi script**
```bash
chmod +x data_management_script.sh
```
**Menjalankan script**
```bash
./data_management_script.sh
```
**Direktori data1 telah berhasil dibuat**
---
 **CRONTAB SYNTAX:** 

- Ketik pada terminal :
```bash
crontab -e 
```
lalu paste command berikut menjalankan skrip setiap hari pukul 07:00 AM:
```bash
0 7 * * * /home/project/data_management_script.sh
```
- Tekan ctrl + x
- Tekan Y , lalu Enter

Untuk melihat list crontab ketik :
```bash
crontab -l
```

## Challenge 2

Using the script from question number 1, add another condition if a directory exists inside the path.

**Variables:**
- `filename_excel=daily_market_price.xlsx`
- `source_dir=/local/data/market`
- `target_dir=Refer to Question Number 1 Path`

**Conditions:**
- Copy the file from the source directory into the target directory.
- Create a log file inside the same path with "File Moved Successfully" as a log content if successful.

**Ubah isi file task 1 menjadi seperti berikut :**
---
```bash
#!/bin/bash

# Define the variables
path="/home/project"
name_of_directory="data1"

# Check if the directory exists
if [ -d "$path/$name_of_directory" ]; then
  echo "There is $name_of_directory Directory Exists!"
else
  echo "$name_of_directory Directory Not Exists!"
  mkdir "$path/$name_of_directory"
  echo "Created $name_of_directory directory."
fi

# Define the variables for copying
filename_excel="daily_market_price.xlsx"
source_dir="$path/source"
target_dir="$path/$name_of_directory"

# Check if the source directory exists
if [ -d "$source_dir" ]; then
  # Copy file from source directory to target directory
  cp "$source_dir/$filename_excel" "$target_dir/"

  # Check if the copy was successful
  if [ $? -eq 0 ]; then
    echo "File Moved Successfully" > "$target_dir/log.txt"
  else
    echo "File Move Failed" > "$target_dir/log.txt"
  fi
else
  echo "Source directory $source_dir does not exist."
fi
```
---
- Jalankan script secara manual untuk menyalin file dan membuat log:
```bash
./data_management_script.sh
```
---
- `Buka folder data1`
- ` file xls telah berhasil dipindahkan`
- `dan log telah berhasil dibuat yang berisi "File Moved Successfully"`


## Challenge 3

Complete the below Syntax {Highlighted Sentence} to insert data from Python to MySQL.
![task3](https://github.com/Makmurry/Kalbe-DE/blob/main/image/task3.jpg)

**Lihat Script Pyhton [disini](https://github.com/Makmurry/Kalbe-DE/blob/main/final_project_python_to_sql.py)**

## Challenge 4

Convert this instruction into SQL Query Language.

**SQL Instructions:**
- Create a database with 'KALBE' as the name.
- Inside the database, create a table named 'Inventory' with columns:
  - Item_code
  - Item_name
  - Item_price
  - Item_total
- Choose appropriate data types and lengths according to best practice.
- Choose one unique column as a primary key and decide column constraints.
- Insert the provided data into the table:
![task4](https://github.com/Makmurry/Kalbe-DE/blob/main/image/task4.jpg)
- Show Item_name that has the highest number in Item_total.
- Update the Item_price of the output of the question bullet.
- Describe what will happen if we insert another Item_name with Item_code of 2343 into the table.
- Delete the Item_name that has the lowest number of Item_total.

---
**Membuat Tabel Inventory**
```sql
CREATE TABLE inventory (
    Item_code INT PRIMARY KEY,
    Item_name VARCHAR(255),
    Item_price INT,
    Item_total INT,
    PRIMARY KEY (Item_code)
);

INSERT INTO inventory (Item_code, Item_name, Item_price, Item_total)
VALUES
    (2341, 'Promag Tablet', 3000, 100),
    (2342, 'Hydro Coco 250ML', 7000, 20),
    (2343, 'Nutrive Benecol 100ML', 20000, 30),
    (2344, 'Blackmores Vit C 500Mg', 95000, 45),
    (2345, 'Entrasol Gold 370G', 90000, 120);
```
**Menampilkan Item_name dengan jumlah tertinggi dalam kolom Item_total:**
```sql
SELECT Item_name
FROM Inventory
WHERE Item_total = (SELECT MAX(Item_total) FROM inventory);
```
**Mengupdate Item_price dari hasil pertanyaan sebelumnya:
Kasus: Memberikan diskon 10% pada semua item dengan item_total > 100**
```sql
UPDATE inventory
SET Item_price = Item_price * 0.9 -- Mengurangi 10%
WHERE Item_total > 100;
```
**Menyisipkan Item_name lain dengan Item_code 2343**
```sql
INSERT INTO Inventory (Item_code, Item_name)
VALUES (2343, 'new_item');
```
---
**Note :**
Jika kita mencoba menyisipkan data baru dengan Item_code 2343 yang sudah ada sebelumnya, maka akan mengalami kesalahan unik karena Item_code diatur sebagai PRIMARY KEY. 
Tabel tersebut hanya bisa memiliki satu baris dengan Item_code yang sama sebagai PRIMARY KEY,  dan mencoba menyisipkan baris baru dengan nilai yang sama akan menghasilkan kesalahan.

---
**Menghapus Item_name dengan jumlah terendah dalam kolom Item_total:**
```sql
DELETE FROM Inventory
WHERE Item_total = (SELECT MIN(Item_total) FROM Inventory);
```
## Challenge 5

Create a query to display all customer orders where the purchase amount is less than 100 or exclude those orders where the order date is on or greater than 25 Aug 2022 and the customer ID is above 2001.
![task5](https://github.com/Makmurry/Kalbe-DE/blob/main/image/task5.jpg)

**Sample table:**
- Table Name: customer_orders

---

**Membuat tabel customer_orders:**
```sql
CREATE TABLE customer_orders (
    order_no INT PRIMARY KEY,
    purchase_amount INT,
    order_date DATE,
    customer_id INT,
    salesman_id INT
);

INSERT INTO customer_orders (order_no, purchase_amount, order_date, customer_id, salesman_id)
VALUES
    (10001, 150, '2022-10-05', 2005, 3002),
    (10009, 279, '2022-09-10', 2001, 3005),
    (10002, 65, '2022-10-05', 2002, 3001),
    (10004, 110, '2022-08-17', 2009, 3003),
    (10007, 948, '2022-09-10', 2005, 3002),
    (10005, 2400, '2022-07-27', 2007, 3001);

SELECT *
FROM customer_orders
WHERE 
	purchase_amount < 100 
	OR 
	order_date >= '2022-08-25' 
	AND 
	customer_id > 2001;
```
---
**`Dalam kueri di atas, kita menggunakan SELECT * untuk memilih semua kolom dari tabel customer_orders.
Kemudian menggunakan kondisi (purchase_amount < 100 OR order_date < '2022-08-25') untuk memilih pesanan dengan jumlah pembelian kurang dari 100 atau tanggal pesanan sebelum 25 Agustus 2022.
Selanjutnya, kita menambahkan kondisi AND customer_id <= 2001 untuk hanya memilih pesanan dengan customer_id kurang dari atau sama dengan 2001.
Kueri ini akan menampilkan semua pesanan pelanggan yang memenuhi salah satu atau kedua kondisi tersebut.`**

# Challenge 6

Please explain what is wrong with this picture and give the best solution for this case.

![task6](https://github.com/Makmurry/Kalbe-DE/blob/main/image/task6.jpg)

**Berdasarkan gambar, kesalahan mungkin terletak pada :**

- Tipe data yang digunakan:
`Tipe data NVARCHAR digunakan untuk menyimpan data teks berbasis karakter Unicode.
Perbedaan utama antara NVARCHAR dan VARCHAR adalah bahwa NVARCHAR mendukung karakter Unicode,
sedangkan VARCHAR biasanya mengacu pada karakter yang menggunakan satu set karakter kode tertentu (misalnya, ASCII).`
- Operator logika yang digunakan dalam pernyataan SQL untuk menggabungkan kondisi logis

**Solusi yang Disarankan:**
- Gunakan VARCHAR sebagai tipe data untuk kolom teks khususnya pada kolom ddPlant untuk menghindari kesalahan inputkarakter tertentu pada value
- Gunakan operator logika AND. Operator AND digunakan untuk menggabungkan dua atau lebih kondisi logis, dan semua kondisiharus benar (True) agar baris data diterima.
Pada kasus ini tampilan output yang diharapkan adalah : 
`Request Type = 'Modern Trade PO' AND Plant = 'Belawan'`

##  Challenge 7

Create a simple star schema for the KALBE database consisting of 1 Fact and 5 Dimensions using Physical Data Model Theory.


![ERD task7](https://github.com/Makmurry/Kalbe-DE/blob/main/image/ERD%20task7.jpg)

**Lihat pembuatan simple star schema (ERD) [disini](https://dbdiagram.io/d/simple-star-schema-6525138dffbf5169f062ce86)**


