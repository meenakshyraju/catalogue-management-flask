 # main.py

from dto.catalogue import Catalogue
from service.catalogue_service import CatalogueService
from util.validators import (
    validate_catalogue_name,
    validate_description,
    validate_date_format,
    validate_catalogue_id
)
from exception.catalogue_custom_exceptions import CatalogueException, CatalogueNotFoundException
from datetime import datetime

def main():
    """
    Main function to display CLI menu, take user inputs,
    validate them, and  to call appropriate service methods.
    """
    
    catalogue_service = CatalogueService()

    while True:
        print("\n--- Catalogue Management System ---")
        print("1. Create Catalogue")
        print("2. Get All Catalogues")
        print("3. Get Catalogue by ID")
        print("4. Update Catalogue by ID")
        print("5. Delete Catalogue by ID")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            try:
                name = input("Enter Catalogue Name: ")
                validate_catalogue_name(name)

                description = input("Enter Catalogue Description: ")
                validate_description(description)

                start_date_str = input("Enter Start Date (YYYY-MM-DD): ")
                validate_date_format(start_date_str)
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()

                end_date_str = input("Enter End Date (YYYY-MM-DD): ")
                validate_date_format(end_date_str)
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

                cata_obj = Catalogue(name, description, start_date, end_date)
                catalogue_service.create_catalogue(cata_obj)

            except CatalogueException as ce:
                print(f"Error: {ce}")

        elif choice == "2":
            try:
                catalogues = catalogue_service.get_all_catalogues()
                for row in catalogues:
                    print(row)
            except CatalogueException as ce:
                print(f"Error: {ce}")

        elif choice == "3":
            try:
                catalogue_id = int(input("Enter Catalogue ID: "))
                validate_catalogue_id(catalogue_id)

                catalogue = catalogue_service.get_catalogue_by_id(catalogue_id)
                print(catalogue)
            except CatalogueNotFoundException as cnfe:
                print(f"Not Found: {cnfe}")
            except CatalogueException as ce:
                print(f"Error: {ce}")
            except ValueError:
                print("Invalid input. Catalogue ID must be an integer.")

        elif choice == "4":
            try:
                catalogue_id = int(input("Enter Catalogue ID to Update: "))
                validate_catalogue_id(catalogue_id)

                name = input("Enter New Catalogue Name: ")
                validate_catalogue_name(name)

                description = input("Enter New Catalogue Description: ")
                validate_description(description)

                start_date_str = input("Enter New Start Date (YYYY-MM-DD): ")
                validate_date_format(start_date_str)
                start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()

                end_date_str = input("Enter New End Date (YYYY-MM-DD): ")
                validate_date_format(end_date_str)
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()

                updated_catalogue = Catalogue(name, description, start_date, end_date)
                catalogue_service.update_catalogue_by_id(catalogue_id, updated_catalogue)

            except CatalogueNotFoundException as cnfe:
                print(f"Not Found: {cnfe}")
            except CatalogueException as ce:
                print(f"Error: {ce}")
            except ValueError:
                print("Invalid input. Catalogue ID must be an integer.")

        elif choice == "5":
            try:
                catalogue_id = int(input("Enter Catalogue ID to Delete: "))
                validate_catalogue_id(catalogue_id)
                catalogue_service.delete_catalogue_by_id(catalogue_id)

            except CatalogueNotFoundException as cnfe:
                print(f"Not Found: {cnfe}")
            except CatalogueException as ce:
                print(f"Error: {ce}")
            except ValueError:
                print("Invalid input. Catalogue ID must be an integer.")

        elif choice == "6":
            print("Exiting Catalogue Management System.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
