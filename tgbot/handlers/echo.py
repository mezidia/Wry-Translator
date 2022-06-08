from aiogram.types import Message
from aiogram.utils.markdown import hspoiler


from loader import dp


@dp.message_handler()
async def echo(message: Message) -> Message:
    translator = message.bot['translator']
    await message.answer(f'Через декілька секунд ви отримаєте кривий переклад.\n{hspoiler("Інколи це може займати більше часу.")}')
    wry_text = translator.get_full_translation(message.text.lower())
    await message.answer(wry_text)
