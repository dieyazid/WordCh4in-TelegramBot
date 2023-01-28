from pyrogram import Client, filters
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton)
from words import *
from gifs import gifs

app = Client("my_bot", api_id=28131444 ,api_hash="909be1635a5cb111622cda5ac2f7b5bc",bot_token="5936755342:AAFpb-_n3blnHW37qeuSOMdX4VL69Z_z480")
# app.start

############ Handlers ############
def Main():
    @app.on_message(filters.regex('^\/start$'))
    def handle_word(client, message):
        client.send_message(chat_id=message.chat.id, text="Please wait...")
        Main_Keyboard(client,message.chat.id)

    @app.on_message(filters.regex('^Start Game 🏁$'))
    def handle_action(client, message):
        client.send_message(chat_id=message.chat.id, text="Cool let's play 😄")
        Pre_Game()
        Player_Decision_Keyboard(client,message.chat.id)

    @app.on_message(filters.regex('^Rules 📜$'))
    def handle_action(client, message):
        client.send_message(chat_id=message.chat.id, text="""Rules are simple:
    1. You can only use words that start with the last letter of the previous word.
    2. You can't use the same word twice.
    3. You can't use a word that is not in the dictionary.
    4. Same as the third 😀.
        """)

    @app.on_message(filters.regex('^About$'))
    def handle_action(client, message):
        client.send_message(chat_id=message.chat.id, text="""
        I was made by @Y42id and @medbenzekri.
        You can get in touch with them if you want to know more about me 😁
        """)

############ Pre Game ############
def Pre_Game():
    @app.on_message(filters.regex('^Me 👦$'))
    def handle_action(client, message):
        user_id=message.chat.id
        user = Game.handle_user(user_id)
        client.send_message(chat_id=message.chat.id, text="Ok, you start first")
        Start_Game('HUMAN')

    @app.on_message(filters.regex('^AI 🤖$'))
    def handle_action(client, message):
        # load_words()
        user_id=message.chat.id
        
        user = Game.handle_user(user_id)
        client.send_message(chat_id=message.chat.id, text="Ok, I start first")
        Surrender_Keyboard(client,message.chat.id)
        client.send_message(chat_id=message.chat.id, text="The first word is")
        client.send_message(chat_id=message.chat.id, text=f"{user.ai_first_turn()}")
        client.send_message(chat_id=message.chat.id, text="Your turn")
        Start_Game()

############ Game ############
def Start_Game(First_Player=any):
    @app.on_message(filters.regex('^[a-zA-Z]+$'))
    def handle_word(client, message):
        user_id=message.chat.id
        user = Game.handle_user(user_id)
        if First_Player=='HUMAN':
            valid=user.player_first_turn(message.text)
        else:
            valid=user.player_turn(message.text)
        if valid==False:
            gif_file=random.choice(gifs)
            client.send_message(chat_id=message.chat.id, text="You lost")
            client.send_animation(message.chat.id, gif_file)
            Play_Again_Keyboard(client,message.chat.id)
        else:
            client.send_message(chat_id=message.chat.id, text=f"{user.ai_turn(message.text)}")

    @app.on_message(filters.regex('Surrender 🏳️'))
    def handle_word(client, message):
        client.send_message(chat_id=message.chat.id, text="Well that's a win for me 💪😏")
        Main_Keyboard(client,message.chat.id)

    @app.on_message(filters.regex('[^a-zA-Z]+'))
    def handle_word(client, message):
        client.send_message(chat_id=message.chat.id, text="Wow wait that's not allowed 😶")



### Keybaords
def Main_Keyboard(client,chatid):
    client.send_message(
            chat_id=chatid,
            text="🌪 Weclome to Word Chain ⛓️",
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['Start Game 🏁'],
                    ['Rules 📜'],
                    ['About']
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
        )
def Player_Decision_Keyboard(client,chatid):
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
            text="",
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['Play Again']
                ],
                resize_keyboard=True  # Make the keyboard smaller
            )
        )
app.run(Main())