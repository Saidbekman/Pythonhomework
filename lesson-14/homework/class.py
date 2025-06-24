# Homework
# Task: JSON Parsing
# write a Python script that reads the students.jon JSON file and prints details of each student.
[
    {
        "id": 1,
        "name": "Ali Valiyev",
        "age": 21,
        "major": "Computer Science"
    },
    {
        "id": 2,
        "name": "Laylo Karimova",
        "age": 22,
        "major": "Economics"
    }
]

import json

# JSON faylni ochish va o'qish
with open('students.json', 'r', encoding='utf-8') as file:
    students = json.load(file)

# Har bir talabani ko'rsatish
for student in students:
    print("ID:", student.get("id"))
    print("Ism:", student.get("name"))
    print("Yosh:", student.get("age"))
    print("Mutaxassisligi:", student.get("major"))
    print("-" * 30)

# Task: Weather API
# Use this url : https://openweathermap.org/
# Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
import requests

# O'zingizning API kalitingizni shu yerga yozing
api_key = "YOUR_API_KEY"
city = "Tashkent"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# So'rov yuborish
response = requests.get(url)

# JSON formatdagi javobni olish
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    weather = data["weather"][0]["description"]
    wind_speed = data["wind"]["speed"]

    print(f"Shahar: {city}")
    print(f"Harorat: {temperature}°C")
    print(f"Namlik: {humidity}%")
    print(f"Ob-havo: {weather}")
    print(f"Shamol tezligi: {wind_speed} m/s")
else:
    print("Ma'lumotlarni olishda xatolik yuz berdi:", response.status_code)

# Task: JSON Modification
# Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
[
    {
        "id": 1,
        "title": "Python Basics",
        "author": "John Doe",
        "year": 2020
    }
]
import json
import os

FILE_NAME = 'books.json'

# Fayl mavjud bo'lmasa yaratish
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w') as f:
        json.dump([], f)

# JSON fayldan kitoblar ro'yxatini o'qish
def load_books():
    with open(FILE_NAME, 'r') as f:
        return json.load(f)

# JSON faylga saqlash
def save_books(books):
    with open(FILE_NAME, 'w') as f:
        json.dump(books, f, indent=4)

# Kitob qo'shish
def add_book():
    books = load_books()
    new_id = max([book["id"] for book in books], default=0) + 1
    title = input("Kitob nomi: ")
    author = input("Muallif: ")
    year = int(input("Yil: "))

    new_book = {
        "id": new_id,
        "title": title,
        "author": author,
        "year": year
    }
    books.append(new_book)
    save_books(books)
    print("✅ Kitob muvaffaqiyatli qo‘shildi.")

# Kitobni yangilash
def update_book():
    books = load_books()
    book_id = int(input("Yangilamoqchi bo‘lgan kitob ID raqamini kiriting: "))
    for book in books:
        if book["id"] == book_id:
            book["title"] = input(f"Yangi nomi ({book['title']}): ") or book["title"]
            book["author"] = input(f"Yangi muallifi ({book['author']}): ") or book["author"]
            year_input = input(f"Yangi yili ({book['year']}): ")
            book["year"] = int(year_input) if year_input else book["year"]
            save_books(books)
            print("✅ Kitob ma'lumotlari yangilandi.")
            return
    print("❌ Bunday IDga ega kitob topilmadi.")

# Kitobni o‘chirish
def delete_book():
    books = load_books()
    book_id = int(input("O‘chirmoqchi bo‘lgan kitob ID raqamini kiriting: "))
    books = [book for book in books if book["id"] != book_id]
    save_books(books)
    print("✅ Kitob o‘chirildi.")

# Kitoblar ro'yxatini ko‘rsatish
def show_books():
    books = load_books()
    if not books:
        print("📚 Kitoblar ro'yxati bo‘sh.")
    for book in books:
        print(f"ID: {book['id']} | Nomi: {book['title']} | Muallif: {book['author']} | Yil: {book['year']}")

# Menyu
def main():
    while True:
        print("\n----- Kitoblar Bazasini Boshqarish -----")
        print("1. Kitob qo‘shish")
        print("2. Kitobni yangilash")
        print("3. Kitobni o‘chirish")
        print("4. Barcha kitoblarni ko‘rish")
        print("5. Chiqish")
        choice = input("Tanlang (1-5): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            show_books()
        elif choice == '5':
            print("Dastur tugadi.")
            break
        else:
            print("❌ Noto‘g‘ri tanlov!")

if __name__ == "__main__":
    main()

