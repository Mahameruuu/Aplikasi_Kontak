from conn import get_database_connection

def read_contact():
    database = get_database_connection()
    collection = database['contacts']

    all_contacts = collection.find()

    for contact in all_contacts:
        print(contact)
