# Purpose of the project: Zoo database management system

# TESTING. The recommendation is to, at the very least, test each function
# three times.

import sqlite3

conn = sqlite3.connect("13th_november_version1_DMS/zoo.db")
cursor = conn.cursor()


class StaffAnimal:
    __staff_id = ""

    def __init__(self, staff_id):
        self.__staff_id = staff_id

    # Read all the animals that are the responsibility of the given staff, as identified by the 'staff_id'
    def read_staff_animals(self):
        try:
            sql = """
                SELECT animal.animal_id, animal_type.animal_type_name
                FROM staff_animal
                JOIN animal
                ON staff_animal.animal_id = animal.animal_id
                JOIN animal_type
                ON animal.animal_type_id = animal_type.animal_type_id
                WHERE staff_animal.staff_id = ?
            """

            cursor.execute(sql, (self.__staff_id,))
        except sqlite3.OperationalError as error:
            print("\nFailed to read staff_animal table", error)

        records = cursor.fetchall()
        for record in records:
            print(record)

        return True


# Represents 'staff' table
class Staff:

    # Add new staff to the 'staff' table
    #
    # :param new_staff: a TUPLE containing the information of the new staff member
    # :param animal_ids: a TUPLE containing the animal_id value of each animal, for which
    # the staff member is responsible
    def add_staff(self, new_staff, animal_ids):

        try:
            sql = """
                INSERT INTO staff(staff_name, seniority_level)
                VALUES(?, ?)
                """
            cursor.execute(sql, new_staff)

        except sqlite3.OperationalError as error:
            print("\nFailed to add record to the staff table", error)

        # Find the staff just added
        sql = """
            SELECT *
            FROM staff
            ORDER BY staff_id DESC LIMIT 1
        """

        cursor.execute(sql)

        newStaff = cursor.fetchone()

        # Create the necessary entries in the JOIN table
        # so that there is a connection between the staff and the animals they are responsible for
        try:
            for animal_id in animal_ids:
                sql = """
                    INSERT INTO staff_animal(staff_id, animal_id)
                    VALUES(?, ?)
                    """
                cursor.execute(sql, (newStaff[0], animal_id))

        except sqlite3.OperationalError as error:
            print("\nFailed to create record from the staff_animal table", error)

        print("\nSuccess! New Staff Added.")

        # Print the animals for which this staff member is responsible
        print(
            f"\n{newStaff[1]} with seniority level {newStaff[2]} is responsible for these animals:\n"
        )
        staffAnimal = StaffAnimal(newStaff[0])
        staffAnimal.read_staff_animals()

        return True

    # Print all the staff contained in the 'staff' table
    # to the console.
    # FORMAT is staff name, seniority level followed by all the animals for which they are responsible
    def select_all(self):

        try:
            sql = """
                SELECT staff_id, staff_name, seniority_level
                FROM staff
            """

            cursor.execute(sql)

            records = cursor.fetchall()
            for record in records:
                print(
                    f"\n{record[1]} with seniority level {record[2]} is responsible for these animals:\n"
                )

                staffAnimal = StaffAnimal(record[0])
                staffAnimal.read_staff_animals()

        except sqlite3.OperationalError as error:
            print("\nFailed to read records from the staff table", error)

        return True

    # Delete a staff member from the 'staff' table
    #
    # :param staff_id: A number: The ID identifying the 'staff' record to delete.
    def delete_staff(self, staff_id):
        try:
            sql = """
                DELETE FROM staff
                WHERE staff_id = ?
                """

            # Need comma at the end of round brackets: otherwise, Python will not recognise the value
            # as a TUPLE
            cursor.execute(sql, (staff_id,))

            # Need to also delete records from the JOIN table

            sql = """
                DELETE FROM staff_animal
                WHERE staff_id = ?
                """

            # Need comma at the end of round brackets: otherwise, Python will not recognise the value
            # as a TUPLE
            cursor.execute(sql, (staff_id,))

        except sqlite3.OperationalError as error:
            print("\nFailed to delete record from the animal table", error)

        print(f"\nstaff member of ID {staff_id} successfully deleted!")

        return True


