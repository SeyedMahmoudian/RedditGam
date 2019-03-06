import telepot as bot


class telegramBot:
    token = ""
    photo = ""
    name = ""

    def __init__(self, name):
        self.name = name
        self.telegram()

    def telegram(self):
        token = '' # put the token from telegram here
        myBot = bot.Bot(token)
        url = "C:\\Users\\Amin\\Documents\\MEGA\\pythons\\redditGam\\NatureIsFuckingLit\\_pic.jpg"
        photo = open(url.encode('utf-8'), 'rb')
        myBot.sendPhoto(chat_id='', photo=photo, caption=self.name) # put the chat_id recieved from telegram here 
        photo.close()
        print("posted!")
