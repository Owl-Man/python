import random

locked_symbol = '\u25A0'
heart_symbol = '\u2764'

current_session_record = 0
record = 0

with open('C:\\Users\\Student\\PycharmProjects\\python\\PracticalTasks\\WheelOfFortune\\record_db', encoding='UTF-8') as db:
    record = int(db.read())

words_list = []
with open('C:\\Users\\Student\\PycharmProjects\\python\\PracticalTasks\\WheelOfFortune\\words_db', encoding='UTF-8') as db:
    words_list = db.read().splitlines()


def get_random_word():
    word = random.choice(words_list)
    words_list.remove(word)
    return word


def update_record():
    with open('record_db', encoding='UTF-8', mode='w') as db:
        db.write(str(record))