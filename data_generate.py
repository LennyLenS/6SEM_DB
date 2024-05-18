import random
import sqlite3

import secmail
from nickname_generator import generate
from password_generator import PasswordGenerator
from phone_gen import PhoneNumber

numberUser = 2000
numberStreamer = 20
numberModerator = 50
numberStream = 300
numberCategory = 10
numberTag = 8
numberMessage = 100
numberBan = 100
Moders = list()
Admins = list()


def CreateUsers(n):
    data = ""
    sec = secmail.SecMail()
    phone_number = PhoneNumber("Russian Federation")
    pwo = PasswordGenerator()
    for i in range(n):
        email = sec.generate_email(count=1)
        number = phone_number.get_number()
        passwrd = pwo.generate()
        nickname = generate()
        if i != n - 1:
            data += f"('{email}', '{passwrd}', '{email}', '{number}', '{nickname}'),"
        else:
            data += f"('{email}', '{passwrd}', '{email}', '{number}', '{nickname}');"
    command = "INSERT INTO User(Login, Password, Email, Phone_number, Nickname) VALUES " + data
    return command


def CreateStreamers(n):
    sponsors = ["" for i in range(25)]
    sponsors += [
        "Winline",
        "1xBet",
        "BetBoom",
        "Volt",
        "RedBull",
        "Genshin",
        "Coca-Cola",
        "Nestle",
        "VK",
        "Yandex",
    ]
    data = ""
    for i in range(n):
        if i != n - 1:
            data += f"('{sponsors[int(random.random() * 100) % 35]}', '{0}', '{0}', '{int(random.random() * numberUser)}'),"
        else:
            data += f"('{sponsors[int(random.random() * 100) % 35]}', '{0}', '{0}', '{int(random.random() * numberUser)}');"
    command = "INSERT INTO Streamer(Sponsor, Followers, Subscribers, User_id) VALUES " + data
    return command


def CreateModerators(n):
    data = ""
    usersList = random.sample(range(1, numberUser), n)
    for i in range(n):
        level_access = int(random.random() * 2)
        if level_access == 0:
            Moders.append(i)
        else:
            Admins.append(i)
        if i != n - 1:
            data += f"('{level_access}', '{usersList[i]}'),"
        else:
            data += f"('{level_access}', '{usersList[i]}');"
    command = "INSERT INTO Moderator(Level_access, User_id) VALUES " + data
    return command


def CreateCategory(n):
    data = ""
    command = (
        "INSERT INTO Category(Name) VALUES ('Just Chatting'), ('Tanki Online'), ('GTA'), ('Dota 2'), ('Hearthstone'), ('Minecraft'), ('Valorant'), ('CS2'), ('IRL'), ('Fortinite');"
        + data
    )
    return command


def CreateTag(n):
    data = ""
    command = "INSERT INTO Tag(Name) VALUES ('Anime'), ('Cybersport'), ('gay'), ('cs'), ('major'), ('tunder'), ('game'), ('unboxing');" + data
    return command


def CreateStreams(n):
    data = ""
    for i in range(n):
        if i != n - 1:
            data += f"('{generate()}', '{int(random.random() * 1000)}', '{int(random.random() * numberStreamer)}'),"
        else:
            data += f"('{generate()}', '{int(random.random() * 1000)}', '{int(random.random() * numberStreamer)}');"
    command = "INSERT INTO Stream(Name, Number_viewers, Streamer_id) VALUES " + data
    return command


def CreateBans(n):
    data = ""
    for i in range(n):
        moder = int(random.random() * numberModerator)
        streamer_id = "NULL"
        if moder in Moders:
            streamer_id = str(int(random.random() * numberStreamer))
        date = "2023-" + str(random.randint(0, 1)) + str(random.randint(1, 9)) + "-" + str(random.randint(0, 2)) + str(random.randint(1, 9))
        if i != n - 1:
            data += f"({int(random.random() * numberUser)}, {moder}, {streamer_id}, '{date}'),"
        else:
            data += f"({int(random.random() * numberUser)}, {moder}, {streamer_id}, '{date}');"
    command = "INSERT INTO Ban(User_id, Moderator_id, Streamer_id, Date) VALUES " + data
    return command


def CreateStreamCategory(n):
    data = ""
    for i in range(n):
        if i != n - 1:
            data += f"({int(random.random() * numberStream)}, {int(random.random() * numberCategory)}),"
        else:
            data += f"({int(random.random() * numberStream)}, {int(random.random() * numberCategory)});"
    command = "INSERT INTO StreamCategory(Stream_id, Category_id) VALUES " + data
    return command


