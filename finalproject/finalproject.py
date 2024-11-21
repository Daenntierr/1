import sqlite3
import requests
from bs4 import BeautifulSoup
from collections import Counter


class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
        self.cursor = None

    def connect(self):
        """Підключення до бази даних."""
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()

    def close(self):
        """Закриття з'єднання з базою даних."""
        if self.connection:
            self.connection.close()

    def create_table(self):
        """Створення таблиці для зберігання сайтів."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sites (
                id INTEGER PRIMARY KEY,
                url TEXT UNIQUE
            )
        ''')
        self.connection.commit()

    def add_site(self, url):
        """Додавання нового сайту в базу даних."""
        try:
            self.cursor.execute('INSERT INTO sites (url) VALUES (?)', (url,))
            self.connection.commit()
        except sqlite3.IntegrityError:
            print(f"Site {url} already exists in the database.")

    def get_sites(self):
        """Отримання всіх сайтів з бази даних."""
        self.cursor.execute('SELECT url FROM sites')
        return [row[0] for row in self.cursor.fetchall()]

    def clear_database(self):
        """Очистка бази даних від всіх сайтів."""
        self.cursor.execute('DELETE FROM sites')
        self.connection.commit()


class WebScraper:
    def __init__(self):
        pass

    def fetch_page(self, url):
        """Отримання HTML-коду сторінки."""
        response = requests.get(url)
        return response.text

    def count_word_occurrences(self, html, search_word):
        """Підрахунок кількості згадок слова на сторінці."""
        soup = BeautifulSoup(html, 'html.parser')
        text = soup.get_text().lower()
        return text.count(search_word.lower())


class UserInterface:
    def __init__(self):
        pass

    def display_message(self, message):
        """Виведення повідомлень для користувача."""
        print(message)

    def get_input(self, prompt):
        """Отримання вводу від користувача."""
        return input(prompt)

    def display_search_results(self, results):
        """Виведення результатів пошуку."""
        for result in results:
            print(f"URL: {result['url']}, Matches: {result['count']}")


def run():
    db = Database('sites.db')
    scraper = WebScraper()
    ui = UserInterface()

    # Підключення до бази даних та створення таблиці
    db.connect()
    db.create_table()

    while True:
        print("\n1. Додати сайт")
        print("2. Очищення бази даних")
        print("3. Пошук інформації на сайтах")
        print("4. Переглянути всі сайти")
        print("5. Вийти")

        choice = ui.get_input("Виберіть дію: ")

        if choice == '1':
            url = ui.get_input("Введіть URL сайту: ")
            db.add_site(url)
        elif choice == '2':
            db.clear_database()
            ui.display_message("База даних очищена.")
        elif choice == '3':
            search_word = ui.get_input("Введіть слово для пошуку: ")
            sites = db.get_sites()
            results = []

            for site in sites:
                html = scraper.fetch_page(site)
                count = scraper.count_word_occurrences(html, search_word)
                if count > 0:
                    results.append({'url': site, 'count': count})

            results = sorted(results, key=lambda x: x['count'], reverse=True)
            ui.display_search_results(results)
        elif choice == '4':
            sites = db.get_sites()
            ui.display_message("Список сайтів:")
            for site in sites:
                print(site)
        elif choice == '5':
            break

    # Закриття з'єднання з базою даних
    db.close()


if __name__ == "__main__":
    run()

