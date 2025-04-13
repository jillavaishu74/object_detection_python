import telegram
import asyncio
bot = telegram.Bot(token='6908044989:AAEzEm6x7Qjnq4jRtJFsX1CkHpkzzjx-lAc')
channel_id = '5225253331'

# Send a text message
async def custom_coro():
	await bot.send_message(chat_id=channel_id, text='Hello, World!')

coro = custom_coro()
asyncio.run(coro)