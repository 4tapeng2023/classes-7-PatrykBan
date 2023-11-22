from xml_file_processor import FileProcessor
import xml.etree.ElementTree as ET

def main():
    processor = FileProcessor()

    while True:
        print("\nMenu:")
        print("1. Read XML File")
        print("2. Add Record")
        print("3. Delete Record")
        print("4. Update Record")
        print("5. Display Records")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter the XML file name: ")
            processor.read_file(filename)

        elif choice == "2":
            filename = input("Enter the XML file name: ")
            name = input("Enter the name: ")
            age = input("Enter the age: ")

            # Creating an example record
            record_str = f'<record><name>{name}</name><age>{age}</age></record>'
            record = ET.fromstring(record_str)
            
            processor.add_record(filename, record)

        elif choice == "3":
            filename = input("Enter the XML file name: ")
            record_id = input("Enter the record id to delete: ")
            processor.delete_record(filename, record_id)

        elif choice == "4":
            filename = input("Enter the XML file name: ")
            record_id = input("Enter the record id to update: ")
            new_name = input("Enter the new name: ")
            new_age = input("Enter the new age: ")

            # Creating an example updated record
            new_record_str = f'<record><name>{new_name}</name><age>{new_age}</age></record>'
            new_record = ET.fromstring(new_record_str)
            
            processor.update_record(filename, record_id, new_record)

        elif choice == "5":
            filename = input("Enter the XML file name: ")
            processor.display_records(filename)

        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()