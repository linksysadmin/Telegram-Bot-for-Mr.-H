# -*- coding: utf-8 -*-
import logging

import flask
import telebot

from handlers.register import RegisterTelegramFunctions
from config import bot
from services.redis_db import redis_cache


logging.basicConfig(filename='log.log',
                    level=logging.INFO,
                    encoding='utf-8',
                    format='%(asctime)s -%(levelname)s:%(message)s',
                    datefmt='%m.%d.%Y')

logger = logging.getLogger(__name__)


RegisterTelegramFunctions()


try:
    logger.info('Бот запущен')
    bot.infinity_polling(skip_pending=True)
except KeyboardInterrupt:
    logger.info('Выход из программы')
finally:
    logger.warning('Программа остановлена')
    redis_cache.clear_all_cache()

#
# app = flask.Flask(__name__)
# @app.route('/', methods=['POST'])
# def webhook():
#     """Обработка http-запросов, которые telegram пересылает на наш сервер"""
#     if flask.request.headers.get('content-type') == 'application/json':
#         json_string = flask.request.get_data().decode('utf-8')
#         update = telebot.types.Update.de_json(json_string)
#         bot.process_new_updates([update])
#         return ''
#     else:
#         logger.error('abort(403)')
#         flask.abort(403)

