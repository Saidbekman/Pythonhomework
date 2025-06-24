# Review Exercises
# Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.
import sqlite3

# Ma'lumotlar bazasini yaratish yoki unga ulanish
conn = sqlite3.connect('zoo.db')  # fayl nomi: zoo.db
cursor = conn.cursor()

# Roster jadvalini yaratish
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
''')

# O'zgarishlarni saqlash va ulanishni yopish
conn.commit()
conn.close()

print("✅ 'Roster' jadvali yaratildi yoki mavjud bo‘lsa, o‘zgartirilmadi.")

# Populate your new table with the following values:

# Name	Species	Age
# Benjamin Sisko	Human	40
# Jadzia Dax	Trill	300
# Kira Nerys	Bajoran	29
import sqlite3

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('zoo.db')
cursor = conn.cursor()

# Roster jadvaliga ma'lumotlar qo'shish
data = [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
]

cursor.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', data)

# O'zgarishlarni saqlash va ulanishni yopish
conn.commit()
conn.close()

print("✅ Ma'lumotlar Roster jadvaliga muvaffaqiyatli qo'shildi.")

# Update the Name of Jadzia Dax to be Ezri Dax
import sqlite3

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('zoo.db')
cursor = conn.cursor()

# Ismni yangilash: Jadzia Dax -> Ezri Dax
cursor.execute('''
    UPDATE Roster
    SET Name = ?
    WHERE Name = ?
''', ("Ezri Dax", "Jadzia Dax"))

# O'zgarishlarni saqlash va ulanishni yopish
conn.commit()
conn.close()

print("✅ 'Jadzia Dax' ismi 'Ezri Dax' ga yangilandi.")

conn = sqlite3.connect('zoo.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM Roster')
for row in cursor.fetchall():
    print(row)

conn.close()

# Display the Name and Age of everyone in the table classified as Bajoran.
import sqlite3

# Ma'lumotlar bazasiga ulanish
conn = sqlite3.connect('zoo.db')
cursor = conn.cursor()

# Species = 'Bajoran' bo'lganlarni tanlash
cursor.execute('''
    SELECT Name, Age
    FROM Roster
    WHERE Species = ?
''', ("Bajoran",))

# Natijalarni chiqarish
results = cursor.fetchall()
for name, age in results:
    print(f"Ism: {name}, Yosh: {age}")

# Ulashishni yopish
conn.close()
