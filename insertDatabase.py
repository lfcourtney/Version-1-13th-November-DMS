import sqlite3

conn = sqlite3.connect("13th_november_version1_DMS/zoo.db")
cursor = conn.cursor()


"""
For a given SQL query that returns data, execute the query and
print each record

:param sql: The SQL query to return the data for
"""


def execute_and_print_sql(sql):
    cursor.execute(sql)

    records = cursor.fetchall()
    for record in records:
        print(record)

    # Print newline
    print("\n")
    return True


# Drop tables if they exist
sql = """
    DROP TABLE IF EXISTS zoo_section;
"""
cursor.execute(sql)

sql = """
    DROP TABLE IF EXISTS animal_type;
"""
cursor.execute(sql)

sql = """
    DROP TABLE IF EXISTS animal;
"""
cursor.execute(sql)

sql = """
    DROP TABLE IF EXISTS staff;
"""
cursor.execute(sql)

sql = """
    DROP TABLE IF EXISTS staff_animal;
"""
cursor.execute(sql)

# CREATE TABLE: zoo_section
# Has one to many relationship with animal table

sql = """
CREATE TABLE zoo_section(
    zoo_section_id INTEGER,
    zoo_section_name TEXT NOT NULL,
    square_metre REAL NOT NULL,
    PRIMARY KEY (zoo_section_id)
)
"""

cursor.execute(sql)

# INSERT records into 'zoo_section'
records = [
    (1, "Wild Aisa", 53.2),
    (2, "American Adventure", 25.26),
    (3, "African Foot Safari", 62.1),
    (4, "Woodland Walks", 75.2),
    (5, "Carnivore County", 34.71),
]

sql = """
INSERT INTO zoo_section VALUES(
    ?, ?, ?
)
"""

cursor.executemany(sql, records)


print("--zoo_section data--")

execute_and_print_sql(
    """
    SELECT * FROM zoo_section
"""
)


# CREATE TABLE: animal_type
# Has one to many relationship with animal table
sql = """
CREATE TABLE animal_type(
    animal_type_id INTEGER,
    animal_type_name TEXT NOT NULL,
    PRIMARY KEY (animal_type_id)
)
"""

cursor.execute(sql)

records = [
    (1, "Asiatic lion"),
    (2, "Sumatran tiger"),
    (3, "Western lowland gorilla"),
    (4, "Giraffe"),
    (5, "Pygmy hippo"),
    (6, "Linne's two-toed sloth"),
    (7, "Okapi"),
    (8, "Humboldt penguin"),
    (9, "Abdim's stork"),
    (10, "African bullfrog"),
    (11, "Alaotran gentle lemur"),
    (12, "Alpaca"),
]

sql = """
INSERT INTO animal_type VALUES(
    ?, ?
)
"""

cursor.executemany(sql, records)

print("--animal_type data--")

execute_and_print_sql(
    """
    SELECT * FROM animal_type
"""
)

# CREATE TABLE: animal

sql = """
CREATE TABLE animal(
    animal_id INTEGER,
    animal_type_id INTEGER,
    zoo_section_id INTEGER,
    PRIMARY KEY (animal_id),
    FOREIGN KEY (animal_type_id) REFERENCES animal_type(animal_type_id),
    FOREIGN KEY (zoo_section_id) REFERENCES zoo_section(zoo_section_id)
)
"""

cursor.execute(sql)

records = [
    # ID 1: Asiatic lion. ID 4: Woodland Walks
    (1, 1, 4),
    (2, 1, 4),
    (3, 1, 4),
    (4, 1, 4),
    # ID 2: Sumatran tiger. ID 1: Wild Asia
    (5, 2, 1),
    (6, 2, 1),
    # ID 3: Western lowland gorilla. ID 5: Carnivore County
    (7, 3, 5),
    (8, 3, 5),
    # ID 4: Giraffe. ID 3: African Foot Safari
    (9, 4, 5),
    (10, 4, 5),
    (11, 4, 5),
    (12, 4, 5),
    (13, 4, 5),
    # ID 5: Pygmy hippo. ID 2: American Adventure
    (14, 5, 2),
    (15, 5, 2),
    (16, 5, 2),
    (17, 5, 2),
    (18, 5, 2),
    # ID 6: Linne\'s two-toed sloth. ID 4: Woodland Walks
    (19, 6, 4),
    # ID 7: Okapi. ID 5: Carnivore County
    (20, 7, 5),
    (21, 7, 5),
    # ID 8: Humboldt penguin. ID 1: Wild Asia
    (22, 8, 1),
    (23, 8, 1),
    (24, 8, 1),
    # ID 9: Abdim\'s stork. ID 2: American Adventure
    (25, 9, 2),
    (26, 9, 2),
    (27, 9, 2),
    (28, 9, 2),
    (29, 9, 2),
    # ID 10: African bullfrog. ID 3: African Foot Safari
    (30, 10, 3),
    (31, 10, 3),
    (32, 10, 3),
    # ID 11: Alaotran gentle lemur. ID 5: Carnivore County
    (33, 11, 5),
    (34, 11, 5),
    # ID 12: Alpaca. ID 2: American Adventure
    (35, 12, 2),
    (36, 12, 2),
    (37, 12, 2),
    (38, 12, 2),
    (39, 12, 2),
    (40, 12, 2),
]

