import asyncio
import config
from aiogram import Bot, Dispatcher, types,F
from aiogram.filters.command import Command
import logging
import random
from keyboards import kb1, kb2
from random_fox import fox


#Включаем логгирование
logging.basicConfig(level=logging.INFO)

#Создаем объект бота
bot = Bot(token=config.token)

#Диспечер
dp = Dispatcher()


#Хэндлер на команду /start
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    name = message.chat.first_name
    await message.answer(f'Здравствуйте, {name}', reply_markup=kb1)


#Хэндлер на команду /info
@dp.message(F.text == 'Инфо')
@dp.message(Command("info"))
async def cmd_info(message: types.Message):
    await message.reply("Адрес клиники: г.Москва, Дербеневская набережная,д.13/17, стр.1. Вход с торца. 24/7 ")


#Хэндлер на команду /stop
@dp.message(F.text == 'Стоп')
@dp.message(Command("stop"))
async def cmd_info(message: types.Message):
    await message.reply("Желаем здоровья Вам и Вашим питомцам!")


#Хэндлер на команду /close
@dp.message(F.text == 'Закрыть')
@dp.message(Command("close"))
async def cmd_info(message: types.Message):
    await message.reply("Мы на связи с Вами 24/7!")


#Хэндлер на команду /fox
@dp.message(F.text == 'Покажите лису')
@dp.message(Command('fox'))
@dp.message(Command('лиса'))
async def cmd_fox(message: types.Message):
    name = message.chat.first_name
    img_fox = fox()
    await message.reply(f'Вот Вам лиса, {name}!')
    await message.answer_photo(photo=img_fox)


#Хендлер на сообщения
@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message.chat.first_name
    if 'привет' in msg_user:
        await message.answer(f'Привет-привет, {name}')
    elif 'пока' == msg_user:
        await message.answer(f'Пока-пока, {name}')
    elif 'ты кто' in msg_user:
        await message.answer(f'Я бот, {name}')
    elif 'покажи лису' in msg_user:
        await message.answer(f'Смотри, что у меня есть, {name}', reply_markup=kb2)
    elif 'покажи фокус' in msg_user:
        await message.answer_dice(emoji="🎲")
    else:
        await message.answer(f'Я не знаю такого слова')


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())