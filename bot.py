from fileinput import filename
import telebot
import csv
import owncloud
import datetime

class TelegramBot():
    def __init__(self, token, url, username, password, remote_file):
        # token = token
        fileName = 'database.csv'
        bot = telebot.TeleBot(token=token)

        @bot.message_handler(content_types=['text'])
        def message_received(message):
            print(message)
            bot.send_message(chat_id=message.from_user.id, text="AyeAye! Ist eingetragen!", reply_to_message_id="Hi")
            #bot.send_message(reply_to_message_id="Hi")

            oc = owncloud.Client(url)
            oc.login(username,password)
            oc.get_file(remote_file, fileName)

            day = datetime.utcfromtimestamp(message.date).strftime('%Y%m%d')
            hour = datetime.utcfromtimestamp(message.date).strftime('%H:%M:%S')
            with open(fileName, 'a', newline='') as Zaf_file:
                writer = csv.writer(Zaf_file)
                writer.writerow([message.from_user.first_name, message.from_user.username, message.from_user.last_name, day, hour, message.text])

            oc.put_file(filename, remote_file)
            oc.delete(fileName)

        bot.polling(True)