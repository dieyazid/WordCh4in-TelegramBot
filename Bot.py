from pyrogram import Client, filters
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton)
from words import *
from gifs import gifs
import os
api_id = os.environ.get("API_ID")
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

app = Client("my_bot", api_id=api_id ,api_hash=api_hash,bot_token=bot_token)
# app.start

def Main():
    @app.on_message(filters.command('start'))
    def handle_word(client, message):
        Main_Keyboard(client,message.chat.id)
        Handle_Main()

### Handlers ########################################################################
def Handle_Main():
    @app.on_message(filters.regex('^Start Game 🏁$') | filters.regex('^Rules 📜$') | filters.regex('^About$'))
    def handle_action(client, message):
        if message.text == 'Start Game 🏁':
            client.send_message(chat_id=message.chat.id, text="Cool let's play 😄")
            Pre_Game(client,message.chat.id)

        elif message.text == 'Rules 📜':
            client.send_message(chat_id=message.chat.id, text="""Rules are simple:
            1. You can only use words that start with the last letter of the previous word.
            2. You can't use the same word twice.
            3. You can't use a word that is not in the dictionary.
            4. Same as the third 😀.
                """)

        elif message.text == 'About':
            client.send_message(chat_id=message.chat.id, text="""
                I was made by @Y42id and @medbenzekri.
                You can get in touch with them if you want to know more about me 😁
                """)
def Play_Again_Handler(client,message):
    Play_Again_Keyboard(client,message.chat.id)
    @app.on_message(filters.regex('^Play Again 🔄$') | filters.regex('No Thanks'))
    def handle_action(client, message):
        if message.text == 'Play Again 🔄':
            Pre_Game(client,message.chat.id)
        elif message.text == 'No Thanks':
            client.send_message(chat_id=message.chat.id, text="Ok, see you later 😁")
            Main_Keyboard(client,message.chat.id)
            Handle_Main()
### Pre Game ########################################################################
def Pre_Game(client,chatid):
    Turn_Decision_Keyboard(client,chatid)
    @app.on_message(filters.regex('^Me 👦$') | filters.regex('^AI 🤖$'))
    def handle_action(client, message):
        user_id=message.chat.id
        user = Game.handle_user(user_id)
        if message.text == 'Me 👦':
            client.send_message(chat_id=message.chat.id, text="Ok, you start first")
            Start_Game('HUMAN')
        elif message.text == 'AI 🤖':
            client.send_message(chat_id=message.chat.id, text="Ok, I start first")
            Surrender_Keyboard(client,message.chat.id)
            client.send_message(chat_id=message.chat.id, text="The first word is")
            client.send_message(chat_id=message.chat.id, text=f"{user.Ai_Turn(True)}")
            client.send_message(chat_id=message.chat.id, text="Your turn")
            Start_Game()

############ Game #####################################################################

def Start_Game(First_Player=any):
    @app.on_message(filters.regex('^[a-zA-Z]+$'))
    def handle_word(client, message):
        user_id=message.chat.id
        user = Game.handle_user(user_id)

        if First_Player=='HUMAN':
            user.Player_Turn(True,message.text.lower())
        else:
            response=user.Player_Turn(False,message.text.lower())
            Handle_Error(client,message,response,user)

    @app.on_message(filters.regex('Surrender 🏳️'))
    def handle_word(client, message):
        client.send_message(chat_id=message.chat.id, text="Well that's a win for me 💪😏")
        Main_Keyboard(client,message.chat.id)

    # @app.on_message(filters.regex('[^a-zA-Z]+'))
    # def handle_word(client, message):
    #     client.send_message(chat_id=message.chat.id, text="Wow wait that's not allowed 😶")

### Game Result ######################################################################

def Handle_Error(client,message,result,user):
    if result in ['Unvalid','Letter Fail','Duplicated']:
        if result=='Unvalid':
            client.send_message(message.chat.id, text='You used an unvalid or misspelled word!')
            client.send_message(message.chat.id, text="You should read a dictionary!")

        elif result=='Letter Fail':
            client.send_message(message.chat.id, text='Wrong word!')
            client.send_message(message.chat.id, text='You can only use words that start with the last letter of the previous word.')
        
        elif result=='Duplicated':
            client.send_message(message.chat.id, text='Wrong word!')
            client.send_message(message.chat.id, text='You can\'t use the same word twice.')
        ### Sarcasm
        gif_file=random.choice(gifs)
        client.send_animation(message.chat.id, gif_file)
        Play_Again_Handler(client,message)
    
    elif result=='Valid': 
        client.send_message(message.chat.id, text=f"{user.Ai_Turn(False,message.text.lower())}")

### Keybaords ########################################################################

def Main_Keyboard(client,chatid):
    client.send_message(
            chat_id=chatid,
            text="⛓️ Word Chain ⛓️",
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['Start Game 🏁'],
                    ['Rules 📜'],
                    ['About']
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
        )
def Turn_Decision_Keyboard(client,chatid):
    client.send_message(
            chat_id=chatid,
            text="But before that who do you think should start first? 🤔",
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['Me 👦','AI 🤖']
                ],
                resize_keyboard=True
            )
        )
def Surrender_Keyboard(client,chatid):
    client.send_message(
            chat_id=chatid,
            text='You can just press Surrender button if you felt like stopping',
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['Surrender 🏳️']
                ],
                resize_keyboard=True
            )
        )

def Play_Again_Keyboard(client,chatid):
    client.send_message(
            chat_id=chatid,
            text="Would you like to play again?",
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['Play Again 🔄','No Thanks']
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
        )
app.run(Main())
