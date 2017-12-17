# coding=utf-8
"""
Образец файла sessions, на основе которого будут созданы остальные боты.

Для работы создаем свой файл sessions.py на основе этого файла,
подставляя в него значения для каждого аккаунта.

Название сессии не чувствительно к регистру.
С 15-го уровня становится доступен ChatWarsTradeBot.
Уровень, с которого стоит ходить в пещеру, устанавливаем сами.

Перед первым запуском на всякий случай проверьте,
что бот надел лучшую одежду для защиты и сбора.

Бот требует наличия в десяти первых диалогах:
    * Бота игры @ChatWarsBot
    * Бота Капчеватора для капчи @ChatWarsCaptchaBot
    * Бота торговли @ChatWarsTradeBot
    * Бота Енота для стока твинков @enotobot

А также общего канала, в которую он будет отписываться
о боях и командах. В эту же группу перед боем отправляем приказ.

Параметры для вызова main.py:
    -s: логгирует в файл logs/НазваниеСессии.log, а не в стандартный вывод.
    -l: (только для одного пользователя)
        Используем для первого ввода кода и создания файла .session
    -r: «перезапуск»: все действия откладываются, чтобы не спамить
        при массовых перезагрузках.

Команды-приказы — куда бот пойдет в атаку.
Не чувствительны к регистру.
Если совпадает с цветом замка или союзника, бот остается в защите.
    к: Красный,
    ч: Черный,
    б: Белый,
    ж: Желтый,
    с: Синий,
    м: Мятный,
    у: Сумеречный,
    л: Лесной форт,
    г: Горный форт,
    о: Морской форт

Сейчас бот умеет:
    * Ходить в пещеру, лес, на побережье и к караванам
    * Ходить в бой
    * Надевать свои лучшие предметы перед атакой и защитой
    * Помогать с монстрами /fight
    * Защищать КОРОВАНЫ /go
    * Понимать прямые команды

Прямые команды отправляются в общую группу в формате:
Префикс От (До): Команда x Раз, где:
    Префикс определяет, каким конкретно ботам реагировать на команду.
        Возможные значения:
            !! — всем ботам в чате
            Смайлик-флага — только воинам определенного замка
            Название-сессии — только конкретному боту

    От определяет минимальный порог уровня для отправки команды.
    До определяет максимальный порог уровня для отправки команды. Необязателен.

    Команда будет в точности передан боту. Не ошибитесь!
    Раз определяет, сколько раз подряд передать команду. Полезно для строек.

Примеры:
    !!: /repair_wall x 5 — всем воинам отправиться на починку стены 5 раз
    🇮🇲 26 35: /fight_b1 — всем воинам замка 🇮🇲 c 26 по 35 уровень отправиться в бой
    A1: /report — боту с названием сессии A1 отправить свой отчет

После отправки команды и небольшой задержки ― до 5 минут на стройке ―
бот перешлет последнее сообщение от бота игры.
"""

from bot.data import LEVEL_UP, DEFEND, WOODS, CAVE, SHORE, CARAVANS


# Берем из Телеграма
API_ID = 123456
API_HASH = "0123456789abcdef0123456789abcdef"

# ТГ номер супергруппы, в которую будем писать о боях
SUPERGROUP = 1123894847

# Данные по каждой локации для посещения в порядке приоритетности
# command: текст команды
# level: минимальный уровень для посещения
# chance: среднее вероятность того, что Фармитель пойдет в эту локацию

# Пример приключений. Создаем сколько угодно и выставляем нужным.
MASTER = [
    {"command": SHORE, "level": 0, "chance": 0},
    {"command": CAVE, "level": 55, "chance": 1},     # ходит с 55-го уровня
    {"command": CARAVANS, "level": 0, "chance": 0},
    {"command": WOODS, "level": 0, "chance": 1},
]

SESSIONS = {
    "S1": {                       # запуск: python main.py s1, лог: s1.log
        "phone": "+12345678901",
        "girl": True,             # влияет на род глаголов в 3-м лице :)
        "adventures": MASTER,     # локации на выбор, по умоланию ходит в лес
        LEVEL_UP: DEFEND,         # атрибут на выбор, по умолчанию — атака
    },

    "Session-2": {                # продолжаем для второго аккаунта
    }                             # запуск обоих: python main.py s1 session-2
}
