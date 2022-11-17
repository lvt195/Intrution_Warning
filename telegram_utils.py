import telegram

def send_telegram(photo_path="img/alert.png"):
    try:
        my_token = "5668555029:AAHB7sWIy-w5f18KETb34e8hotU7M7vmUlI"
        bot = telegram.Bot(token=my_token)
        bot.sendPhoto(chat_id="5414283367", photo=open(photo_path,"rb"), caption="Có xâm nhập, nguy hiêm!")
    except Exception as ex:
        print("Can not send message telegram ", ex)

    print("Send sucess")