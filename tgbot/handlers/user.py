from aiogram.types import Message
from aiogram.dispatcher.filters import CommandHelp, CommandStart
from aiogram.utils.markdown import hlink

from loader import dp


@dp.message_handler(CommandHelp())
@dp.message_handler(CommandStart())
async def send_welcome(message: Message):
    """
    This handler will be called when user sends /help or /start command
    """
    await message.answer(f'Привіт! Я бот, який надає кривий переклад. Дізнатись, що це, можеш {hlink("тут", "https://www.youtube.com/watch?v=jFbqy6-SK0Y")}. Якщо коротко, то бот перекладає текст через 10 різних мов і повертається до початкового вигляду.')
