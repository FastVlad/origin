import telebot
from decouple import config
from peewee import *
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Файл .env отсутствует')
else:
    load_dotenv()

bot = telebot.TeleBot(config("TOKEN"))

headers: dict = {
    'x-rapidapi-host': "hotels4.p.rapidapi.com",
    'x-rapidapi-key': config('TOKEN_API')
}

my_db = MySQLDatabase(
    config("DB_name"),
    user="root",
    password=config("DB_password"),
    host='127.0.0.1',
    port=int(config("DB_port"))

)
