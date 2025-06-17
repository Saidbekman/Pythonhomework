# Homework:
# Age Calculator: Ask the user to enter their birthdate. Calculate and print their age in years, months, and days.
import datetime
def yosh_aniqlash():
    try:
        foydalanuvchi_yoshi = input("Belgilangan tartibda sana kiriting ({kun}-{oy}-{yil}): ").strip()
        if not foydalanuvchi_yoshi:
            print("Ma'lumot to'g'ri kiritilmagan. Mos ravishda kiriting.")
            return
        sana = datetime.datetime.strptime(foydalanuvchi_yoshi, "%d-%m-%Y").date()
        bugun = datetime.date.today()
        yosh = bugun.year - sana.year
        oy = bugun.month - sana.month
        kun = bugun.day - sana.day
        if kun < 0:
            oy -= 1
            oldingi_oy = bugun.replace(day=1) - datetime.timedelta(days=1)
            kun += oldingi_oy.day
        if oy < 0:
            yosh -= 1
            oy += 12
        print(f"Sizning yashagan vaqtingiz {yosh} yosh, {oy} oy, {kun} kun bo'ladi!")
    except Exception as e:
        print("Jarayonda xatolik bor:", e)
yosh_aniqlash()

# Days Until Next Birthday: Similar to the first exercise, but this time, calculate and print the number of days remaining until the user's next birthday.
def tugilgan_kungacha_qolgan_kunlar():
    try:
        sana_str = input("Tug'ilgan kuningizni kiriting (kun-oy-yil): ").strip()
        if not sana_str:
            print("Ma'lumot to'g'ri kiritilmadi.")
            return

        tugilgan_sana = datetime.datetime.strptime(sana_str, "%d-%m-%Y").date()
        bugun = datetime.date.today()

        bu_yilgi_tugilgan_kun = datetime.date(bugun.year, tugilgan_sana.month, tugilgan_sana.day)
        
        if bu_yilgi_tugilgan_kun < bugun:
            keyingi_tugilgan_kun = datetime.date(bugun.year + 1, tugilgan_sana.month, tugilgan_sana.day)
        else:
            keyingi_tugilgan_kun = bu_yilgi_tugilgan_kun

        qolgan_kunlar = (keyingi_tugilgan_kun - bugun).days

        print(f"Keyingi tug'ilgan kuningizgacha {qolgan_kunlar} kun qoldi.")

    except Exception as e:
        print("Xatolik yuz berdi:", e)

tugilgan_kungacha_qolgan_kunlar()

# Meeting Scheduler: Ask the user to enter the current date and time, as well as the duration of a meeting in hours and minutes. Calculate and print the date and time when the meeting will end.
def uchrashuv_rejalashtiruvchi():
    try:
        boshlanish_str = input("Uchrashuv boshlanish sanasi va vaqtini kiriting (dd-mm-yyyy HH:MM): ").strip()
        boshlanish_vaqti = datetime.datetime.strptime(boshlanish_str, "%d-%m-%Y %H:%M")
        soat = int(input("Uchrashuv davomiyligini kiriting (soat): ").strip())
        daqiqa = int(input("Uchrashuv davomiyligini kiriting (daqiqa): ").strip())
        davomiylik = datetime.timedelta(hours=soat, minutes=daqiqa)
        tugash_vaqti = boshlanish_vaqti + davomiylik
        print(f"Uchrashuv {boshlanish_vaqti.strftime('%d-%m-%Y %H:%M')} da boshlanadi.")
        print(f"Uchrashuv {tugash_vaqti.strftime('%d-%m-%Y %H:%M')} da tugaydi.")
    except Exception as e:
        print("Xatolik yuz berdi:", e)
uchrashuv_rejalashtiruvchi()

# Timezone Converter: Create a program that allows the user to enter a date and time along with their current timezone, and then convert and print the date and time in another timezone of their choice.
import datetime
import pytz
def timezone_converter():
    try:
        dt_str = input("Sana va vaqtni kiriting (dd-mm-yyyy HH:MM): ").strip()
        dt_naive = datetime.datetime.strptime(dt_str, "%d-%m-%Y %H:%M")

        current_tz_str = input("Hozirgi vaqt zonangizni kiriting (masalan: Asia/Tashkent): ").strip()
        current_tz = pytz.timezone(current_tz_str)
        dt_local = current_tz.localize(dt_naive)

        target_tz_str = input("O'zgartirmoqchi bo'lgan vaqt zonangizni kiriting (masalan: Europe/London): ").strip()
        target_tz = pytz.timezone(target_tz_str)

        dt_converted = dt_local.astimezone(target_tz)

        print(f"\nSiz kiritgan vaqt ({current_tz_str}): {dt_local.strftime('%d-%m-%Y %H:%M')}")
        print(f"O'zgartirilgan vaqt ({target_tz_str}): {dt_converted.strftime('%d-%m-%Y %H:%M')}")

    except Exception as e:
        print("Xatolik yuz berdi:", e)

timezone_converter()

