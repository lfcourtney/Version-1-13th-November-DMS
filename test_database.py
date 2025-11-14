import pytest
from challenge import StaffAnimal


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