# Represents 'animal' table
class Animal:

    # Add a new animal to the 'animal' table
    #
    # :param new_animal: a TUPLE containing the information of the new animal to add
    def add_animal(self, new_animal):

        try:
            sql = """
                INSERT INTO animal(animal_type_id, zoo_section_id)
                VALUES(?, ?)
                """
            cursor.execute(sql, new_animal)

            # Find the animal just added, and print it out
            sql = """
                SELECT animal.animal_id, animal_type.animal_type_name, zoo_section.zoo_section_name
                FROM animal
                JOIN animal_type
                ON animal.animal_type_id = animal_type.animal_type_id
                JOIN zoo_section
                ON animal.zoo_section_id = zoo_section.zoo_section_id
                ORDER BY animal.animal_id DESC LIMIT 1
            """

            cursor.execute(sql)

        except sqlite3.OperationalError as error:
            print("\nFailed to add record to the animal table", error)

        records = cursor.fetchall()

        print("\nSuccess! Animal added:")
        print(records[-1])

        return True

    # Print every animal record contained in the 'animal' table
    # to the console.
    # FORMAT: 1) animal ID. 2) animal_type_name. 3) zoo_section_name
    def select_all(self):

        try:
            sql = """
                SELECT animal.animal_id, animal_type.animal_type_name, zoo_section.zoo_section_name
                FROM animal
                JOIN animal_type
                ON animal.animal_type_id = animal_type.animal_type_id
                JOIN zoo_section
                ON animal.zoo_section_id = zoo_section.zoo_section_id
            """

            cursor.execute(sql)
        except sqlite3.OperationalError as error:
            print("Failed to read from the animal table", error)

        print("\nFORMAT: 1) animal ID. 2) animal_type_name. 3) zoo_section_name.")

        records = cursor.fetchall()
        for record in records:
            print(record)

        return True

    # Based on a user search query, print all the animals that matches the user search query,
    # searching on the animal_type_name field
    #
    # :param user_search: The user search field
    def search_for_animal(self, user_search):

        try:
            sql = """
                SELECT animal.animal_id, animal_type.animal_type_name, zoo_section.zoo_section_name
                FROM animal
                JOIN animal_type
                ON animal.animal_type_id = animal_type.animal_type_id
                JOIN zoo_section
                ON animal.zoo_section_id = zoo_section.zoo_section_id
                WHERE animal_type.animal_type_name LIKE '%{search}%'
            """.format(
                search=user_search
            )

            cursor.execute(sql)
        except sqlite3.OperationalError as error:
            print("Failed to read from the animal table", error)

        print("\nFORMAT: 1) animal ID. 2) animal_type_name. 3) zoo_section_name.")

        records = cursor.fetchall()
        for record in records:
            print(record)

        return True

    # Update an animal from the 'animal' table
    #
    # :param animal_id. A number: The ID identifying the 'animal' record to update.
    # :param animal_type_id. A number: The new 'animal_type_id' value.
    # :param zoo_section_id. A number: The new 'zoo_section_id' value.
    def update_animal(self, animal_id, animal_type_id, zoo_section_id):

        try:
            sql = """
                UPDATE animal
                SET animal_type_id = ?, zoo_section_id = ?
                WHERE animal_id = ?
                """
            cursor.execute(
                sql,
                (
                    animal_type_id,
                    zoo_section_id,
                    animal_id,
                ),
            )
        except sqlite3.OperationalError as error:
            print(
                f"\nFailed to update record {animal_id} from the animal table",
                error,
            )

        print(f"\nanimal of ID {animal_id} successfully updated!")

        return True

    # Delete an animal to the 'animal' table
    #
    # :param animal_id: A number: The ID identifying the 'animal' record to delete.
    def delete_animal(self, animal_id):

        try:
            sql = """
                DELETE FROM animal
                WHERE animal_id = ?
                """

            # Need comma at the end of round brackets: otherwise, Python will not recognise the value
            # as a TUPLE
            cursor.execute(sql, (animal_id,))
        except sqlite3.OperationalError as error:
            print("\nFailed to delete record from the animal table", error)

        print(f"\nanimal of ID {animal_id} successfully deleted!")

        return True


