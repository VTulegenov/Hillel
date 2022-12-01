import sqlite3
from datetime import date
import datetime


current_date = date.today()
db = sqlite3.connect('server.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS databas (
    name TEXT,
    surname TEXT,
    patronymic TEXT,
    age BIGINT,
    date_of_birth BIGINT,
    Date_of_death BIGINT,
    sex TEXT
)""")

db.commit()


while True:
    print("1. Ввести новую запись")
    print("2. Поиск в БД")
    print("3. Загрузить данные в БД из файла")
    print("4. Сохранить данные из БД в файл")
    print("5. Экспортировать данные в json формат")
    print('-' * 50)
    print("0. Выход")
    choice = input("Ваш выбор: ")

    if choice.isdigit() and int(choice) < 6:

        if int(choice) == 1:
            name = input('Введите имя: ')
            surname = input('Введите фамилию: ')
            patronymic = input('Введите отчество: ')
            date_of_birth = input('Введите дату рождения: ')
            Date_of_death = input('Введите дату смерти: ')
            sex = input('Введите пол: ')

            if Date_of_death == '':
                date_of_birth = date_of_birth.split('-')
                current_date = Date_of_death.split('-')
                aa = datetime.date(int(date_of_birth[0]), int(date_of_birth[1]), int(date_of_birth[2]))
                bb = datetime.date(int(current_date[0]), int(current_date[1]), int(current_date[2]))
                age = int((bb-aa).days / (365.2425))
            else:
                date_of_birth = date_of_birth.split('-')
                Date_of_death = Date_of_death.split('-')
                aa = datetime.date(int(date_of_birth[0]), int(date_of_birth[1]), int(date_of_birth[2]))
                bb = datetime.date(int(Date_of_death[0]), int(Date_of_death[1]), int(Date_of_death[2]))
                age = int((bb-aa).days / (365.2425))

                sql.execute(f"INSERT INTO databas VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (str(name), str(surname), str(patronymic), str(age), str(date_of_birth), str(Date_of_death), str(sex)))
                db.commit()


        elif int(choice) == 2:

            word = input('Введите слово: ')
            for title in sql.execute('SELECT * FROM databas WHERE name LIKE ?', ['%' + word + '%']):
                print(title)



        elif int(choice) == 3:
            user_file = input('Укажите файл: ')
            sql.execute(f"INSERT INTO databas VALUES (?)", (open(user_file).read(),))
            db.commit()


        elif int(choice) == 4:
            db.commit()

        elif int(choice) == 5:
            for value in sql.execute("SELECT * FROM databas"):
                print(value)


        elif int(choice) == 0:
            sql.close()
            break
    else:
        print('Некоректный ввод!')



