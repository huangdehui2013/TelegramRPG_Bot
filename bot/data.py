# coding=utf-8
"""
Игровые данные
"""

# Обязательно проверяем, что в топ-100 есть все эти диалоги
TELEGRAM = 777000    # Telegram
GAME = 265204902     # Бот игры
TRADE = 278525885    # Бот торговли
CAPTCHA = 313998026  # Бот капчи
ENOT = 402544905     # Бот Енот (Пингвин) — склад

CHATS = [TELEGRAM, GAME, TRADE, CAPTCHA, ENOT]

WAR = {
    "Красный": "🇮🇲",
    "Черный": "🇬🇵",
    "Белый": "🇨🇾",
    "Желтый": "🇻🇦",
    "Синий": "🇪🇺",
    "Мятный": "🇲🇴",
    "Сумрачный": "🇰🇮",
    "Лесной форт": "🌲Лесной форт",
    "Горный форт": "⛰Горный форт",
    "Морской форт": "⚓Морской форт",
}

WAR_COMMANDS = {
    "к": "Красный",
    "ч": "Черный",
    "б": "Белый",
    "ж": "Желтый",
    "с": "Синий",
    "м": "Мятный",
    "у": "Сумрачный",
    "л": "Лесной форт",
    "г": "Горный форт",
    "о": "Морской форт",
}

GENITIVES = {
    "Красного": "Красный",
    "Синего": "Синий",
    "Черного": "Черный",
    "Белого": "Белый",
    "Желтого": "Желтый",
    "Мятного": "Мятный",
    "Сумрачного": "Сумрачный",
}

ATTACK = "⚔Атака"
DEFEND = "🛡Защита"
ALLY = "Союзник"
WIND = "Ветер"
VICTORIES = "🤺Побед"  # используем для проверки на /hero

REGROUP = "!!"  # забываем приказ

VERBS = {
    True: {},
    False: {
        0: "Пропустил",
        4: "Защищал",
        5: "Атаковал",
    }
}

for verb, string in VERBS[False].items():
    VERBS[True][verb] = string + "а "
    VERBS[False][verb] = string + " "

RIGHT = "правую руку"  # мечи, копья, кирки и молоты
LEFT = "левую руку"    # кинжалы и щиты
HANDS = {
    DEFEND: "предмет для защиты на ",
    ATTACK: "предмет для атаки на "
}

EQUIP = {
    RIGHT: {
        # (!) добавить копья и набор для крафта, если появятся копья
        100: {ATTACK: 1, DEFEND: 0},    # меч ученика
        101: {ATTACK: 3, DEFEND: 0},    # короткий меч
        102: {ATTACK: 6, DEFEND: 0},    # длинный меч
        103: {ATTACK: 10, DEFEND: 0},   # меч вдовы
        104: {ATTACK: 16, DEFEND: 0},
        105: {ATTACK: 18, DEFEND: 2},   # эльфийский меч
        106: {ATTACK: 22, DEFEND: 0},   # рапира
        119: {ATTACK: 3, DEFEND: 3},    # кирка
        120: {ATTACK: 14, DEFEND: 17},  # молот гномов
    },
    LEFT: {
        # (!) добавить все предметы
        112: {ATTACK: 1, DEFEND: 0},    # кухонный нож
        113: {ATTACK: 3, DEFEND: 0},    # боевой нож
        114: {ATTACK: 7, DEFEND: 0},    # кинжал
        123: {ATTACK: 9, DEFEND: 5},    # клещи
        212: {ATTACK: 0, DEFEND: 1},    # деревянный щит
        213: {ATTACK: 0, DEFEND: 2},    # щит скелета
        214: {ATTACK: 0, DEFEND: 3},    # бронзовый щит
        215: {ATTACK: 0, DEFEND: 5},    # серебряный щит
        216: {ATTACK: 0, DEFEND: 7},    # мифриловый щит
    },
}

# Парсер не справляется со смайликом и тегом ``
HELLO = "{} Просыпается {}, фармитель {}-го уровня!"
SENDING = "Пересылаю {} {}-й раз из `{}`"

HERO = "🏅Герой"

COOLDOWN = 7200           # Минимальное время между усталостью
MONSTER_COOLDOWN = 86400  # Время между монстрами

FIGHT = "/fight"

LEVEL_UP = "/level_up"
PLUS_ONE = {
    ATTACK: "+1 ⚔Атака",  # Увеличиваем атаку каждый уровень
    DEFEND: "+1 🛡Защита"  # или защиту
}

QUESTS = "🗺 Квесты"

WOODS = "🌲Лес"
CAVE = "🕸Пещера"
SHORE = "🏝Побережье"
CARAVANS = "🐫ГРАБИТЬ КОРОВАНЫ"
BUSY = "сейчас занят другим приключением"
