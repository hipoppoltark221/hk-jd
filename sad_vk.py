import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
key = "db758977181336e729bf3b379163b461a953efa30b350dfd9e8479df809711783f864f530611c694b9d28"
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
key = "db758977181336e729bf3b379163b461a953efa30b350dfd9e8479df809711783f864f530611c694b9d28"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message):
    from random import randint
    vk.method('messages.send',
              {'user_id': user_id,
               "random_id":randint(1,1000) ,
               'message': message,}
              )
WHAT = """what?
    supported commands:
    hello
            game
кот
"""
dev_id = 546922354
send_message(dev_id,'hi i am alive')
debug = False
# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            if user_id == dev_id:
                if text == 'debug':
                    debug = not debug
                    send_message(dev_id,'debug is now '+str(debug))
                if debug:
                    text = ''
                    for i in dir(event):
                        if i[0]!='_':
                            send_message(dev_id,i+' : '+str(eval('event.'+i)))
                    continue
            if text == "hello":
                send_message(user_id,str(user_id))
            elif text == "game":
                game_mod = True
                chislo = randint(1,100)
                gamers[user_id] = chislo
                send_message(user_id, "гони с украденным дощиком")
            elif "кот" in text:
                send_message(user_id, "пошел в пень ")
            elif user_id in gamers:
                chislo = gamers[user_id]
                x = int(text)
                if chislo < x:
                    send_message(user_id,"мое число наверное может быть меньше")
                elif chislo > x:
                    send_message(user_id,"моя число наверное может быть больше")
                elif chislo == x:
                    send_message(user_id,"ты выйграл все отвали!")
                    del gamers[user_id]
                    game_mode = False
            else:
                send_message(user_id, WHAT)