# Countdown Timer: Implement a countdown timer. Ask the user to input a future date and time, and then continuously print the time remaining until that point in regular intervals (e.g., every second).
import datetime
import time
import sys
def countdown_timer():
    try:
        deadline_str = input("Kelajakdagi sana va vaqtni kiriting (dd-mm-yyyy HH:MM:SS): ").strip()
        deadline = datetime.datetime.strptime(deadline_str, "%d-%m-%Y %H:%M:%S")

        print("\nCountdown boshlanmoqda...\n")

        while True:
            hozir = datetime.datetime.now()
            farq = deadline - hozir

            if farq.total_seconds() <= 0:
                print("\n⏰ Taymer tugadi!")
                break

            kun = farq.days
            soat, qoldiq = divmod(farq.seconds, 3600)
            daqiqa, soniya = divmod(qoldiq, 60)

            sys.stdout.write(f"\rQolgan vaqt: {kun} kun, {soat:02d}:{daqiqa:02d}:{soniya:02d}")
            sys.stdout.flush()

            time.sleep(1)

    except Exception as e:
        print("Xatolik yuz berdi:", e)

countdown_timer()

# Email Validator: Write a program that validates email addresses. Ask the user to input an email address, and check if it follows a valid email format.
import re
def email_validator():
    email = input("Email manzilini kiriting: ").strip()

    # Oddiy email andozasi (regex)
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if re.match(pattern, email):
        print("✅ Email formati to‘g‘ri.")
    else:
        print("❌ Email formati noto‘g‘ri.")

email_validator()

# Phone Number Formatter: Create a program that takes a phone number as input and formats it according to a standard format. For example, convert "1234567890" to "(123) 456-7890".
def phone_number_formatter():
    raqam = input("Telefon raqamingizni faqat raqamlardan iborat qilib kiriting (masalan: 1234567890): ").strip()

    # Faqat 10 ta raqam bo'lishi kerak
    if len(raqam) == 10 and raqam.isdigit():
        formatlangan = f"({raqam[:3]}) {raqam[3:6]}-{raqam[6:]}"
        print("Formatlangan raqam:", formatlangan)
    else:
        print("❌ Noto‘g‘ri format. Iltimos, faqat 10 ta raqam kiriting.")

phone_number_formatter()

# Password Strength Checker: Implement a password strength checker. Ask the user to input a password and check if it meets certain criteria (e.g., minimum length, contains at least one uppercase letter, one lowercase letter, and one digit).
import re

def password_strength_checker():
    password = input("Parolni kiriting: ").strip()

    uzunlik = len(password) >= 8
    katta_harf = re.search(r"[A-Z]", password)
    kichik_harf = re.search(r"[a-z]", password)
    raqam = re.search(r"\d", password)
    maxsus_belgi = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if all([uzunlik, katta_harf, kichik_harf, raqam]):
        if maxsus_belgi:
            print("✅ Kuchli parol (strong)!")
        else:
            print("⚠️ Yaxshi parol, lekin maxsus belgi yo'q.")
    else:
        print("❌ Parol zaif. Talablar:")
        if not uzunlik:
            print("- Kamida 8 ta belgi bo‘lishi kerak.")
        if not katta_harf:
            print("- Kamida 1 ta katta harf kerak (A-Z).")
        if not kichik_harf:
            print("- Kamida 1 ta kichik harf kerak (a-z).")
        if not raqam:
            print("- Kamida 1 ta raqam kerak (0-9).")

password_strength_checker()

# Word Finder: Develop a program that finds all occurrences of a specific word in a given text. Ask the user to input a word, and then search for and print all occurrences of that word in a sample text.
def word_finder():
    # Misol matn
    matn = """
    Python is a powerful programming language. Many people learn Python because it is simple and effective.
    Python is used in data science, web development, automation, and more.
    """
    soz = input("Qidirilayotgan so‘zni kiriting: ").strip()

    if not soz:
        print("❌ So‘z kiritilmadi.")
        return
    matn_lower = matn.lower()
    soz_lower = soz.lower()

    soni = matn_lower.count(soz_lower)

    indekslar = []
    start = 0
    while True:
        idx = matn_lower.find(soz_lower, start)
        if idx == -1:
            break
        indekslar.append(idx)
        start = idx + len(soz_lower)

    if soni > 0:
        print(f"\n✅ \"{soz}\" so‘zi matnda {soni} marta uchradi.")
        print("📍 Joylashgan indekslar:", indekslar)
    else:
        print(f"\n🔍 \"{soz}\" so‘zi matnda topilmadi.")

word_finder()

# Date Extractor: Write a program that extracts dates from a given text. Ask the user to input a text, and then identify and print all the dates present in the text.
import re

def date_extractor():
    text = input("Matnni kiriting (sanalari bilan birga):\n").strip()
    pattern = r'\b\d{2}[-/.]\d{2}[-/.]\d{4}\b'
    sanalar = re.findall(pattern, text)
    if sanalar:
        print(f"\n✅ Matndan topilgan sanalar ({len(sanalar)} ta):")
        for sana in sanalar:
            print(f"📅 {sana}")
    else:
        print("\n❌ Matnda sana topilmadi.")

date_extractor()
