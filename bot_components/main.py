from aiogram import executor
from bot_gen import dp

from bot_components.commands import register_command_handlers


@dp.message_handler()
async def get_started(mess):
    await mess.answer(f"Для начала работы с ботом испольщуйте команду /start")

register_command_handlers(dp)
executor.start_polling(dp, skip_updates=True)
