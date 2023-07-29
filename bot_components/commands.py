from aiogram import Dispatcher
from db_connection.db_tools import *


async def get_started(mess):
    print(mess)
    return await mess.answer("started")


async def get_menu(mess):
    return await mess.answer("characters list")


def register_command_handlers(dp: Dispatcher):
    dp.register_message_handler(get_started, commands=["start"], state=None)
    dp.register_message_handler(get_menu, commands=["menu"], state=None)
