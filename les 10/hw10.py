import sqlite3
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# 1. Створення бази даних
DB_NAME = "weather_data.db"
def create_database():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Weather (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            datetime TEXT NOT NULL,
            temperature TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# 2. Функція для парсингу погоди
CITY_URL = "https://example-weather-website.com/your-city"  # Замініть на реальну URL

def fetch_weather():
    response = requests.get(CITY_URL)
    if response.status_code != 200:
        raise Exception("Не вдалося отримати дані з сайту погоди")

    soup = BeautifulSoup(response.text, "html.parser")
    # Замініть '.temperature-class' на реальний селектор сайту
    temperature = soup.select_one(".temperature-class").text.strip()
    return temperature

# 3. Додавання даних до БД
def insert_weather_data(temperature):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO Weather (datetime, temperature) VALUES (?, ?)",
                   (current_datetime, temperature))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    try:
        create_database()
        temperature = fetch_weather()
        insert_weather_data(temperature)
        print("Дані успішно збережено до бази даних.")
    except Exception as e:
        print(f"Сталася помилка: {e}")