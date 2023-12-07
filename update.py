from conn import get_database_connection

def update_data():
    database = get_database_connection()
    collection = database['contacts']

    nama = input("Masukkan nama yang ingin diubah: ")
    new_nomor = input("Masukkan Nomor baru: ")
    new_email = input("Masukkan Email baru: ")

    filter_criteria = {"nama": nama}
    update_data = {"$set": {"nomor": new_nomor, "email": new_email}}

    update_result = collection.update_one(filter_criteria, update_data)
    if update_result.modified_count > 0:
        print("Kontak berhasil diperbarui")
    else:
        print("Tidak ada kontak yang diperbarui")

if __name__ == "__main__":
    update_data()
