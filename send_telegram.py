import telegram
from telegram import InputFile
import asyncio  # Import the asyncio library


async def send_tele(image_path):
    print("**********************************")
    # Replace 'YOUR_API_TOKEN' with the API token provided by BotFather
    api_token = '6908044989:AAEzEm6x7Qjnq4jRtJFsX1CkHpkzzjx-lAc'

    # Initialize the Telegram Bot
    bot = telegram.Bot(token=api_token)

    # Replace 'chat_id' with the chat or channel ID where you want to send the image
    chat_id = '5225253331'

    # Replace 'path_to_image.jpg' with the actual path to your image file
    # image_path = '/home/mustafa/Desktop/hero.jpg'

    # Send the image
    with open(image_path, 'rb') as image_file:
        await bot.send_photo(chat_id=chat_id, photo=InputFile(image_file))