sql = """
INSERT INTO animal VALUES(
    ?, ?, ?
)
"""

cursor.executemany(sql, records)

print("--animal data--")

execute_and_print_sql(
    """
    SELECT * FROM animal
"""
)

# CREATE TABLE: staff
# Has many to many relationship with animal table.
# Hence, a JOIN TABLE is needed for this relationship ---
# to show which staff are responsible for which animals.
sql = """
CREATE TABLE staff(
    staff_id INTEGER,
    staff_name TEXT NOT NULL,
    seniority_level INTEGER NOT NULL,
    CHECK(seniority_level BETWEEN 1 AND 5),
    PRIMARY KEY (staff_id)
)
"""

cursor.execute(sql)

records = [
    (1, "Lanzo Nanabah", 5),
    (2, "Celestino Husain", 3),
    (3, "Dina Purity", 1),
    (4, "Anil Yasmeen", 4),
    (5, "Vilde Traian", 3),
    (6, "Aldhard Nikitha", 2),
    (7, "Tibor Genoveffa", 5),
    (8, "Verdandi Ramiz", 1),
    (9, "Monica Fergus", 2),
    (10, "Octavia Lavena", 4),
    (11, "Aelianus Roser", 5),
    (12, "Matthaios Kennedy", 2),
    (13, "Usha Baldev", 3),
    (14, "Cosme Itsasne", 4),
    (15, "Zarina Geroald", 2),
]

sql = """
INSERT INTO staff VALUES(
    ?, ?, ?
)
"""

cursor.executemany(sql, records)

print("--staff data--")

execute_and_print_sql(
    """
    SELECT * FROM staff
"""
)

# ========================
# Create Join Tables
# ========================

# Create JOIN TABLE for the many to many relationship
# between the 'staff' and 'animal' tables, showing which
# staff are responsible for which animals

sql = """
CREATE TABLE staff_animal(
    staff_id INTEGER,
    animal_id INTEGER,
    FOREIGN KEY (staff_id) REFERENCES staff(staff_id),
    FOREIGN KEY (animal_id) REFERENCES animal(animal_id)
)
"""

cursor.execute(sql)

records = [
    # Staff: Lanzo Nanabah
    (1, 1),
    (1, 19),
    (1, 30),
    (1, 5),
    # Staff: Celestino Hussain
    (2, 40),
    # Staff: Dina Purity
    (3, 30),
    (3, 34),
    (3, 11),
    # Staff: Anil Yaseem
    (4, 26),
    (4, 4),
    (4, 36),
    # Staff: Vilde Traian
    (5, 14),
    (5, 22),
    (5, 7),
    (5, 37),
    # Staff: Aldhard Nikitha
    (6, 9),
    (6, 16),
    (6, 31),
    # Staff: Tibor Genoveffa
    (7, 15),
    (7, 32),
    (7, 5),
    # Staff: Verdandi Ramiz
    (8, 27),
    (8, 30),
    (8, 3),
    # Staff: Monica Fergus
    (9, 28),
    (9, 35),
    (9, 33),
    (9, 6),
    # Staff: Octavia Lavena
    (10, 32),
    (10, 29),
    (10, 9),
    (10, 25),
    # Staff: Aelianus Roser
    (11, 21),
    (11, 24),
    (11, 39),
    (11, 20),
    # Staff: Matthaios Kennedy
    (12, 19),
    (12, 10),
    (12, 17),
    (12, 2),
    # Staff: Usha Baldev
    (13, 32),
    (13, 8),
    (13, 38),
    (13, 23),
    # Staff: Cosme Itsasne
    (14, 15),
    (14, 9),
    (14, 18),
    (14, 3),
    # Staff: Zarina Geroald
    (15, 13),
    (15, 29),
    (15, 3),
    (15, 15),
]

sql = """
INSERT INTO staff_animal VALUES(
    ?, ?
)
"""

cursor.executemany(sql, records)

print("--staff_animal data--")

execute_and_print_sql(
    """
    SELECT * FROM staff_animal
"""
)


# Commit to data changes
conn.commit()
