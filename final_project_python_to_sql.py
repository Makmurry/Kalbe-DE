# Melakukan import postgresql connector
import psycopg2
import psycopg2.extras

# Membuat Connector Variable
hostname = 'localhost'
database = 'kalbe'
username = 'postgres'
pwd = 'your password'
port_id = your_port
conn = None

# Melakukan percobaan koneksi
try:
    # Penggunaan with untuk menangani open dan close Connection serta Cursor 
    with psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id) as conn:
        
        # Membuat object cursor sebagai penanda
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            
            # Menghapus tabel karyawan (bila ada)
            cur.execute('DROP TABLE IF EXISTS karyawan')

            # Membuat tabel karyawan
            create_script = '''CREATE TABLE IF NOT EXISTS karyawan (
                                id INTEGER,
                                first_name VARCHAR(100),
                                last_name VARCHAR(100),
                                age INTEGER,
                                sex VARCHAR(10),
                                income INTEGER,
                                PRIMARY KEY(id))'''
            cur.execute(create_script)

            insert_script = 'INSERT INTO karyawan (id, first_name, last_name, age, sex, income) VALUES (%s, %s, %s, %s, %s, %s)'
            insert_values = [
                                (1, 'John', 'Doe', 30, 'Male', 5000000),
                                (2, 'Jane', 'Smith', 25, 'Female', 6000000),
                                (3, 'Michael', 'Johnson', 35, 'Male', 7500000)
                            ]
            # Deklarasi SQL Query untuk memasukkan record ke tabel (karyawan)
            try:
                for record in insert_values:
                    cur.execute(insert_script, record)
                    
                # Commit perubahan ke database setelah operasi INSERT berhasil
                conn.commit()  
            except Exception as insert_error:

                # Rollback jika terjadi error saat INSERT
                conn.rollback()  

                # Melempar kembali error untuk penanganan di luar blok try
                raise insert_error  

            # Menampilkan hasil Query
            cur.execute('SELECT * FROM karyawan')
            for record in cur:
                # Mengakses kolom tertentu
                first_name = record['first_name']
                income = record['income']
                print(first_name, income)

# Except Error dan Menutup Koneksi                                  
except Exception as error:
    print(error)
finally:
    if conn is not None:
        conn.close()
