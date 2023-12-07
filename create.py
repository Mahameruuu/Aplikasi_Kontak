from conn import get_database_connection

def insert_data_to_contacts(nama, nomor, email):
    collection = get_database_connection()['contacts']

    data_to_insert = {
        "nama": nama,
        "nomor": nomor,
        "email": email
    }

    insert_result = collection.insert_one(data_to_insert)
    print("Kontak berhasil ditambahkan dengan ID:", insert_result.inserted_id)

def main():
    nama = input("Masukkan nama: ")
    nomor = input("Masukkan nomor: ")
    email = input("Masukkan email: ")

    insert_data_to_contacts(nama, nomor, email)