def CreateStreamTag(n):
    data = ""
    for i in range(n):
        if i != n - 1:
            data += f"({int(random.random() * numberStream)}, {int(random.random() * numberTag)}),"
        else:
            data += f"({int(random.random() * numberStream)}, {int(random.random() * numberTag)});"
    command = "INSERT INTO StreamTag(Stream_id, Tag_id) VALUES " + data
    return command


def CreateStreamerModerator(n):
    data = ""
    for i in range(n):
        if i != n - 1:
            data += f"({Moders[random.randint(0, len(Moders) - 1)]}, {int(random.random() * numberStreamer)}),"
        else:
            data += f"({Moders[random.randint(0, len(Moders) - 1)]}, {int(random.random() * numberStreamer)});"
    command = "INSERT INTO StreamerModerator(Moderator_id, Streamer_id) VALUES " + data
    return command


def CreateSubscribers(n):
    data = ""
    for i in range(n):
        if i != n - 1:
            data += f"({random.randint(0, numberUser - 1)}, {int(random.random() * numberStreamer)}, {random.randint(0, 1)}),"
        else:
            data += f"({random.randint(0, numberUser - 1)}, {int(random.random() * numberStreamer)}, {random.randint(0, 1)});"
    command = "INSERT INTO Subscribe(User_id, Streamer_id, Type) VALUES " + data
    return command


def CreateChatRules(n):
    data = ""
    for i in range(n):
        if i != n - 1:
            data += f"({random.randint(0, 20)}, {random.randint(0, 1)}, {random.randint(0, 1)}, {int(random.random() * numberStreamer)}),"
        else:
            data += f"({random.randint(0, 20)}, {random.randint(0, 1)}, {random.randint(0, 1)}, {int(random.random() * numberStreamer)});"
    command = "INSERT INTO ChatRule(Delay, Only_followers, Only_subscribers, Streamer_id) VALUES " + data
    return command


def CreateMessages(n):
    random_words = [
        "apple",
        "banana",
        "cat",
        "dog",
        "elephant",
        "fish",
        "guitar",
        "hat",
        "ice cream",
        "jacket",
        "kite",
        "lemon",
        "mouse",
        "notebook",
        "orange",
        "piano",
        "queen",
        "rabbit",
        "sun",
        "tiger",
        "umbrella",
        "violin",
        "watermelon",
        "xylophone",
        "yacht",
        "zebra",
        "car",
        "book",
        "tree",
        "house",
        "ball",
        "computer",
        "lamp",
        "desk",
        "chair",
        "flower",
        "moon",
        "star",
        "plane",
        "train",
        "bus",
        "truck",
        "bird",
        "butterfly",
        "snake",
        "lion",
        "turtle",
        "robot",
    ]
    data = ""
    for i in range(n):
        mes_size = random.randint(1, 5) + 1
        message = ""
        for j in range(mes_size):
            message += random.choice(random_words) + " "
        date = "2023-" + str(random.randint(0, 1)) + str(random.randint(1, 9)) + "-" + str(random.randint(0, 2)) + str(random.randint(1, 9))
        if i != n - 1:
            data += f"('{message}', '{date}', {int(random.random() * numberStream)}, {int(random.random() * numberUser)}),"
        else:
            data += f"('{message}', '{date}', {int(random.random() * numberStream)}, {int(random.random() * numberUser)});"
    command = "INSERT INTO Message(Text, Date, Stream_id, User_id) VALUES " + data
    return command


connection = sqlite3.connect("DB")
cursor = connection.cursor()
# cursor.execute(CreateUsers(numberUser))
# print("Users created")
# cursor.execute(CreateStreamers(numberStreamer))
# print("Streamers created")
# cursor.execute(CreateModerators(numberModerator))
# print("Moderators created")
# cursor.execute(CreateCategory(numberStreamer))
# print("Category created")
# cursor.execute(CreateTag(numberTag))
# print("Tag created")
# cursor.execute(CreateStreams(numberStream))
# print("Stream created")
# cursor.execute(CreateBans(numberBan))
# print("Ban created")
# cursor.execute(CreateStreamerModerator(40))
# print("StreamerMOder created")
# cursor.execute(CreateSubscribers(300))
# print("Subs created")
# cursor.execute(CreateChatRules(10))
# print("Rules created")
cursor.execute(CreateMessages(2000))
print("Message created")
# cursor.execute(CreateStreamTag(60))
# print("stream tag created")
# cursor.execute(CreateStreamCategory(30))
connection.commit()
connection.close()
