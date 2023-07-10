from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start", "Запустить анкету"),
        types.BotCommand("cancel", "Остановить анкету"),
        # types.BotCommand("help", "Помощь"),
    ])
