from pyrogram.types import ReplyKeyboardMarkup

def Main_Keyboard(client,chatid):
    client.send_message(
            chat_id=chatid,
            text="⛓️ Welcome to Word Chain ⛓️",
            reply_markup=ReplyKeyboardMarkup(
                [
                    ['Start Game 🏁'],
                    ['Rules 📜'],
                    ['About']
                ],
                resize_keyboard=True
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
                resize_keyboard=True
            )
        )