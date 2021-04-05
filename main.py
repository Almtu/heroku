import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
import json
import smtplib   
from apiModule import efapi # Import class

g = False
isinbuyloop = False
back1 = True
keys = False
qwe = False
understand = False
user = ['544767906', '420465550']

def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id':10})
def get_button(label, color, payload=""):
    return {
        "action": {
            "type": "text",
            "payload": json.dumps(payload),
            "label": label
        },
        "color": color
    }
keyboard = {
    "one_time": False,
    "buttons": [
            [get_button(label="💰 Купить", color="positive")],
            [get_button(label="🧠 Поддержка", color="primary")],
            [get_button(label="🗿 Сайт", color="default")]
    ]
}

keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))

token = "1f0585cb178d457837bdef72419fbbcd8466992c244da95171bc0eb049f8e638d4b762a735a4f11f8fe3a"
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text.lower() == 'начать' or event.text.lower() == 'привет' or event.text.lower() == 'старт':
            understand = False
            if event.from_user:
                vk.messages.send(
                    user_id=event.user_id,
                    message='Вас приветствует бот Enemyfear 😈.\nВот мои возможности 👽:',
                    keyboard = keyboard,
                    random_id=random.randint(-2147483648, +2147483648)
                    
		)
                understand = True
            elif event.from_chat:
                vk.messages.send(
                    chat_id=event.chat_id,
                    message='Ваш текст'
		)
        elif event.text.lower() == '❌ назад':
            understand = False
            g = False
            if event.from_user:
                if qwe:
                    keyboard101 = {
                    "one_time": False,
                    "buttons": [
                            [get_button(label="💰 Купить", color="positive")],
                            [get_button(label="🧠 Поддержка", color="primary")],
                            [get_button(label="🗿 Сайт", color="default")]
                    ]
                }

                    keyboard101 = json.dumps(keyboard101, ensure_ascii=False).encode('utf-8')
                    keyboard101 = str(keyboard101.decode('utf-8'))
                    vk.messages.send(
                        user_id = event.user_id,
                        keyboard = keyboard101,
                        message = "🤖 Главное меню",
                        random_id=random.randint(-2147483648, +2147483648)
                    )
                    qwe = False
                    understand = True
                elif back1 == False:
                    understand = False
                    keyboard100 = {
                    "one_time": False,
                    "buttons": [
                            [get_button(label="💰 Купить", color="positive")],
                            [get_button(label="🧠 Поддержка", color="primary")],
                            [get_button(label="🗿 Сайт", color="default")]
                    ]
                }

                    keyboard100 = json.dumps(keyboard100, ensure_ascii=False).encode('utf-8')
                    keyboard100 = str(keyboard100.decode('utf-8'))
                    vk.messages.send(
                        user_id = event.user_id,
                        keyboard = keyboard100,
                        message = "🤖 Главное меню",
                        random_id=random.randint(-2147483648, +2147483648)
                    )
                    understand = True
        elif event.text.lower() == '🧠 поддержка':
            understand = False
            if event.from_user:
                g = True
                keyboard3 = {
                    "one_time": False,
                    "buttons": [
                        [get_button(label="❌ Назад", color="negative")],
                        [get_button(label="🟣 Дискорд", color="primary")],
                        [get_button(label="🔵 Телеграмм", color="default")]
                    ]
                    }
                keyboard3 = json.dumps(keyboard3, ensure_ascii=False).encode('utf-8')
                keyboard3= str(keyboard3.decode('utf-8'))
                vk.messages.send(
                    user_id = event.user_id,
                    message='🎃 Пожалуйста, опишите вашу проблему максимально подробно и в скором времени с вами свяжется агент поддержки',
                    keyboard = keyboard3,
                    random_id=random.randint(-2147483648, +2147483648)
                )
                back1 = False
        elif event.text.lower() == '🔵 телеграмм':
            understand = False
            if event.from_user:
                vk.messages.send(
                    user_id = event.user_id,
                    #telegram group or bot
                    message='Пока не доступен:(',
                    random_id=random.randint(-2147483648, +2147483648)
                )
                understand = False
        elif event.text.lower() == '🟣 дискорд':
            understand = False
            if event.from_user:
                vk.messages.send(
                    user_id = event.user_id,
                    message='https://discord.gg/eUGYSnpk3b',
                    random_id=random.randint(-2147483648, +2147483648)
                )
                understand = True
        elif event.text.lower() == '🗿 сайт':
            understand = False
            if event.from_user:
                vk.messages.send(
                    user_id = event.user_id,
                    #site
                    message='https://enemyfear.xyz/',
                    random_id=random.randint(-2147483648, +2147483648)
                )
                understand = True
        elif event.text.lower() == '💰 купить':
            understand = False
            isinbuyloop = True
            if event.from_user:
                vk.messages.send(
                    user_id = event.user_id,
                    message='Пожалуйста, отправьте свою электронную почту',
                    random_id=random.randint(-2147483648, +2147483648)
                )
        elif event.text.lower() == 'admin':
            understand = False
            keys = True
            if event.from_user and str(event.user_id) in user:
                keyboard6 = {
                "one_time": False,
                "buttons": [
                    [get_button(label="ключик", color="default")],
                    [get_button(label="❌ Назад", color="negative")]
                    ]
                }
                keyboard6 = json.dumps(keyboard6, ensure_ascii=False).encode('utf-8')
                keyboard6= str(keyboard6.decode('utf-8'))
                vk.messages.send(
                    user_id = event.user_id,
                    message = '✔ Выполнен вход в админ панель',
                    keyboard = keyboard6,
                    random_id=random.randint(-2147483648, +2147483648)
                )
                qwe = True
                understand = True
        elif event.text.lower() == 'ключик':
            if event.from_user:
                if keys:
                    vk.messages.send(
                        user_id = event.user_id,
                        message = '✔ Создан ключик',
                        random_id=random.randint(-2147483648, +2147483648)
                    )
                    webapi = efapi() # Init class module
                    password = "4328799p8fdshnfd" # Password for api
                    key = webapi.createKey(password) # Generating key
                    vk.messages.send(
                        user_id = event.user_id,
                        message = str(key),
                        random_id=random.randint(-2147483648, +2147483648)
                    )
                    keys = False
                    understand = False
        else:
            if event.from_user and isinbuyloop:
                for item in user:
                    vk.messages.send(
                        user_id = item,
                        message = f"https://vk.com/id" + str(event.user_id) + " хочет купить",
                        random_id=random.randint(-2147483648, +2147483648)
                    )
                vk.messages.send(
                    user_id = event.user_id,
                    message = "💱 Ваш заказ передан на обработку, пожалуйста, ожидайте ответа от продавца...",
                    random_id=random.randint(-2147483648, +2147483648)
                )
                isinbuyloop = False
            elif event.from_user and g and back1 == False:
                for item in user:
                    vk.messages.send(
                        user_id = item,
                        message = f"https://vk.com/id" + str(event.user_id) + " нуждается в помощи!",
                        random_id=random.randint(-2147483648, +2147483648)
                    )
                    g = False
            elif event.from_user and understand:
                vk.messages.send(
                    user_id = event.user_id,
                    message = "Я тебя не понимаю 🤷. Попробуй написать другую команду",
                    random_id=random.randint(-2147483648, +2147483648)
                    )
