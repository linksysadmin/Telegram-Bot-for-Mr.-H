import os

import telebot
from telebot.storage import StateRedisStorage
from dotenv import load_dotenv

load_dotenv()

# FOR OPENAI_API(ChatGPT)
OPENAI_API_TOKEN = os.getenv('OPENAI_API_TOKEN')

# FOR TELEGRAM_API
TELEGRAM_BOT_API_TOKEN = os.getenv('TELEGRAM_BOT_API_TOKEN')
OPERATOR_ID = int(os.getenv('OPERATOR_ID'))



# FOR MySQL
MySQL_HOST = 'mysql'
MySQL_USER = os.getenv('MYSQL_USER')
MySQL_PASS = os.getenv('MYSQL_ROOT_PASSWORD')
MySQL_DB = os.getenv('MYSQL_DATABASE')

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIR_FOR_TECHNICAL_TASKS = f'{BASE_DIR}/static/documents/technical_tasks'
DIR_FOR_COMMERCIAL_OFFERS = f'{BASE_DIR}/static/documents/commercial_offers'
DIR_FOR_REPORTS = f'{BASE_DIR}/static/documents/reports'
DIR_FOR_OTHER_FILES = f'{BASE_DIR}/static/documents/other_documents'
DIR_FOR_SAVE_DIALOGS = f'{BASE_DIR}/static/documents/dialogs'

bot = telebot.TeleBot(TELEGRAM_BOT_API_TOKEN, state_storage=StateRedisStorage(host='redis'), parse_mode='HTML')









