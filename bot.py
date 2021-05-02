import telebot

import api
import utils


bot = telebot.TeleBot('1646742384:AAH9rDrMR19EfPZzueCdCgVzRzDatKTIGRw')



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,
    """
    Hello, I'm Covid-19 🦠 tracker Bot for Kazakhstan 🇰🇿
/symptoms
/last
/stat
    """)


@bot.message_handler(commands=['stat'])
def stat_by_date(message):
    try:
        date = telebot.util.extract_arguments(message.text)
        d = utils.validate_date(date)

        if type(d) == dict:
            bot.send_message(message.chat.id, d['error'])
        else:
            data = api.get_country_statistics()
            date_data = next((stat for stat in data if stat['Date'] == '{y:4}-{m:02}-{d:02}T00:00:00Z'.format(y=d.year, m=d.month, d=d.day)), None)
            if not date_data:
                bot.send_message(message.chat.id, "Sorry, statisctics for that date not found.")
                return

            utils.save_to_csv([date_data], f'data/date/{date}Kazakhstan.csv')
            bot.send_message(message.chat.id,
            f"""
The statistics for Kazakhstan 🇰🇿
Confirmed: {date_data['Confirmed']} 🧐
Recovered: {date_data['Recovered']} 👩🏼‍🔬
Active: {date_data['Active']} 🤕
Died: {date_data['Deaths']} ⚰️

Date: {date}""")

            doc = open(f'data/date/{date}Kazakhstan.csv', 'rb')
            bot.send_document(message.chat.id, doc)
    except Exception as e:
        bot.send_message(message.chat.id, str(e))

@bot.message_handler(commands=['last'])
def last_statistics(message):
    data = api.get_last_statistics()

    date = data['Date'].split('T')[0]
    bot.send_message(message.chat.id,
f"""
The last statistics for Kazakhstan 🇰🇿
Confirmed: {data['Confirmed']} 🧐
Recovered: {data['Recovered']} 👩🏼‍🔬
Active: {data['Active']} 🤕
Died: {data['Deaths']} ⚰️

Date: {date}
""")

@bot.message_handler(commands=['symptoms'])
def send_symptoms(message):
    bot.send_message(message.chat.id,
    """
    🛑 Most common symptoms 🛑:
- fever
- dry cough
- tiredness
⭕️ Less common symptoms ⭕️:
- aches and pains
- sore throat
- diarrhoea
- conjunctivitis
- headache
- loss of taste or smell
- a rash on skin, or discolouration of fingers or toes
🆘 Serious symptoms 🆘:
- difficulty breathing or shortness of breath
- chest pain or pressure
- loss of speech or movement
    """)


bot.polling()