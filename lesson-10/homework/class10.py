# Homework Projects:
# Homework 1. ToDo List Application
# 1. Define Task Class:
# Create a Task class with attributes such as task title, description, due date, and status.
class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title                
        self.description = description    
        self.due_date = due_date          
        self.status = status              

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Status: {self.status}\n")
task1 = Task(
    title="Python darsini o'rganish",
    description="Python klasslar mavzusini o'zlashtirish",
    due_date="2025-06-10"
)

print(task1)

# 2. Define ToDoList Class:
# Create a ToDoList class that manages a list of tasks.
# Include methods to add a task, mark a task as complete, list all tasks, and display incomplete tasks.
class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = "Completed"

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Status: {self.status}\n")


class ToDoList:
    def __init__(self):
        self.tasks = []   

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
        else:
            print("Noto'g'ri indeks!")

    def list_all_tasks(self):
        if not self.tasks:
            print("Vazifalar yo'q!")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}. {task}")

    def display_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status != "Completed"]
        if not incomplete:
            print("Bajarilmagan vazifalar yo'q!")
        for i, task in enumerate(incomplete, start=1):
            print(f"{i}. {task}")
todo = ToDoList()
task1 = Task("Python darsini o'rganish", "Klasslar mavzusini o'zlashtirish", "2025-06-10")
task2 = Task("Uy vazifasini bajarish", "5 ta masalani yechish", "2025-06-11")

todo.add_task(task1)
todo.add_task(task2)

print("Barcha vazifalar:")
todo.list_all_tasks()

print("Bajarilmagan vazifalar:")
todo.display_incomplete_tasks()
todo.mark_task_complete(0)

print("Barcha vazifalar (yangilangan):")
todo.list_all_tasks()

# 3. Create Main Program:
# Develop a simple CLI to interact with the ToDoList.
# Include options to add tasks, mark tasks as complete, list all tasks, and display only incomplete tasks.
class Task:
    def __init__(self, title, description, due_date, status="Pending"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        self.status = "Completed"

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Description: {self.description}\n"
                f"Due Date: {self.due_date}\n"
                f"Status: {self.status}\n")


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print("Vazifa bajarildi!")
        else:
            print("Noto'g'ri indeks!")

    def list_all_tasks(self):
        if not self.tasks:
            print("Vazifalar yo'q!")
        for i, task in enumerate(self.tasks, start=1):
            print(f"{i}.\n{task}")

    def display_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if task.status != "Completed"]
        if not incomplete:
            print("Bajarilmagan vazifalar yo'q!")
        for i, task in enumerate(incomplete, start=1):
            print(f"{i}.\n{task}")

def main():
    todo = ToDoList()
    while True:
        print("\n===== ToDo List Dasturi =====")
        print("1. Vazifa qo'shish")
        print("2. Vazifani bajarildi deb belgilash")
        print("3. Barcha vazifalarni ko‘rish")
        print("4. Faqat bajarilmagan vazifalarni ko‘rish")
        print("5. Chiqish")

        tanlov = input("Tanlovingizni kiriting (1-5): ")
        if tanlov == '1':
            title = input("Vazifa nomi: ")
            description = input("Tavsifi: ")
            due_date = input("Tugash sanasi (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo.add_task(task)
            print("Vazifa qo'shildi!")
        elif tanlov == '2':
            todo.list_all_tasks()
            idx = input("Qaysi vazifa bajarildi? (raqamini kiriting): ")
            if idx.isdigit():
                todo.mark_task_complete(int(idx)-1)
            else:
                print("Raqam kiriting!")
        elif tanlov == '3':
            todo.list_all_tasks()
        elif tanlov == '4':
            todo.display_incomplete_tasks()
        elif tanlov == '5':
            print("Dastur yakunlandi.")
            break
        else:
            print("Noto'g'ri tanlov!")

if __name__ == "__main__":
    main()

# 4. Test the Application:
# Create instances of tasks and test the functionality of your ToDoList.
# Avval Task va ToDoList klasslari oldingi kodlardek bo‘lishi kerak.

# Test qilish uchun kod:
def test_todolist():
    todo = ToDoList()
    task1 = Task("Python o‘rganish", "Klasslar va obyektlar", "2025-06-10")
    task2 = Task("Uyga vazifa", "3 ta masala yechish", "2025-06-12")
    task3 = Task("Do‘stga qo‘ng‘iroq qilish", "Ahvol so‘rash", "2025-06-11")
    todo.add_task(task1)
    todo.add_task(task2)
    todo.add_task(task3)
    print("1. Barcha vazifalar:")
    todo.list_all_tasks()
    todo.mark_task_complete(0)
    todo.mark_task_complete(2)
    print("\n2. Barcha vazifalar (yangilangan holat):")
    todo.list_all_tasks()
    print("\n3. Faqat bajarilmagan vazifalar:")
    todo.display_incomplete_tasks()
test_todolist()


# Homework 2. Simple Blog System
# 1. Define Post Class:
# Create a Post class with attributes like title, content, and author.
class Post:
    def __init__(self, title, content, author):
        self.title = title        
        self.content = content    
        self.author = author      

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Content: {self.content}\n"
                f"Author: {self.author}\n")