# Create table objects
animal = Animal()
staff = Staff()


# Presents Initial User Input and handles user response.
# Effectively the function that starts the application.
def initial_user_input():
    print("\nThe Options:")
    print("1) See all animals")
    print("2) Search for animal")
    print("3) Add an animal")
    print("4) Update an animal")
    print("5) Delete an animal")
    print("6) See all staff")
    print("7) Add a staff member")
    print("8) Delete a staff member")

    user_input = input(">")

    if user_input == "1":
        animal.select_all()
        print("\n\nWould you like to go back to the main menu? Y/N")

    elif user_input == "2":
        print("\nPlease search for an animal type: ")
        animal_type = input(">")
        animal.search_for_animal(animal_type)
        print("\n\nWould you like to go back to the main menu? Y/N")

    elif user_input == "3":
        print("\nPlease enter the animal type ID: ")
        animal_type_id = input(">")
        print("\nPlease enter the zoo section ID: ")
        zoo_section_id = input(">")

        new_animal = (animal_type_id, zoo_section_id)

        animal.add_animal(new_animal)

        print("\n\nWould you like to go back to the main menu? Y/N")

    elif user_input == "4":
        print("\nPlease enter the 'animal_id' of the animal to update: ")
        animal_id = input(">")
        print("\nPlease enter the updated animal type ID: ")
        animal_type_id = input(">")
        print("\nPlease enter the updated zoo section ID: ")
        zoo_section_id = input(">")

        animal.update_animal(animal_id, animal_type_id, zoo_section_id)

        print("\n\nWould you like to go back to the main menu? Y/N")

    elif user_input == "5":
        print("\nPlease enter the animal ID to delete ")
        animal_id = input(">")

        animal.delete_animal(animal_id)

        print("\n\nWould you like to go back to the main menu? Y/N")

    elif user_input == "6":
        staff.select_all()
        print("\n\nWould you like to go back to the main menu? Y/N")

    elif user_input == "7":
        print("\nPlease enter the staff name: ")
        staff_name = input(">")
        print("\nPlease enter the seniority level: ")
        seniority_level = input(">")
        print(
            "\nEnter a comma separated list of animal_ids for which the staff should be responsible: "
        )
        animal_ids = tuple(input(">").split(", "))

        new_staff = (staff_name, seniority_level)

        staff.add_staff(new_staff, animal_ids)

        print("\n\nWould you like to go back to the main menu? Y/N")

    elif user_input == "8":
        print("\nPlease enter the staff ID to delete ")
        staff_id = input(">")

        staff.delete_staff(staff_id)

        print("\n\nWould you like to go back to the main menu? Y/N")

    else:
        print("Sorry. Input could not be recognised.")
        print("\nWould you like to try again? Y/N")

    # Before ending the application, give the user a chance to repeat the application,
    # ie, go back to the main menu.
    prompt_user_repeat_user_input()

    return True


# Can repeat the application. The user response determines whether the user will quit the
# application or continue using it.
def prompt_user_repeat_user_input():
    user_input = input(">")

    if user_input.lower() == "Y".lower():
        initial_user_input()
    else:
        print("\nOK. Thank you for using the zoo DBS. Bye.")

    return True


def main():
    print(
        "Courtney Terminal [Version 42] \n(c) Courtney Corporation. All rights reserved."
    )
    print("======================================\n")
    print("WELCOME TO COURTNEY'S ZOO DATABASE MANAGEMENT SYSTEM")

    initial_user_input()

    return True


# Execute this code only when the file is executed as a script
if __name__ == "__main__":
    main()

    # Commit to data changes
    conn.commit()

    # Close the cursor object and the database connection
    cursor.close()
    conn.close()
