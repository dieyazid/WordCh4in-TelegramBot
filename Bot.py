from pyrogram import Client, filters

app = Client("my_bot", api_id=28131444 ,api_hash="909be1635a5cb111622cda5ac2f7b5bc",bot_token="5936755342:AAFpb-_n3blnHW37qeuSOMdX4VL69Z_z480")
# app.start

@app.on_message()
def handle_word(client, message):
    client.send_message(chat_id=message.chat.id, text="Please wait...")


app.run()