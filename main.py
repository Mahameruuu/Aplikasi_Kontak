import sys
from create import main
from read import read_contact
from delete import delete_data_contact
from update import update_data

while True:
    print("Pilihan Opsi Contacts :")
    print("1. Create Contact")
    print("2. Read Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit\n")
    opsi = input("Masukkan Pilihan Anda: ")

    match opsi:
        case '1':
            main()
        case '2':
            read_contact()
        case '3':
            update_data()
        case '4':
            delete_data_contact()
        case '5':
            sys.exit