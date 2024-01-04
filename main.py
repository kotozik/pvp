import telebot

bot = telebot.TeleBot("")
games = {
}


@bot.message_handler(commands=['create_game'])
def msgs(m):
    games[m.chat.id] = {
        'player1': None,
        'player2': None
    }
    bot.send_message(m.chat.id, "Игра была создана! Присоединитесь " +
                     "командой /join.")


@bot.message_handler(commands=['join'])
def msgs2(m):
    game = games[m.chat.id]
    if game['player1'] == None:
        creat_player(m, 'player1')

    elif game['player2'] == None:
        create_player(m, 'player2')


def create_player(m, player, game):
    game[player] = {
        'id': m.from_user.first_name,
        'defence': None,
        'attack': None
    }


@bot.message_handler(commands=['bebra'])
def msgs(m):
    bot.send_message(m.chat.id, "Игра началась ")


bot.send_message(game['player1']['id']
"Какую часть тела защищать(Отправь текст)"
"защита1 - Голова/защитаn2 - Туловище/защитаn3 - Ноги")
bot.send_message(game['player2']['id']
"Какую часть тела защищать(Отправь текст )"
"защита1 - Голова/nзащита2 - Туловище/nзащита3 - Ноги")

def select_defence(m, game):
    if game['player1']['id'] == m.from_user.id:
        game['player1']['defence'] = m.text

elif game['player2']['id'] == m.from_user.id:
game['player2']['defence'] = m.text


@bot.message_handler()
def digits(m):
    game = games[m.chat.id]
    if m.text == "защита1":
        bot.send_message(m.chat.id, "Выбрана оборона: Голова.")
        select_defence(m, game)
    if m.text == "защита2":
        bot.send_message(m.chat.id, "Выбрана оборона: Туловище.")
        select_defence(m, game)
    if m.text == "защита3":
        bot.send_message(m.chat.id, "Выбрана оборона: Ноги.")
        select_defence(m, game)

    if m.text == "атака1":
        bot.send_message(m.chat.id, "Выбрана атака : Голова.")
        select_defence(m, game)
    if m.text == "атака2":
        bot.send_message(m.chat.id, "Выбрана атака : Туловище.")
        select_defence(m, game)
    if m.text == "атака3":
        bot.send_message(m.chat.id, "Выбрана атака : Ноги.")
        select_defence(m, game)


def select_attak(m, game):
    if game['player1']['id'] == m.from_user.id:
        game['player1']['attak'] = m.text

elif game['player2']['id'] == m.from_user.id:
game['player2']['attak'] = m.text

if game['player1']['defence'] !=







bot_infinity_polling()