post1 = Post("Yangi Python darsi", "Bugun biz klasslar mavzusini o‘rganamiz.", "Saidbek")
print(post1)

# 2. Define Blog Class:
# Create a Blog class that manages a list of posts.
# Include methods to add a post, list all posts, and display posts by a specific author.
class Blog:
    def __init__(self):
        self.posts = []  

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("Hech qanday post yo'q!")
        for i, post in enumerate(self.posts, start=1):
            print(f"{i}.\n{post}")

    def display_posts_by_author(self, author):
        found = False
        for i, post in enumerate(self.posts, start=1):
            if post.author == author:
                print(f"{i}.\n{post}")
                found = True
        if not found:
            print(f"{author} tomonidan hech qanday post topilmadi.")
if __name__ == "__main__":
    blog = Blog()
    post1 = Post("Klasslar haqida", "OOP va klasslar juda muhim.", "Saidbek")
    post2 = Post("Python darsi", "Bugun Python'da funksiya yozamiz.", "Dilorom")
    post3 = Post("Blog yangiligi", "Yangi mavzu qo'shildi.", "Saidbek")

    blog.add_post(post1)
    blog.add_post(post2)
    blog.add_post(post3)

    print("Barcha postlar:")
    blog.list_all_posts()

    print("\nMuallif: Saidbek postlari:")
    blog.display_posts_by_author("Saidbek")

# 3. Create Main Program:
# Develop a CLI to interact with the Blog system.
# Include options to add posts, list all posts, and display posts by a specific author.
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Content: {self.content}\n"
                f"Author: {self.author}\n")


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("Hech qanday post yo'q!")
        for i, post in enumerate(self.posts, start=1):
            print(f"{i}.\n{post}")

    def display_posts_by_author(self, author):
        found = False
        for i, post in enumerate(self.posts, start=1):
            if post.author == author:
                print(f"{i}.\n{post}")
                found = True
        if not found:
            print(f"{author} tomonidan hech qanday post topilmadi.")


def main():
    blog = Blog()
    while True:
        print("\n==== Blog tizimi ====")
        print("1. Yangi post qoʻshish")
        print("2. Barcha postlarni koʻrish")
        print("3. Muallif bo‘yicha postlarni chiqarish")
        print("4. Chiqish")

        choice = input("Tanlovingizni kiriting (1-4): ")
        if choice == '1':
            title = input("Post sarlavhasi: ")
            content = input("Post matni: ")
            author = input("Muallif: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post muvaffaqiyatli qoʻshildi!")
        elif choice == '2':
            print("\nBarcha postlar:")
            blog.list_all_posts()
        elif choice == '3':
            author = input("Muallif ismini kiriting: ")
            print(f"\n{author} tomonidan yozilgan postlar:")
            blog.display_posts_by_author(author)
        elif choice == '4':
            print("Dastur yakunlandi.")
            break
        else:
            print("Noto'g'ri tanlov! Qayta urinib ko‘ring.")

