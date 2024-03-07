from dispatcher import dp

from keyboard.main_menu.start import start_kb

from database.control import users

@dp.message_handler(commands="/start")
async def start(message):

    user_id = message.from_user.id

    await users.insert(message.from_user)

    await message.answer(text=f"""<b>
👋 Hi, {message.from_user.first_name}!

🖥 Github - https://github.com/fajox1
</b>""", reply_markup=await start_kb(user_id))
