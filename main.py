from aiogram import executor, types
from bot_components.bot_gen import dp
from bot_components.commands import register_command_handlers

register_command_handlers(dp)


@dp.message_handler()
async def get_started(mess):
    await mess.answer(f"Для начала работы с ботом испольщуйте команду /start\n Для выбора персонажа используйте /menu")


executor.start_polling(dp, skip_updates=True)