if __name__ == "__main__":
    main()

# 4. Enhance Blog System:
# Add functionality to delete a post, edit a post, and display the latest posts.
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Content: {self.content}\n"
                f"Author: {self.author}\n")


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        if not self.posts:
            print("Hech qanday post yo'q!")
        for i, post in enumerate(self.posts, start=1):
            print(f"{i}.\n{post}")

    def display_posts_by_author(self, author):
        found = False
        for i, post in enumerate(self.posts, start=1):
            if post.author == author:
                print(f"{i}.\n{post}")
                found = True
        if not found:
            print(f"{author} tomonidan hech qanday post topilmadi.")

    def delete_post(self, index):
        if 0 <= index < len(self.posts):
            deleted_post = self.posts.pop(index)
            print(f"Post '{deleted_post.title}' o‘chirildi.")
        else:
            print("Noto‘g‘ri indeks!")

    def edit_post(self, index, new_title=None, new_content=None, new_author=None):
        if 0 <= index < len(self.posts):
            if new_title:
                self.posts[index].title = new_title
            if new_content:
                self.posts[index].content = new_content
            if new_author:
                self.posts[index].author = new_author
            print("Post muvaffaqiyatli tahrirlandi.")
        else:
            print("Noto‘g‘ri indeks!")

    def display_latest_posts(self, count=3):
        if not self.posts:
            print("Hech qanday post yo‘q!")
            return
        print(f"So‘nggi {min(count, len(self.posts))} ta post:")
        for i, post in enumerate(self.posts[-count:], start=1):
            print(f"{i}.\n{post}")

def main():
    blog = Blog()
    while True:
        print("\n==== Blog tizimi ====")
        print("1. Yangi post qoʻshish")
        print("2. Barcha postlarni koʻrish")
        print("3. Muallif bo‘yicha postlarni chiqarish")
        print("4. Postni o‘chirish")
        print("5. Postni tahrirlash")
        print("6. So‘nggi postlarni ko‘rish")
        print("7. Chiqish")

        choice = input("Tanlovingizni kiriting (1-7): ")
        if choice == '1':
            title = input("Post sarlavhasi: ")
            content = input("Post matni: ")
            author = input("Muallif: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post muvaffaqiyatli qoʻshildi!")
        elif choice == '2':
            print("\nBarcha postlar:")
            blog.list_all_posts()
        elif choice == '3':
            author = input("Muallif ismini kiriting: ")
            print(f"\n{author} tomonidan yozilgan postlar:")
            blog.display_posts_by_author(author)
        elif choice == '4':
            blog.list_all_posts()
            idx = input("Qaysi postni o‘chirmoqchisiz? (raqamini kiriting): ")
            if idx.isdigit():
                blog.delete_post(int(idx)-1)
            else:
                print("Raqam kiriting!")
        elif choice == '5':
            blog.list_all_posts()
            idx = input("Qaysi postni tahrirlamoqchisiz? (raqamini kiriting): ")
            if idx.isdigit():
                idx_int = int(idx) - 1
                new_title = input("Yangi sarlavha (qoldirish uchun Enter bosing): ")
                new_content = input("Yangi matn (qoldirish uchun Enter bosing): ")
                new_author = input("Yangi muallif (qoldirish uchun Enter bosing): ")
                blog.edit_post(
                    idx_int,
                    new_title if new_title else None,
                    new_content if new_content else None,
                    new_author if new_author else None
                )
            else:
                print("Raqam kiriting!")
        elif choice == '6':
            cnt = input("Nechta so‘nggi postni ko‘rsatamiz? (default 3): ")
            if cnt.isdigit():
                blog.display_latest_posts(int(cnt))
            else:
                blog.display_latest_posts()
        elif choice == '7':
            print("Dastur yakunlandi.")
            break
        else:
            print("Noto'g'ri tanlov! Qayta urinib ko‘ring.")

