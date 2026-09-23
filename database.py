import sqlite3
import json
from datetime import datetime

DB_NAME = "lessons.db"


def init_db():
    """Создание таблиц при первом запуске"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Таблица пользователей
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            last_name TEXT,
            registered_at TEXT
        )
    ''')

    # Таблица платежей и доступов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            lesson_id TEXT,
            payment_id TEXT UNIQUE,
            amount INTEGER,
            currency TEXT,
            status TEXT,
            zoom_link TEXT,
            paid_at TEXT,
            accessed_at TEXT,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
        )
    ''')

    conn.commit()
    conn.close()


def save_user(user_id, username, first_name, last_name):
    """Сохранить или обновить пользователя"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR IGNORE INTO users (user_id, username, first_name, last_name, registered_at)
        VALUES (?, ?, ?, ?, ?)
    ''', (user_id, username, first_name, last_name, datetime.now().isoformat()))
    conn.commit()
    conn.close()


def save_payment(user_id, lesson_id, payment_id, amount, currency, zoom_link):
    """Сохранить информацию о платеже"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO payments (user_id, lesson_id, payment_id, amount, currency, status, zoom_link, paid_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, lesson_id, payment_id, amount, currency, "paid", zoom_link, datetime.now().isoformat()))
    conn.commit()
    conn.close()


def is_lesson_purchased(user_id, lesson_id):
    """Проверить, куплен ли урок пользователем"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT 1 FROM payments 
        WHERE user_id = ? AND lesson_id = ? AND status = 'paid'
    ''', (user_id, lesson_id))
    result = cursor.fetchone()
    conn.close()
    return result is not None


def get_user_purchases(user_id):
    """Получить все купленные уроки пользователя"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT lesson_id, zoom_link, paid_at FROM payments 
        WHERE user_id = ? AND status = 'paid'
        ORDER BY paid_at DESC
    ''', (user_id,))
    results = cursor.fetchall()
    conn.close()
    return results


def mark_lesson_accessed(user_id, lesson_id):
    """Отметить, что ссылка была выдана (логирование)"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE payments 
        SET accessed_at = ? 
        WHERE user_id = ? AND lesson_id = ? AND status = 'paid'
    ''', (datetime.now().isoformat(), user_id, lesson_id))
    conn.commit()
    conn.close()