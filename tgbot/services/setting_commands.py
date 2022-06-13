from aiogram import Bot
from aiogram.types import BotCommand


async def set_default_commands(bot: Bot) -> None:
    commands = [
        BotCommand(command='start', description='Запустити бота'),
        BotCommand(command='help', description='Показати інструкцію'),
    ]
    await bot.set_my_commands(commands=commands)