if __name__ == "__main__":
    main()

# 5. Test the Application:
# Create instances of posts and test the functionality of your Blog system.
# Avval Post va Blog klasslari yuqoridagidek bo‘lishi kerak.

def test_blog_system():
    blog = Blog()
    post1 = Post("Python OOP", "Klass va obyektlar haqida", "Saidbek")
    post2 = Post("Dasturlash Asoslari", "Oson if-else misollari", "Dilorom")
    post3 = Post("CLI dastur", "ToDo va Blog tizimi uchun CLI", "Saidbek")
    post4 = Post("Yangilik", "Python 3.12 chiqdi!", "Dilorom")

    blog.add_post(post1)
    blog.add_post(post2)
    blog.add_post(post3)
    blog.add_post(post4)

    print("1. Barcha postlar:")
    blog.list_all_posts()
    print("\n2. Saidbek tomonidan yozilgan postlar:")
    blog.display_posts_by_author("Saidbek")
    print("\n3. Ikkinchi postni o‘chirish:")
    blog.delete_post(1)
    blog.list_all_posts()
    print("\n4. Birinchi postni tahrirlash:")
    blog.edit_post(0, new_title="Python OOP Yangilandi", new_content="Yangilangan mazmun", new_author="Bekzod")
    blog.list_all_posts()
    print("\n5. So‘nggi 2 ta post:")
    blog.display_latest_posts(2)
test_blog_system()


# Homework 3. Simple Banking System
# 1. Define Account Class:
# Create an Account class with attributes like account number, account holder name, and balance.
class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number      
        self.account_holder = account_holder      
        self.balance = balance                    
    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Balance: {self.balance:.2f}")
acc1 = Account("0011223344", "Saidbek Sobirov", 150000)
print(acc1)

# 2. Define Bank Class:
# Create a Bank class that manages a list of accounts.
# Include methods to add an account, check balance, deposit money, and withdraw money.
class Bank:
    def __init__(self):
        self.accounts = []  # Hisoblar ro‘yxati

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Hisob raqami {account.account_number} muvaffaqiyatli qo'shildi!")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f"Balans: {account.balance:.2f}")
        else:
            print("Hisob topilmadi!")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                print(f"{amount:.2f} so'm muvaffaqiyatli qo'shildi!")
            else:
                print("Yaroqsiz summa!")
        else:
            print("Hisob topilmadi!")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            if amount > 0 and account.balance >= amount:
                account.balance -= amount
                print(f"{amount:.2f} so'm muvaffaqiyatli yechildi!")
            elif amount > 0:
                print("Yetarli mablag' yo'q!")
            else:
                print("Yaroqsiz summa!")
        else:
            print("Hisob topilmadi!")
if __name__ == "__main__":
    bank = Bank()
    acc1 = Account("1001", "Saidbek", 50000)
    acc2 = Account("1002", "Dilorom", 100000)

    bank.add_account(acc1)
    bank.add_account(acc2)

    bank.check_balance("1001")
    bank.deposit("1001", 20000)
    bank.check_balance("1001")
    bank.withdraw("1001", 50000)
    bank.check_balance("1001")
    bank.withdraw("1001", 500000)  

# 3. Create Main Program:
# Develop a CLI to interact with the Banking system.
# Include options to add accounts, check balance, deposit money, and withdraw money.
class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Balance: {self.balance:.2f}")

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Hisob raqami {account.account_number} muvaffaqiyatli qo'shildi!")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f"Balans: {account.balance:.2f} so'm")
        else:
            print("Hisob topilmadi!")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                print(f"{amount:.2f} so'm muvaffaqiyatli qo'shildi!")
            else:
                print("Yaroqsiz summa!")
        else:
            print("Hisob topilmadi!")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            if amount > 0 and account.balance >= amount:
                account.balance -= amount
                print(f"{amount:.2f} so'm muvaffaqiyatli yechildi!")
            elif amount > 0:
                print("Yetarli mablag' yo'q!")
            else:
                print("Yaroqsiz summa!")
        else:
            print("Hisob topilmadi!")

