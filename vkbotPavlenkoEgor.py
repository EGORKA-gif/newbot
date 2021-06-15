import requests
import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token='768f2d28e05dbaf52bc5a4f5ae5989a2a982ba2616547a686491a784af7b552fe9ea0e8144312ea96ec71')

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()
playing_users = {}
users = {}
photos=['photo-205227902_457239020',
'photo-205227902_457239022',]
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        if event.text == 'привет':
            vk.messages.send(
                user_id=event.user_id,
                random_id=random.randint(0, 100000),
                message='и тебе привет'
                )
        elif event.text == 'bingus':
            vk.messages.send(
                user_id=event.user_id,
                random_id=random.randint(0, 100000),
                attachment='photo-205227902_457239021',
                message = "BingusGang))"
            )
        elif event.text == '/comands':
            vk.messages.send(
                user_id=event.user_id,
                random_id=random.randint(0, 100000),
                message = "Если ты играешь, то пиши только числа:)\nСписок команд:\nfloppa\nbingus\nпривет\nпока\nкд?\nчд?\nдавай сыграем"
            )
        elif event.text == 'floppa':
            vk.messages.send(
                user_id=event.user_id,
                random_id=random.randint(0, 100000),
                attachment=random.choice(photos),
                message = "FloppaGang))"
            )
        elif event.text == 'пока':
            vk.messages.send(
                user_id=event.user_id,
                random_id=random.randint(0, 100000),
                message='пока'
                )
        elif event.text == 'кд?':
            nastorenie = random.randint(0,1)
            if int(nastorenie) == 0:
                x='норм'
            else:
                x='балдёжно'
            vk.messages.send(
            user_id=event.user_id,
            random_id=random.randint(0, 100000),
            message = x
            )
        elif event.text == 'чд?':
            dela = random.randint(0,2)
            if int(dela) == 0:
                y='кушаю'
            else:
                if int(dela) == 1:
                    y='сплю, не мешай'
                else:
                    y='смотрю футбол'
            vk.messages.send(
            user_id=event.user_id,
            random_id=random.randint(0, 100000),
            message = y
            )
        elif event.text == 'давай сыграем':
            users[event.user_id] = random.randint(1,1000)
            vk.messages.send(
                    user_id=event.user_id,
                    random_id=random.randint(0, 100000),
                    message = "я загадал число, попробуй его отгадать"
                )
        elif event.user_id in users:
            if event.text.isdigit():
                if users[event.user_id] == int(event.text):
                    vk.messages.send(
                        user_id=event.user_id,
                        random_id=random.randint(0, 100000),
                        message = "правильно, ты угадал"
                    )
                else:
                    if users[event.user_id] > int(event.text):
                        vk.messages.send(
                            user_id = event.user_id,
                            random_id=random.randint(0, 100000),
                            message = "твоё число меньше загаданного"
                        )
                    else:
                        vk.messages.send(
                            user_id = event.user_id,
                            random_id=random.randint(0, 100000),
                            message = "твоё число больше загаданного"
                        )      
            else:
                vk.messages.send(
                    user_id = event.user_id,
                    random_id=random.randint(0, 100000),
                    message = "Я тебя не понимаю, если ты играешь в игру,то пиши только числа.\nЕсли ты хочешь увидеть полный список команд - напиши /comands"
                )
        else:
            vk.messages.send(
                user_id = event.user_id,
                random_id=random.randint(0, 100000),
                message = "Я тебя не понимаю, если ты играешь в игру,то пиши только числа.\nЕсли ты хочешь увидеть полный список команд - напиши /comands"
            )
