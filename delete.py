from conn import get_database_connection

def delete_data_contact():
    database = get_database_connection()
    collection = database['contacts']

    nama = input("Masukkan nama yang ingin dihapus: ")

    filter_criteria = {"nama": nama}

    delete_result = collection.delete_one(filter_criteria)
    print(delete_result.deleted_count)

if __name__ == "__main__":
    delete_data_contact()