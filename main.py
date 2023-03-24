from datetime import datetime
import pyrogram,os,random
from pyrogram import filters
from services.game import *
from services.gifs import *
from services.keyboards import *

api_id = os.environ["API_ID"]
api_hash = os.environ["API_HASH"]
bot_token = os.environ["BOT_TOKEN"]

app = pyrogram.Client("my_bot", api_id=api_id ,api_hash=api_hash,bot_token=bot_token)

now = datetime.now()
class User:
    def __init__(self, id):
        self.id = id
        self.score = 0
        self.answers = []
        self.duplicated=[]
        self.current_word=""
        self.user_word=""
        self.wrong = 0
        self.score = 0
        self.answers = []

users = {}


@app.on_message(filters.command("start"))
def start(client, message):
    user_id = message.chat.id
    if user_id not in users:
        users[user_id] = User(user_id)
        current_time = now.strftime("%H:%M:%S")
        print(str(user_id)+' Joined The session on :'+current_time)
    Main_Keyboard(client, user_id)


@app.on_message(filters.regex('^Start Game 🏁$'))
def play(client, message):
    user_id = message.chat.id
    client.send_message(message.chat.id,'''❗Note : Sorry in advance that you might spell a correct word that I don't know because my dictionary is limited to 58k words ❗''')
    client.send_message(message.chat.id,'let\'s play 😄')
    Turn_Decision_Keyboard(client, user_id)
    @app.on_message(filters.regex('^Me 👦$') | filters.regex('^AI 🤖$'))
    def turn(client, message):
        if message.text == 'Me 👦':
            client.send_message(message.chat.id,'You have chosen to start first')
            Game_On(client,message,'Me')
        elif message.text == 'AI 🤖':
            client.send_message(message.chat.id,'Alright I\'ll start first')
            Game_On(client,message,'AI')

@app.on_message(filters.regex('^Rules 📜$'))
def rules(client, message):
    user_id = message.chat.id
    client.send_message(message.chat.id,'''Rules are simple:
            1. You can only use words that start with the last letter of the previous word.
            2. You can't use the same word twice.
            3. You can't use a word that is not in the dictionary.
    ''')

@app.on_message(filters.regex('^About$'))
def about(client, message):
    user_id = message.chat.id
    client.send_message(message.chat.id,'''About:
    This bot is made by @Y_4z1d and @medbenzekri
    ''')

@app.on_message(filters.regex('^No Thanks$'))
def nothanks(client, message):
    user_id = message.chat.id
    client.send_message(message.chat.id,'''Ok, see you later 😊
    ''')

@app.on_message(filters.regex('^Play Again 🔄$'))
def playagain(client, message):
    user_id = message.chat.id
    client.send_message(message.chat.id,'''Ok, let's play again 😊
    ''')
    Turn_Decision_Keyboard(client, user_id)

@app.on_message(filters.regex('^Quit Game ❌$'))
def quitgame(client, message):
    user_id = message.chat.id
    client.send_message(message.chat.id,'''Ok, see you later 😊
    ''')

def Game_On(client,message,Turn,On=True):
    Valid = False
    user_id = message.chat.id
    if Turn == 'Me':
        @app.on_message(filters.text)
        def my_turn(client, message):
            users[user_id].user_word = message.text.lower()
            Valid = Valid_Check(
                users[user_id].user_word,
                users[user_id].current_word,
                users[user_id].duplicated,
            )
            if Valid == True:
                users[user_id].duplicated.append(users[user_id].user_word)
                users[user_id].answers.append(users[user_id].user_word)
                users[user_id].current_word = users[user_id].user_word
                users[user_id].score += 1
                client.send_message(message.chat.id,'''It's my turn now  ''')
                Game_On(client,message,'AI')

            else:
                client.send_message(message.chat.id,'''Invalid word, try again  ''')
                users[user_id].wrong += 1
                if users[user_id].wrong == 1:
                    client.send_message(message.chat.id,'''You have 2 attemps left  ''')
                elif users[user_id].wrong == 2:
                    client.send_message(message.chat.id,'''You have 1 attemps left  ''')
                if users[user_id].wrong == 3:
                    client.send_message(message.chat.id,'''You lost 😔''')
                    Game_Over(client,message)
                Game_On(client,message,'Me')
    elif Turn == 'AI':
        answer = Generate_Bot_Answer(users[user_id].user_word,users[user_id].current_word,users[user_id].duplicated)
        if answer == 'I Lost':
            client.send_message(message.chat.id,'''You won 😒''')
            Game_Over(client,message)
        client.send_message(message.chat.id,answer)
        users[user_id].duplicated.append(answer)
        users[user_id].current_word = answer
        client.send_message(message.chat.id,'''your turn now''')
        Game_On(client,message,'Me')

def Game_Over(client,message):
    user_id = message.chat.id
    gif_file=random.choice(gifs)
    client.send_animation(user_id, gif_file)
    client.send_message(message.chat.id,'''Your score is : '''+str(users[user_id].score))
    client.send_message(message.chat.id,'''Game Over''')
    Play_Again_Keyboard(client, user_id)
    Clear_game(message)

def Clear_game(message):
    user_id = message.chat.id
    users[user_id].user_word = ''
    users[user_id].current_word = ''
    users[user_id].duplicated.clear()
    users[user_id].answers.clear()
    users[user_id].score = 0
    users[user_id].wrong = 0
# =============================== #
def Reply(client,message,text):
    client.send_message(chat_id=message.chat.id, text=text)

app.run()
