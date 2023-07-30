from aiogram import executor, types
from bot_components.bot_gen import dp
from bot_components.commands import register_command_handlers
from bot_components.gpt_connert import asc_to_gpt
from db_connection.db_tools import SQLRequests
from datetime import datetime

register_command_handlers(dp)
dbase = SQLRequests()


@dp.message_handler()
async def common_message_handler(mess):

    # is user registered
    if not dbase.user_exists(mess.chat.id):
        # create new user if not exists
        dbase.create_user({
            'id': mess.chat.id,
            'username': mess.chat.username,
            'name': mess.chat.first_name,
            'time': datetime.now()
        })
        # return the menu to choice character
        await mess.answer("Here will be the link to web app")

    else:
        try:
            # target_character = dbase.get_user_character(mess.chat.id)
            if True:
                # start generate the answer
                await mess.answer("Генерирую ответ...")

                result = await asc_to_gpt(prompt="Супер Марио: " + mess.text)
                await mess.answer(f"Ваш ответ: \n{result}")
            else:
                # user have no character
                await mess.answer("You have no character :( Chose one pls")

        except Exception as e:
            print(e)
            await mess.answer("Что-то пошло не так :(")


executor.start_polling(dp, skip_updates=True)