def main():
    bank = Bank()
    while True:
        print("\n===== Bank Tizimi =====")
        print("1. Hisob qo'shish")
        print("2. Balansni ko'rish")
        print("3. Hisobga pul qo'yish")
        print("4. Hisobdan pul yechish")
        print("5. Chiqish")

        tanlov = input("Tanlovingizni kiriting (1-5): ")
        if tanlov == '1':
            acc_num = input("Hisob raqami: ")
            acc_holder = input("Hisob egasi: ")
            balance_input = input("Boshlang'ich balans (standart 0): ")
            if balance_input.strip() == "":
                balance = 0.0
            else:
                try:
                    balance = float(balance_input)
                except:
                    print("Yaroqsiz balans! 0 qilib o'rnatildi.")
                    balance = 0.0
            account = Account(acc_num, acc_holder, balance)
            bank.add_account(account)
        elif tanlov == '2':
            acc_num = input("Hisob raqamini kiriting: ")
            bank.check_balance(acc_num)
        elif tanlov == '3':
            acc_num = input("Hisob raqamini kiriting: ")
            try:
                amount = float(input("Qo'yiladigan summa: "))
            except:
                print("Yaroqsiz summa!")
                continue
            bank.deposit(acc_num, amount)
        elif tanlov == '4':
            acc_num = input("Hisob raqamini kiriting: ")
            try:
                amount = float(input("Yechiladigan summa: "))
            except:
                print("Yaroqsiz summa!")
                continue
            bank.withdraw(acc_num, amount)
        elif tanlov == '5':
            print("Dastur yakunlandi.")
            break
        else:
            print("Noto'g'ri tanlov!")

if __name__ == "__main__":
    main()

