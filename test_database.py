import pytest
from challenge import StaffAnimal, Staff


# Test the 'StaffAnimal' class
class TestStaffAnimal:

    # :param capsys: pytest argument. Allows console output to be captured.
    def test_read(self, capsys):
        # Arrange
        staff_id = 1
        staff_animal = StaffAnimal(staff_id)

        # Act
        staff_animal.read_staff_animals()
        captured = capsys.readouterr()
        console_output = captured.out
        print(console_output)

        # Assert that console output is not NULL
        assert console_output.strip() != ""

    def test_invalid_read(self, capsys):
        # Arrange
        staff_id = "asdsadsad"
        staff_animal = StaffAnimal(staff_id)

        # Act
        staff_animal.read_staff_animals()
        captured = capsys.readouterr()
        console_output = captured.out

        # Assert that console output is NULL
        assert console_output.strip() == ""


# Test the 'Staff' class
class TestStaff:

    # :param capsys: pytest argument. Allows console output to be captured.
    def test_read(self, capsys):
        # Arrange
        staff = Staff()

        # Act
        staff.select_all()
        captured = capsys.readouterr()
        console_output = captured.out

        # Assert that console output is not NULL
        assert console_output.strip() != ""

        # :param capsys: pytest argument. Allows console output to be captured.

    def test_add(self, capsys):
        # Arrange
        staff = Staff()
        new_staff = ("Courtney Boy", 2)
        animal_ids = (1, 19, 30)

        # Get output before add
        staff.select_all()
        captured = capsys.readouterr()
        console_output = captured.out

        old_output_length = len(console_output.splitlines())

        # Act
        staff.add_staff(new_staff, animal_ids)

        # Get output after add
        staff.select_all()
        captured = capsys.readouterr()
        console_output = captured.out

        new_output_length = len(console_output.splitlines())

        # Assert
        assert new_output_length > old_output_length

    def test_delete(self, capsys):
        # Arrange
        staff = Staff()
        staff_id = 1

        # Get output before delete
        staff.select_all()
        captured = capsys.readouterr()
        console_output = captured.out

        old_output_length = len(console_output.splitlines())

        # Act
        staff.delete_staff(staff_id)

        # Get output after add
        staff.select_all()
        captured = capsys.readouterr()
        console_output = captured.out

        new_output_length = len(console_output.splitlines())

        # Assert
        assert new_output_length < old_output_length
