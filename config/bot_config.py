"""Конфигурация бота."""
import os
from dotenv import load_dotenv

# Загружаем .env файл если он есть (для локальной разработки)
load_dotenv('./config/.env')

# Читаем из переменных окружения системы
API_TOKEN = os.getenv('TOKEN')
SQLALCHEMY_URL = os.getenv('SQLALCHEMY_URL')
ADMIN_ID = int(os.getenv('ADMIN_ID', '0'))

# Проверка обязательных переменных
if not API_TOKEN:
    raise ValueError("❌ TOKEN не найден! Добавьте переменную окружения TOKEN")

if not SQLALCHEMY_URL:
    raise ValueError("❌ SQLALCHEMY_URL не найден! Добавьте переменную окружения SQLALCHEMY_URL")