# 4. Enhance Banking System:
# Add functionality to transfer money between accounts, display account details, and handle account overdrafts.
class Account:
    def __init__(self, account_number, account_holder, balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def __str__(self):
        return (f"Account Number: {self.account_number}\n"
                f"Account Holder: {self.account_holder}\n"
                f"Balance: {self.balance:.2f} so'm")

class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Hisob raqami {account.account_number} muvaffaqiyatli qo'shildi!")

    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def check_balance(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(f"Balans: {account.balance:.2f} so'm")
        else:
            print("Hisob topilmadi!")

    def display_account_details(self, account_number):
        account = self.find_account(account_number)
        if account:
            print(account)
        else:
            print("Hisob topilmadi!")

    def deposit(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            if amount > 0:
                account.balance += amount
                print(f"{amount:.2f} so'm muvaffaqiyatli qo'shildi!")
            else:
                print("Yaroqsiz summa!")
        else:
            print("Hisob topilmadi!")

    def withdraw(self, account_number, amount):
        account = self.find_account(account_number)
        if account:
            if amount > 0:
                account.balance -= amount
                if account.balance < 0:
                    print(f"Diqqat! Hisobda pul yetarli emas, overdraft holatida. Balans: {account.balance:.2f} so'm")
                else:
                    print(f"{amount:.2f} so'm muvaffaqiyatli yechildi!")
            else:
                print("Yaroqsiz summa!")
        else:
            print("Hisob topilmadi!")

    def transfer(self, from_acc_num, to_acc_num, amount):
        from_acc = self.find_account(from_acc_num)
        to_acc = self.find_account(to_acc_num)
        if not from_acc:
            print("Jo'natuvchi hisob topilmadi!")
            return
        if not to_acc:
            print("Qabul qiluvchi hisob topilmadi!")
            return
        if amount <= 0:
            print("Yaroqsiz summa!")
            return
        from_acc.balance -= amount
        to_acc.balance += amount
        if from_acc.balance < 0:
            print(f"Diqqat! {from_acc_num} hisob overdraft holatida. Balans: {from_acc.balance:.2f} so'm")
        print(f"{amount:.2f} so'm {from_acc_num} hisobdan {to_acc_num} hisobga muvaffaqiyatli o‘tkazildi.")

def main():
    bank = Bank()
    while True:
        print("\n===== Bank Tizimi =====")
        print("1. Hisob qo'shish")
        print("2. Balansni ko'rish")
        print("3. Hisobga pul qo'yish")
        print("4. Hisobdan pul yechish")
        print("5. Pul o‘tkazish (hisobdan hisobga)")
        print("6. Hisob tafsilotlarini ko‘rsatish")
        print("7. Chiqish")

        tanlov = input("Tanlovingizni kiriting (1-7): ")
        if tanlov == '1':
            acc_num = input("Hisob raqami: ")
            acc_holder = input("Hisob egasi: ")
            balance_input = input("Boshlang'ich balans (standart 0): ")
            if balance_input.strip() == "":
                balance = 0.0
            else:
                try:
                    balance = float(balance_input)
                except:
                    print("Yaroqsiz balans! 0 qilib o'rnatildi.")
                    balance = 0.0
            account = Account(acc_num, acc_holder, balance)
            bank.add_account(account)
        elif tanlov == '2':
            acc_num = input("Hisob raqamini kiriting: ")
            bank.check_balance(acc_num)
        elif tanlov == '3':
            acc_num = input("Hisob raqamini kiriting: ")
            try:
                amount = float(input("Qo'yiladigan summa: "))
            except:
                print("Yaroqsiz summa!")
                continue
            bank.deposit(acc_num, amount)
        elif tanlov == '4':
            acc_num = input("Hisob raqamini kiriting: ")
            try:
                amount = float(input("Yechiladigan summa: "))
            except:
                print("Yaroqsiz summa!")
                continue
            bank.withdraw(acc_num, amount)
        elif tanlov == '5':
            from_acc = input("Qaysi hisobdan (raqami): ")
            to_acc = input("Qaysi hisobga (raqami): ")
            try:
                amount = float(input("O‘tkaziladigan summa: "))
            except:
                print("Yaroqsiz summa!")
                continue
            bank.transfer(from_acc, to_acc, amount)
        elif tanlov == '6':
            acc_num = input("Hisob raqamini kiriting: ")
            bank.display_account_details(acc_num)
        elif tanlov == '7':
            print("Dastur yakunlandi.")
            break
        else:
            print("Noto'g'ri tanlov!")

if __name__ == "__main__":
    main()

# 5. Test the Application:
# Create instances of accounts and test the functionality of your Banking system.
def test_banking_system():
    bank = Bank()
    acc1 = Account("1001", "Saidbek", 100_000)
    acc2 = Account("1002", "Dilorom", 50_000)
    acc3 = Account("1003", "Akbar", 5_000)

    bank.add_account(acc1)
    bank.add_account(acc2)
    bank.add_account(acc3)

    print("\n1. Barcha hisob tafsilotlari:")
    bank.display_account_details("1001")
    bank.display_account_details("1002")
    bank.display_account_details("1003")
    print("\n2. Hisobga pul qo'yish:")
    bank.deposit("1001", 20_000)  
    bank.deposit("1002", 10_000)  
    print("\n3. Hisobdan pul yechish:")
    bank.withdraw("1003", 4_000)  
    bank.withdraw("1003", 2_000)  
    print("\n4. Pul o‘tkazish:")
    bank.transfer("1001", "1002", 50_000)  
    bank.transfer("1003", "1002", 2_000)   
    print("\n5. Balanslarni ko‘rish:")
    bank.check_balance("1001")
    bank.check_balance("1002")
    bank.check_balance("1003")
    print("\n6. Hisob tafsilotlari:")
    bank.display_account_details("1001")
    bank.display_account_details("1002")
    bank.display_account_details("1003")

    print("\n7. Noto'g'ri so‘rovlar:")
    bank.deposit("9999", 1000)          
    bank.withdraw("1001", -500)         
    bank.transfer("1001", "1002", -50)  
    bank.transfer("1001", "9999", 500)  
test_banking_system()
